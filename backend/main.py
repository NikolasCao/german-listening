"""
德语听力生成器 —— FastAPI 后端主服务
"""

import os
import sys
import uuid
import time
from contextlib import asynccontextmanager
from pathlib import Path

# Windows 控制台 UTF-8 支持
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from fastapi import FastAPI
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# 确保能导入 backend 模块
sys.path.insert(0, str(Path(__file__).parent.parent))

from backend.tts_engine import GermanTTSEngine
from backend.content_generator import generate_content
from backend.audio_merger import cleanup_temp_files

# ==================== 路径配置 ====================
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
OUTPUT_DIR = BASE_DIR / "output"
OUTPUT_DIR.mkdir(exist_ok=True)


# ==================== 生命周期管理 ====================
@asynccontextmanager
async def lifespan(app: FastAPI):
    """启动时清理超过 1 小时的旧音频文件和临时片段"""
    now = time.time()
    for f in OUTPUT_DIR.glob("audio_*.mp3"):
        try:
            if now - f.stat().st_mtime > 3600:
                f.unlink()
        except Exception:
            pass
    # 清理 temp 目录中的残留片段
    temp_dir = OUTPUT_DIR / "temp"
    if temp_dir.exists():
        for f in temp_dir.glob("*_seg*.mp3"):
            try:
                f.unlink()
            except Exception:
                pass
    yield


# ==================== FastAPI 应用 ====================
app = FastAPI(title="Deutsches Hörverständnis Generator", lifespan=lifespan)

# 挂载静态文件
app.mount("/static", StaticFiles(directory=str(STATIC_DIR)), name="static")
app.mount("/audio", StaticFiles(directory=str(OUTPUT_DIR)), name="audio")

# TTS 引擎实例
tts_engine = GermanTTSEngine(output_dir=str(OUTPUT_DIR))


# ==================== 请求模型 ====================
class GenerateRequest(BaseModel):
    identity: str = "student"        # teacher / student
    difficulty: str = "A1"           # A1-C2
    question_type: str = "选择题"    # 选择题/填空题/解答题
    theme: str = "Begrüßung"         # 主题


# ==================== API 接口 ====================
@app.get("/api/status")
async def status():
    """检查服务状态和 LLM 配置"""
    from backend.content_generator import LLM_API_KEY, LLM_MODEL
    return {
        "status": "ok",
        "llm_configured": bool(LLM_API_KEY and LLM_API_KEY != "your-api-key-here"),
        "llm_model": LLM_MODEL if LLM_API_KEY else None,
    }


@app.post("/api/generate")
async def generate(req: GenerateRequest):
    """
    生成德语听力练习。

    请求参数:
    - identity: teacher / student
    - difficulty: A1, A2, B1, B2, C1, C2
    - question_type: 选择题, 填空题, 解答题
    - theme: 主题（德语或中文均可）

    返回:
    - content: 听力原文、题目、答案
    - audio_url: 音频文件 URL
    - voice_map: 说话者->语音映射
    """
    # 1. 生成内容
    content_result = await generate_content(
        difficulty=req.difficulty,
        question_type=req.question_type,
        theme=req.theme,
    )

    if not content_result["success"]:
        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "error": content_result["error"],
                "source": content_result["source"],
            },
        )

    data = content_result["data"]

    # 2. 生成 TTS 音频
    audio_filename = f"audio_{uuid.uuid4().hex[:8]}"
    tts_result = await tts_engine.generate_audio(
        text_segments=data.get("text_segments", []),
        speakers=data.get("speakers", []),
        output_filename=audio_filename,
    )

    # 3. 清理临时文件
    temp_dir = OUTPUT_DIR / "temp"
    cleanup_temp_files(str(temp_dir))

    # 4. 构建响应
    response = {
        "success": True,
        "source": content_result["source"],
        "identity": req.identity,
        "difficulty": req.difficulty,
        "question_type": req.question_type,
        "theme": req.theme,
        "content": {
            "title": data.get("title", ""),
            "description": data.get("description", ""),
            "text_type": data.get("text_type", "monologue"),
            "speakers": data.get("speakers", []),
            "text_segments": data.get("text_segments", []),
            "questions": data.get("questions", []),
        },
        "audio_url": f"/audio/{audio_filename}.mp3" if tts_result["success"] else None,
        "voice_map": tts_result.get("voice_map", {}),
        "tts_error": tts_result.get("error") if not tts_result["success"] else None,
    }

    return response


@app.get("/")
async def index():
    """返回主页面"""
    return FileResponse(str(STATIC_DIR / "index.html"))


if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8765))
    print("=" * 50)
    print("  Deutsches Hörverständnis Generator")
    print(f"  http://localhost:{port}")
    print("=" * 50)
    uvicorn.run(app, host="0.0.0.0", port=port)
