@echo off
REM Excel to JSON Converter - Windows Simple Launcher
REM User-friendly wrapper that shows instructions and accepts files

setlocal enabledelayedexpansion

echo.
echo ================================================
echo    Excel to JSON Converter - Windows
echo ================================================
echo.
echo WHAT TO DO:
echo.
echo 1. Find your Excel file (.xlsx)
echo 2. Drag and drop it onto this window
echo 3. Press ENTER
echo 4. Your JSON file will be created!
echo.
echo ================================================
echo.

set /p input_file="Drag your Excel file here (then press ENTER): "

REM Trim quotes if present
set input_file=!input_file:"=!

REM Check if file was provided
if "!input_file!"=="" (
    echo.
    echo Error: No file provided.
    pause
    exit /b 1
)

REM Check if file exists
if not exist "!input_file!" (
    echo.
    echo Error: File not found: !input_file!
    pause
    exit /b 1
)

echo.
echo Converting... Please wait...
echo.

REM Run converter (same directory)
ExcelToJsonConverter.exe "!input_file!"

if %errorlevel% equ 0 (
    echo.
    echo Success! Your JSON file has been created!
    echo.
    echo Look in the same folder as your Excel file
    echo.
    pause
) else (
    echo.
    echo Error: Conversion failed.
    pause
    exit /b 1
)
