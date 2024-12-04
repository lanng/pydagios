@echo off
:: Check if the script is running with admin privileges
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

:: Change to the directory where the batch file is located
cd /d "%~dp0"

:: Open PowerShell and activate the virtual environment
powershell -NoExit -Command "& {Set-Location '%cd%'; . .\venv\Scripts\Activate.ps1}"
