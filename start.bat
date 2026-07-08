@echo off
chcp 65001 >nul 2>&1
set PYTHONIOENCODING=utf-8
set PYTHONUTF8=1
title Deutsches Hoerverstaendnis Generator
echo ==================================================
echo   Deutsches Hoerverstaendnis Generator
echo   http://localhost:8765
echo ==================================================
echo.

cd /d "%~dp0"

set PYTHON=C:\Users\18767\.workbuddy\binaries\python\envs\german-tts\Scripts\python.exe

echo [Starting server...]
"%PYTHON%" -m backend.main

pause
