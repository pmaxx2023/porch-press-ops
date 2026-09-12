@echo off
REM PP-ELEANOR-AU-001A — one-click local FIXTURE preview (unpublished).
REM Opens http://127.0.0.1:8765/ — no Pages, no live storefront.
setlocal
cd /d "%~dp0"
set PORT=8765
set URL=http://127.0.0.1:%PORT%/
where python >nul 2>&1
if errorlevel 1 (
  where py >nul 2>&1
  if errorlevel 1 (
    echo python is required.
    exit /b 1
  )
  set PY=py -3
) else (
  set PY=python
)
echo FIXTURE preview — NOT live game content
echo Serving %CD%
echo Hub:    %URL%
echo Portal: %URL%portal/
echo Stop with Ctrl-C
start "" "%URL%"
%PY% -m http.server %PORT%
