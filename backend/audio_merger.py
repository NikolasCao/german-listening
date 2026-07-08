"""
音频合成模块 —— 将多段 MP3 拼接为完整音频
纯 Python 实现，正确匹配 edge-tts 输出格式
"""

import os
import struct


def _strip_id3(data: bytes) -> bytes:
    """移除 MP3 文件头部的 ID3 标签（如果有）"""
    if len(data) > 10 and data[:3] == b"ID3":
        size_bytes = data[6:10]
        size = (size_bytes[0] << 21) | (size_bytes[1] << 14) | (size_bytes[2] << 7) | size_bytes[3]
        return data[10 + size:]
    return data


def _detect_mp3_format(data: bytes) -> dict:
    """
    从 MP3 数据中检测帧格式。
    edge-tts 通常输出 MPEG2 Layer3 48kbps 24000Hz Mono。
    """
    data = _strip_id3(data)
    for i in range(min(len(data) - 4, 4096)):
        if data[i] == 0xFF and (data[i + 1] & 0xE0) == 0xE0:
            b1, b2, b3 = data[i + 1], data[i + 2], data[i + 3]
            version_id = (b1 >> 3) & 3   # 0=2.5, 2=2, 3=1
            layer_id = (b1 >> 1) & 3     # 1=Layer3
            bitrate_idx = (b2 >> 4) & 0xF
            sample_idx = (b2 >> 2) & 3
            padding = (b2 >> 1) & 1
            mono = (b3 >> 6) & 3 == 3

            # Bitrate tables
            if version_id == 3:  # MPEG1
                br_table = [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0]
                sr_table = {0: 44100, 1: 48000, 2: 32000}
                frame_factor = 144
            else:  # MPEG2 or 2.5
                br_table = [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0]
                sr_table = {0: 22050, 1: 24000, 2: 16000}
                if version_id == 0:  # MPEG2.5
                    sr_table = {0: 11025, 1: 12000, 2: 8000}
                frame_factor = 72

            bitrate = br_table[bitrate_idx] if 0 < bitrate_idx < 15 else 48
            sample_rate = sr_table.get(sample_idx, 24000)

            # Frame size calculation
            if sample_rate > 0 and bitrate > 0:
                frame_size = frame_factor * bitrate * 1000 // sample_rate + padding
            else:
                frame_size = 144  # fallback for MPEG2 48kbps 24kHz

            # Frame duration in ms
            if version_id == 3:
                frame_duration_ms = 1152 * 1000 // sample_rate
            else:
                frame_duration_ms = 576 * 1000 // sample_rate

            return {
                "version_id": version_id,
                "header_bytes": bytes([data[i], data[i + 1], data[i + 2], data[i + 3]]),
                "bitrate": bitrate,
                "sample_rate": sample_rate,
                "frame_size": frame_size,
                "frame_duration_ms": frame_duration_ms,
                "mono": mono,
            }

    # Fallback: assume MPEG2 48kbps 24000Hz (edge-tts default)
    return {
        "version_id": 2,
        "header_bytes": bytes([0xFF, 0xF3, 0x64, 0xC4]),
        "bitrate": 48,
        "sample_rate": 24000,
        "frame_size": 144,
        "frame_duration_ms": 24,  # 576/24000*1000
        "mono": True,
    }


def _create_silence_frame(fmt: dict) -> bytes:
    """创建一个正确格式的静音 MP3 帧"""
    header = fmt["header_bytes"]
    frame_size = fmt["frame_size"]
    # 帧头 4 字节 + 剩余填充零
    return header + bytes(frame_size - 4)


def _create_silence(duration_ms: int, fmt: dict) -> bytes:
    """创建指定时长的静音 MP3 数据，使用正确格式"""
    frame_dur = fmt["frame_duration_ms"]
    num_frames = max(1, int(duration_ms / frame_dur))
    silent_frame = _create_silence_frame(fmt)
    return silent_frame * num_frames


def _strip_xing_frame(data: bytes, fmt: dict) -> bytes:
    """检测并移除第一个帧中的 Xing/Info VBR 头（如果存在）"""
    frame_size = fmt["frame_size"]
    if len(data) < frame_size + 4:
        return data

    # Xing/Info 标签位置: MPEG1 在 offset 36, MPEG2/2.5 在 offset 21
    if fmt["version_id"] == 3:  # MPEG1
        xing_offset = 36
    else:
        xing_offset = 21

    if xing_offset + 4 <= len(data):
        tag = data[xing_offset:xing_offset + 4]
        if tag in (b"Xing", b"Info"):
            # 这是一个 VBR 信息帧，移除它
            return data[frame_size:]

    return data


def merge_mp3_files(file_paths: list[str], output_path: str, gap_ms: int = 400) -> bool:
    """
    将多个 MP3 文件合并为一个，支持句间停顿。
    自动检测 edge-tts 输出格式并生成匹配的静音帧。

    Args:
        file_paths: MP3 文件路径列表（按顺序）
        output_path: 输出文件路径
        gap_ms: 句子之间的停顿毫秒数（默认 400ms）

    Returns:
        True 如果合并成功
    """
    try:
        if not file_paths:
            return False

        # 读取所有文件数据
        all_data = []
        for path in file_paths:
            if not os.path.exists(path):
                print(f"[AudioMerger] 文件不存在: {path}")
                continue
            with open(path, "rb") as f:
                raw = f.read()
            # 移除 ID3 标签
            audio_data = _strip_id3(raw)
            all_data.append(audio_data)

        if not all_data:
            return False

        # 从第一个文件检测 MP3 格式
        fmt = _detect_mp3_format(all_data[0])
        print(f"[AudioMerger] 检测到格式: {fmt['bitrate']}kbps {fmt['sample_rate']}Hz "
              f"frame_size={fmt['frame_size']} frame_dur={fmt['frame_duration_ms']}ms")

        # 生成正确格式的静音数据
        silence_data = _create_silence(gap_ms, fmt) if gap_ms > 0 else b""

        merged = bytearray()

        for i, data in enumerate(all_data):
            # 移除可能的 Xing/Info VBR 头帧
            clean_data = _strip_xing_frame(data, fmt)
            merged.extend(clean_data)

            # 在段落之间插入正确格式的静音
            if i < len(all_data) - 1 and gap_ms > 0:
                merged.extend(silence_data)

        with open(output_path, "wb") as f:
            f.write(bytes(merged))

        result_size = os.path.getsize(output_path)
        print(f"[AudioMerger] 合并完成: {len(all_data)} 段, 输出 {result_size} 字节")
        return result_size > 0

    except Exception as e:
        print(f"[AudioMerger] 合并失败: {e}")
        return False


def cleanup_temp_files(temp_dir: str, pattern: str = "*_seg*.mp3"):
    """清理临时音频片段文件"""
    import glob
    for f in glob.glob(os.path.join(temp_dir, pattern)):
        try:
            os.remove(f)
        except Exception:
            pass
