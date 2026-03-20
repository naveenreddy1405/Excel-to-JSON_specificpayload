@echo off
REM Excel to JSON Converter - Quick Batch Script for Windows
REM Drag and drop Excel file onto this script to convert

if "%~1"=="" (
    echo.
    echo Excel to JSON Converter
    echo =======================
    echo.
    echo Usage: Drag and drop your Excel file onto this script
    echo Example: run.bat input.xlsx
    echo.
    echo Or run from command line:
    echo   run.bat input.xlsx
    echo   run.bat input.xlsx output.json
    echo.
    pause
    exit /b 1
)

setlocal enabledelayedexpansion

REM First check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

REM Check if dependencies are installed
python -c "import pandas" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Installing required dependencies (pandas, openpyxl)...
    echo This will only happen once.
    echo.
    pip install -r CLI_requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install dependencies
        echo Please ensure you have internet connection and Python is properly installed
        echo.
        pause
        exit /b 1
    )
)

REM Run the converter
python excel_to_json_converter.py %*

if errorlevel 1 (
    echo.
    echo Conversion failed. See error message above.
    echo.
    pause
    exit /b 1
)

echo.
echo Success! Check for your output JSON file.
echo.
pause
