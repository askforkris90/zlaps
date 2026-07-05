@echo off
REM ZLAPS Desktop Application Launcher Batch Script
REM This script sets up and launches the ZLAPS desktop GUI on Windows

setlocal enabledelayedexpansion

color 0B
cls

echo ================================
echo 🌊 ZLAPS Desktop Application 🌊
echo ================================
echo.

REM Check if Python is installed
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    color 0C
    echo ❌ Error: Python is not installed
    echo.
    echo Please install Python 3.7 or higher from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version 2^>^&1') do set PYTHON_VERSION=%%i
color 0A
echo ✓ Python found: %PYTHON_VERSION%
color 0B
echo.

REM Check if we're in the zlaps directory
if not exist "communication_core.py" (
    color 0C
    echo ❌ Error: Not in zlaps directory
    color 0B
    echo.
    echo Please navigate to the zlaps folder first:
    echo   cd zlaps
    echo   launch_desktop.bat
    echo.
    pause
    exit /b 1
)

color 0A
echo ✓ ZLAPS directory detected
color 0B
echo.

REM Upgrade pip
color 0E
echo 📦 Upgrading pip...
python -m pip install --upgrade pip --quiet 2>nul

REM Install required packages
echo 📦 Installing required packages...
echo    - numpy
python -m pip install numpy --quiet 2>nul
echo    - pillow
python -m pip install pillow --quiet 2>nul

color 0A
echo ✓ Dependencies installed successfully
color 0B
echo.

REM Generate logo if it doesn't exist
if not exist "zlaps_logo.png" (
    color 0E
    echo 🎨 Generating logo...
    python generate_logo.py >nul 2>&1
    color 0B
    echo.
)

REM Launch the desktop app
color 0A
echo 🚀 Launching ZLAPS Desktop Application...
echo ✓ Opening window on your desktop...
color 0B
echo.
echo Waiting for application to start...
echo.

REM Run the desktop application
python zlaps_desktop.py

echo.
color 0E
echo ❌ Application closed
color 0B
echo.
pause
