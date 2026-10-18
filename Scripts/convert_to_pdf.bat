@echo off
setlocal

if "%~1"=="" (
    echo Usage: %~nx0 path\to\file.md [output.pdf]
    echo You can also drag and drop a .md file directly onto this .bat file.
    pause
    exit /b 1
)

set SCRIPT_DIR=%~dp0
set VENV_PYTHON=%SCRIPT_DIR%..\.venv\Scripts\python.exe

if not exist "%VENV_PYTHON%" (
    echo [ERROR] Virtual environment python not found at %VENV_PYTHON%
    echo Please make sure .venv is installed in the project root.
    pause
    exit /b 1
)

"%VENV_PYTHON%" "%SCRIPT_DIR%md_to_pdf.py" "%~1" %2
if %ERRORLEVEL% equ 0 (
    echo.
    echo [SUCCESS] PDF conversion completed!
) else (
    echo.
    echo [ERROR] PDF conversion failed.
)

if "%~2"=="" (
    timeout /t 3 >nul
)
