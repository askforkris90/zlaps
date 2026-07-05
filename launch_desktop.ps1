# ZLAPS Desktop Application Launcher for PowerShell
# This script sets up and launches the ZLAPS desktop GUI on Windows

Write-Host "================================" -ForegroundColor Cyan
Write-Host "🌊 ZLAPS Desktop Application 🌊" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
$pythonCheck = python --version 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Error: Python is not installed" -ForegroundColor Red
    Write-Host "Please install Python 3.7 or higher from https://www.python.org/" -ForegroundColor Red
    Write-Host "Make sure to check 'Add Python to PATH' during installation" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✓ Python found: $pythonCheck" -ForegroundColor Green
Write-Host ""

# Check if we're in the zlaps directory
if (-Not (Test-Path "communication_core.py")) {
    Write-Host "❌ Error: Not in zlaps directory" -ForegroundColor Red
    Write-Host "Please run this script from the zlaps folder:" -ForegroundColor Yellow
    Write-Host "  cd zlaps" -ForegroundColor White
    Write-Host "  .\launch_desktop.ps1" -ForegroundColor White
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host "✓ ZLAPS directory detected" -ForegroundColor Green
Write-Host ""

# Upgrade pip
Write-Host "📦 Upgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip --quiet
if ($LASTEXITCODE -ne 0) {
    Write-Host "⚠️  Warning: pip upgrade had issues, continuing anyway..." -ForegroundColor Yellow
}

# Install required packages
Write-Host "📦 Installing required packages..." -ForegroundColor Yellow
Write-Host "   - numpy" -ForegroundColor Gray
python -m pip install numpy --quiet
Write-Host "   - pillow" -ForegroundColor Gray
python -m pip install pillow --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "✓ Dependencies installed successfully" -ForegroundColor Green
} else {
    Write-Host "❌ Error installing dependencies" -ForegroundColor Red
    Read-Host "Press Enter to exit"
    exit 1
}
Write-Host ""

# Generate logo if it doesn't exist
if (-Not (Test-Path "zlaps_logo.png")) {
    Write-Host "🎨 Generating logo..." -ForegroundColor Yellow
    python generate_logo.py
    Write-Host ""
}

# Launch the desktop app
Write-Host "🚀 Launching ZLAPS Desktop Application..." -ForegroundColor Green
Write-Host "✓ Opening window on your desktop..." -ForegroundColor Green
Write-Host ""
Write-Host "Waiting for application to start..." -ForegroundColor Gray
Write-Host ""

# Run the desktop application
python zlaps_desktop.py

Write-Host ""
Write-Host "❌ Application closed" -ForegroundColor Yellow
Read-Host "Press Enter to exit"
