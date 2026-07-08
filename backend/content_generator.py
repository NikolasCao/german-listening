"""
内容生成模块 —— 通过 LLM API 生成德语听力原文、题目和答案
支持 OpenAI 兼容接口，无 API Key 时使用内置 Demo 内容
"""

import json
import os
import random
from typing import Optional

import httpx
from dotenv import load_dotenv

load_dotenv()

from backend.demo_content import get_demo_content, DEMO_AVAILABLE


# ==================== 配置 ====================
LLM_API_KEY = os.getenv("LLM_API_KEY", "").strip()
LLM_API_BASE = os.getenv("LLM_API_BASE", "https://api.openai.com/v1").strip()
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o").strip()


# ==================== LLM Prompt 模板 ====================
SYSTEM_PROMPT = """Du bist ein Experte für Deutsch als Fremdsprache (DaF) und erstellst Hörverständnisübungen.
Du generierst Übungen auf Deutsch, die genau dem angegebenen CEFR-Niveau entsprechen."""

QUESTION_TYPE_MAP = {
    "选择题": "Multiple-Choice-Fragen (4 Optionen: A, B, C, D)",
    "填空题": "Lückentext (Sätze mit fehlenden Wörtern)",
    "解答题": "Offene Fragen (freie Antworten)",
}

CEFR_GUIDE = {
    "A1": ("Sehr einfache Sätze, Grundwortschatz, NUR Präsens. Kurze Texte (4-6 Sätze). "
           "Alltägliche Situationen. Keine Nebensätze, keine komplexen Grammatik."),
    "A2": ("Einfache Sätze, Alltagswortschatz, Präsens und einfaches Präteritum/Perfekt. "
           "Kurze Texte (6-8 Sätze). Einfache weil/dass-Sätze erlaubt."),
    "B1": ("Mittelschwere Sätze, breiterer Wortschatz, verschiedene Zeitformen (Präsens, "
           "Präteritum, Perfekt, Plusquamperfekt). Mittlere Texte (8-12 Sätze). "
           "VERWENDEN Sie: Nebensätze (dass, weil, obwohl, wenn), Relativsätze, "
           "Modalverben in allen Zeitformen, Passiv, Konjunktiv II. "
           "Das Niveau MUSS deutlich schwerer sein als A2."),
    "B2": ("Komplexe Sätze, fortgeschrittener Wortschatz, Redewendungen. "
           "Mittlere Texte (12-15 Sätze). Abstrakte Themen. "
           "VERWENDEN Sie: verschachtelte Nebensätze, Passiv mit Modalverben, "
           "Konjunktiv I und II, Partizipialkonstruktionen, Nominalstil."),
    "C1": ("Sehr komplexe Sprache, akademischer/professioneller Wortschatz. "
           "Lange Texte (15-20 Sätze). Nuancierte Ausdrücke. "
           "VERWENDEN Sie: komplexe Hypotaxen, gehobener Wortschatz, "
           "Passiversatzformen, Funktionsverbgefüge, implizite Argumentation."),
    "C2": ("Muttersprachliches Niveau, alle Aspekte der Sprache. "
           "Lange Texte (20+ Sätze). Idiomatisch und differenziert. "
           "VERWENDEN Sie: idiomatische Wendungen, rhetorische Figuren, "
           "subtile Ironie, alle stilistischen Register, komplexer Nominalstil."),
}


def build_prompt(difficulty: str, question_type: str, theme: str) -> str:
    """构建 LLM 请求 prompt"""
    cefr_desc = CEFR_GUIDE.get(difficulty, CEFR_GUIDE["A1"])
    q_type_desc = QUESTION_TYPE_MAP.get(question_type, QUESTION_TYPE_MAP["选择题"])

    return f"""Erstelle eine Hörverständnisübung mit folgenden Parametern:

- CEFR-Niveau: {difficulty} (DIESES NIVEAU MUSS STRENG EINGEHALTEN WERDEN)
- Fragentyp: {q_type_desc}
- Thema: {theme}

Anforderungen:
1. Erstelle einen deutschen Hörtext (Dialog oder Monolog) der GENAU dem Niveau {difficulty} entspricht.
2. Das Thema ist: {theme}
3. Erstelle genau 5 Fragen im Format: {q_type_desc}
4. Gib zu jeder Frage die richtige Antwort an.
5. Wenn es ein Dialog ist, markiere jeden Sprecher klar.

KRITISCHE NIVEAU-VORGABEN für {difficulty}:
{cefr_desc}

WICHTIG: Der Text MUSS das Niveau {difficulty} widerspiegeln. Ein Text für B1 muss deutlich schwieriger sein als A2, mit Nebensätzen, verschiedenen Zeitformen und anspruchsvollerem Wortschatz. Ein A1-Text darf nur einfache Sätze im Präsens enthalten.

Gib NUR gültiges JSON zurück (keine Markdown-Formatierung, keine Erklärungen) mit dieser Struktur:
{{
  "title": "Titel auf Deutsch",
  "description": "Kurze Beschreibung auf Deutsch",
  "text_type": "dialogue" oder "monologue",
  "speakers": [{{"name": "Name", "gender": "female" oder "male"}}],
  "text_segments": [{{"speaker": "Name", "text": "Deutscher Text"}}],
  "questions": [
    {{
      "id": 1,
      "type": "multiple_choice" oder "fill_blank" oder "open_ended",
      "question": "Frage auf Deutsch",
      "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
      "answer": "Antwort"
    }}
  ]
}}

Wichtig:
- Bei Multiple-Choice: 4 Optionen (A-D), answer ist der Buchstabe (z.B. "A")
- Bei Lückentext: question enthält "___" für die Lücke, answer ist das fehlende Wort
- Bei offenen Fragen: answer ist eine Musterantwort
- Alle Texte auf Deutsch
- Der Hörtext soll natürlich und authentisch klingen"""


async def generate_content(
    difficulty: str,
    question_type: str,
    theme: str,
) -> dict:
    """
    生成德语听力内容。

    Returns:
        {
            "success": bool,
            "data": {...} | None,
            "source": "llm" | "demo",
            "error": str | None
        }
    """
    # 如果没有 API Key，使用 Demo 内容
    if not LLM_API_KEY or LLM_API_KEY == "your-api-key-here":
        demo = get_demo_content(difficulty, question_type, theme)
        if demo:
            return {"success": True, "data": demo, "source": "demo", "error": None}
        return {
            "success": False,
            "data": None,
            "source": "demo",
            "error": "未配置 LLM API Key，且没有匹配的 Demo 内容。请在 .env 文件中配置 LLM_API_KEY。",
        }

    # 调用 LLM API
    prompt = build_prompt(difficulty, question_type, theme)

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(
                f"{LLM_API_BASE}/chat/completions",
                headers={
                    "Authorization": f"Bearer {LLM_API_KEY}",
                    "Content-Type": "application/json",
                },
                json={
                    "model": LLM_MODEL,
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": prompt},
                    ],
                    "temperature": 0.8,
                    "max_tokens": 4096,
                },
            )
            response.raise_for_status()

        result = response.json()
        content = result["choices"][0]["message"]["content"]

        # 清理可能的 markdown 代码块标记
        content = content.strip()
        if content.startswith("```"):
            # 移除 ```json 或 ``` 标记
            lines = content.split("\n")
            content = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])

        data = json.loads(content)

        # 验证必要字段
        required = ["title", "text_segments", "questions"]
        for field in required:
            if field not in data:
                return {"success": False, "data": None, "source": "llm",
                        "error": f"LLM 返回数据缺少字段: {field}"}

        # 确保有 speakers 字段
        if "speakers" not in data or not data["speakers"]:
            speakers = set()
            for seg in data.get("text_segments", []):
                sp = seg.get("speaker", "")
                if sp:
                    speakers.add(sp)
            data["speakers"] = [
                {"name": s, "gender": random.choice(["female", "male"])}
                for s in sorted(speakers)
            ]
            if not data["speakers"]:
                data["speakers"] = [{"name": "Sprecher", "gender": "female"}]

        return {"success": True, "data": data, "source": "llm", "error": None}

    except httpx.HTTPStatusError as e:
        return {"success": False, "data": None, "source": "llm",
                "error": f"LLM API 返回错误 {e.response.status_code}: {e.response.text[:200]}"}
    except json.JSONDecodeError:
        return {"success": False, "data": None, "source": "llm",
                "error": "LLM 返回的内容无法解析为 JSON"}
    except Exception as e:
        return {"success": False, "data": None, "source": "llm",
                "error": f"LLM 请求失败: {str(e)}"}
