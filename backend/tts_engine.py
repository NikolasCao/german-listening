"""
德语 TTS 引擎 —— 基于 edge-tts 的微软神经语音
专为德语优化，支持多角色不同声线分配
"""

import asyncio
import os
import uuid
from typing import Optional
import edge_tts

# ==================== 德语语音库 ====================
# 5 个女声 + 5 个男声，涵盖德德/奥德/瑞德口音
GERMAN_VOICES = {
    "female": [
        "de-DE-KatjaNeural",            # 标准 德德 女声
        "de-DE-AmalaNeural",            # 年轻 德德 女声
        "de-DE-SeraphinaMultilingualNeural",  # 多语言 女声
        "de-AT-IngridNeural",           # 奥地利 女声
        "de-CH-LeniNeural",             # 瑞士 女声
    ],
    "male": [
        "de-DE-ConradNeural",           # 标准 德德 男声
        "de-DE-KillianNeural",          # 年轻 德德 男声
        "de-DE-FlorianMultilingualNeural",    # 多语言 男声
        "de-AT-JonasNeural",            # 奥地利 男声
        "de-CH-JanNeural",              # 瑞士 男声
    ],
}


class GermanTTSEngine:
    """德语 TTS 引擎：为多角色对话自动分配不同声线"""

    def __init__(self, output_dir: str = "output"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def _assign_voices(self, speakers: list[dict]) -> dict[str, str]:
        """
        为每个说话者分配一个德语语音。
        策略：同性别轮流使用不同声线，确保角色区分度。
        """
        voice_map = {}
        female_idx = 0
        male_idx = 0

        for speaker in speakers:
            name = speaker.get("name", "Speaker")
            gender = speaker.get("gender", "female").lower()

            if gender == "male":
                voice_map[name] = GERMAN_VOICES["male"][male_idx % len(GERMAN_VOICES["male"])]
                male_idx += 1
            else:
                voice_map[name] = GERMAN_VOICES["female"][female_idx % len(GERMAN_VOICES["female"])]
                female_idx += 1

        return voice_map

    async def _generate_single(
        self,
        text: str,
        voice: str,
        output_path: str,
        rate: str = "+0%",
        pitch: str = "+0Hz",
    ) -> bool:
        """为单句文本生成德语音频"""
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice=voice,
                rate=rate,
                pitch=pitch,
            )
            await communicate.save(output_path)
            return os.path.exists(output_path) and os.path.getsize(output_path) > 0
        except Exception as e:
            print(f"[TTS] 生成失败 (voice={voice}): {e}")
            return False

    async def generate_audio(
        self,
        text_segments: list[dict],
        speakers: list[dict],
        output_filename: Optional[str] = None,
    ) -> dict:
        """
        为听力原文生成完整音频。

        Args:
            text_segments: [{"speaker": "Anna", "text": "Hallo!"}, ...]
            speakers: [{"name": "Anna", "gender": "female"}, ...]
            output_filename: 输出文件名（不含路径）

        Returns:
            {
                "success": bool,
                "audio_path": str,         # 合并后音频相对路径
                "segments": [...],          # 各段音频信息
                "voice_map": {...},         # 说话者->语音映射
                "error": str | None
            }
        """
        if not output_filename:
            output_filename = f"audio_{uuid.uuid4().hex[:8]}"

        voice_map = self._assign_voices(speakers)

        # 为每段文本生成单独的音频文件
        segment_files = []
        temp_dir = os.path.join(self.output_dir, "temp")
        os.makedirs(temp_dir, exist_ok=True)

        tasks = []
        for i, seg in enumerate(text_segments):
            speaker = seg.get("speaker", "")
            text = seg.get("text", "").strip()
            if not text:
                continue

            voice = voice_map.get(speaker, GERMAN_VOICES["female"][0])
            seg_filename = f"{output_filename}_seg{i:03d}.mp3"
            seg_path = os.path.join(temp_dir, seg_filename)

            tasks.append(self._generate_single(text, voice, seg_path))
            segment_files.append({
                "index": i,
                "speaker": speaker,
                "voice": voice,
                "text": text,
                "filepath": seg_path,
            })

        # 并行生成所有语音片段
        results = await asyncio.gather(*tasks)

        # 检查生成结果
        for i, (success, seg_info) in enumerate(zip(results, segment_files)):
            seg_info["success"] = success

        failed = [s for s in segment_files if not s.get("success")]
        if failed:
            return {
                "success": False,
                "audio_path": None,
                "segments": segment_files,
                "voice_map": voice_map,
                "error": f"{len(failed)} 个语音片段生成失败",
            }

        # 合并音频文件
        from backend.audio_merger import merge_mp3_files

        merged_path = os.path.join(self.output_dir, f"{output_filename}.mp3")
        file_paths = [s["filepath"] for s in segment_files]
        merge_success = merge_mp3_files(file_paths, merged_path, gap_ms=400)

        return {
            "success": merge_success,
            "audio_path": f"output/{output_filename}.mp3" if merge_success else None,
            "segments": segment_files,
            "voice_map": voice_map,
            "error": None if merge_success else "音频合并失败",
        }
