#!/bin/bash
# Excel to JSON Converter - Quick Shell Script for Mac/Linux
# Drag and drop Excel file onto this script to convert

if [ $# -eq 0 ]; then
    cat << 'EOF'

Excel to JSON Converter
=======================

Usage: ./run.sh input.xlsx
       ./run.sh input.xlsx output.json

Or drag and drop your Excel file onto this script.

EOF
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo ""
    echo "ERROR: Python3 is not installed"
    echo ""
    echo "Install Python using:"
    echo "  macOS: brew install python3"
    echo "  Linux: sudo apt-get install python3"
    echo ""
    exit 1
fi

# Check if dependencies are installed
python3 -c "import pandas" 2>/dev/null
if [ $? -ne 0 ]; then
    echo ""
    echo "Installing required dependencies (pandas, openpyxl)..."
    echo "This will only happen once."
    echo ""
    pip3 install -r CLI_requirements.txt
    if [ $? -ne 0 ]; then
        echo ""
        echo "ERROR: Failed to install dependencies"
        echo "Please ensure you have internet connection and Python3 is properly installed"
        echo ""
        exit 1
    fi
fi

# Run the converter
python3 excel_to_json_converter.py "$@"

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Check for your output JSON file."
    echo ""
else
    echo ""
    echo "❌ Conversion failed. See error message above."
    echo ""
    exit 1
fi
