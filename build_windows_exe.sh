#!/bin/bash
# Script to build Windows .EXE on Mac/Linux
# This uses PyInstaller to create a standalone Windows executable

echo "==========================================="
echo "Creating Standalone Windows .EXE"
echo "==========================================="

# Check if PyInstaller is installed
python3 -m pip show pyinstaller > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing PyInstaller..."
    python3 -m pip install pyinstaller
fi

# Create Windows executable
python3 -m PyInstaller \
    --name=ExcelToJsonConverter \
    --onefile \
    --console \
    --target-arch=x86_64 \
    excel_to_json_converter.py

echo ""
echo "✅ Build complete!"
echo "📦 Check dist/ folder for ExcelToJsonConverter.exe"
echo ""
echo "Note: This creates a Windows .exe but must be run on Windows or with Wine"
