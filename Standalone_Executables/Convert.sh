#!/bin/bash

# Excel to JSON Converter - Mac Simple Launcher
# User-friendly wrapper that shows instructions and accepts drag-drop

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
CONVERTER="$SCRIPT_DIR/ExcelToJsonConverter_Mac"

# Check if converter exists
if [ ! -f "$CONVERTER" ]; then
    echo "❌ Error: ExcelToJsonConverter_Mac not found in this folder"
    echo "Make sure ExcelToJsonConverter_Mac is in the same folder as this script"
    sleep 5
    exit 1
fi

# Show instructions
clear
echo "════════════════════════════════════════════════════"
echo "      Excel to JSON Converter - Mac"
echo "════════════════════════════════════════════════════"
echo ""
echo "📥 WHAT TO DO:"
echo ""
echo "1. Go to Finder and find your Excel file"
echo "2. Drag your Excel file onto this Terminal window"
echo "3. Press ENTER"
echo "4. ✅ Your JSON file will be created!"
echo ""
echo "────────────────────────────────────────────────────"
echo ""
echo "💡 EXAMPLE:"
echo "   Drag your file here → [drop it now]"
echo ""
read -p "Waiting for your file... " input_file

# Trim whitespace
input_file=$(echo "$input_file" | xargs)

# Check if file was provided
if [ -z "$input_file" ]; then
    echo ""
    echo "❌ No file provided. Exiting."
    sleep 2
    exit 1
fi

# Check if file exists
if [ ! -f "$input_file" ]; then
    echo ""
    echo "❌ Error: File not found: $input_file"
    sleep 3
    exit 1
fi

# Check if it's an Excel file
if [[ ! "$input_file" =~ \.(xlsx|xls)$ ]]; then
    echo ""
    echo "⚠️  Warning: This doesn't look like an Excel file"
    echo "   File: $input_file"
    echo ""
    read -p "Continue anyway? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

echo ""
echo "🔄 Converting... Please wait..."
echo ""

# Run converter
"$CONVERTER" "$input_file"

# Check exit code
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Success! Your JSON file has been created!"
    echo ""
    echo "📁 Look in the same folder as your Excel file"
    echo ""
    sleep 3
else
    echo ""
    echo "❌ Conversion failed. Check the error above."
    sleep 3
fi
