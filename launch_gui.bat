@echo off
setlocal
cd /d "%~dp0"
set "PYTHONPATH=%~dp0src"
where python >nul 2>nul
if %errorlevel%==0 (
  python -m pixel_art_skill_toolkit gui %*
) else (
  py -3 -m pixel_art_skill_toolkit gui %*
)
if errorlevel 1 pause
