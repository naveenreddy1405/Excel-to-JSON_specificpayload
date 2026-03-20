# Excel to JSON Converter - CLI Tool

A standalone command-line tool to convert Excel files to JSON batch request format. **No Django required. No server needed. Works offline.**

## Installation

### Step 1: Install Python Dependencies

```bash
pip install -r CLI_requirements.txt
```

This installs:
- `pandas` - for Excel file reading
- `openpyxl` - for .xlsx file support

### Step 2: Verify Installation

```bash
python excel_to_json_converter.py --help
```

## Usage

### Basic Usage

Convert Excel file to JSON:

```bash
python excel_to_json_converter.py input.xlsx output.json
```

### Auto-generate Output Filename

If you don't specify output file, it creates `input_output.json`:

```bash
python excel_to_json_converter.py input.xlsx
# Creates: input_output.json
```

### Verbose Mode

See detailed processing information:

```bash
python excel_to_json_converter.py input.xlsx output.json -v
```

### Pretty-Print JSON

Format JSON output for readability:

```bash
python excel_to_json_converter.py input.xlsx output.json --pretty
```

## Excel File Format

### Column Types

Your Excel file can use **two formats for metadata fields**:

#### Format 1: Old Style - Column Name with Prefix

```
| objectId | objectType | metaFields.color | metaFields.size |
|----------|------------|------------------|-----------------|
| 123      | Product    | Red              | Large           |
```

#### Format 2: New Style - Marker Column with Inline Fields

```
| objectId | objectType | metaFields | color | size |
|----------|------------|------------|-------|------|
| 123      | Product    | marker     | Red   | Large|
```

Both formats work and can be mixed!

### Required Columns

At least one ID column (required):
- `objectId` - For transaction/product objects
- `object_id` - Legacy naming (converts to objectId)
- `userId` - For user-based operations

### Special Columns

- `requestId` - Unique request identifier (auto-generated if missing)
- `metaFields.*` - Custom metadata fields (old format)
- Column after `metaFields` marker - Custom metadata (new format)

### Example Excel Structure

```
| objectId | objectType | method | path     | value | metaFields.department | metaFields.team |
|----------|------------|--------|----------|-------|----------------------|-----------------|
| OBJ001   | Report     | POST   | /update  | 100   | Finance              | Accounting      |
| OBJ002   | Report     | GET    | /status  | 200   | IT                   | Infrastructure  |
```

## Output Format

Your JSON file will contain a batch request:

```json
{
  "batch_request_id": "update test1",
  "batch_update_url": "https://client-api-domain.com/batch_status_update/",
  "requests": [
    {
      "objectId": "OBJ001",
      "objectType": "Report",
      "method": "POST",
      "path": "/update",
      "value": "100",
      "requestId": "OBJ001",
      "metaFields": {
        "department": "Finance",
        "team": "Accounting"
      }
    },
    {
      "objectId": "OBJ002",
      "objectType": "Report",
      "method": "GET",
      "path": "/status",
      "value": "200",
      "requestId": "OBJ002",
      "metaFields": {
        "department": "IT",
        "team": "Infrastructure"
      }
    }
  ]
}
```

## Features

✅ **Standalone** - No web server required  
✅ **Offline** - Works without internet  
✅ **Supports Both Metafield Formats** - Old and new naming styles  
✅ **Duplicate Handling** - Automatically deduplicates metafields  
✅ **Date Formatting** - Converts dates to YYYY-MM-DD  
✅ **Logging** - Detailed processing information  
✅ **Error Handling** - Clear error messages  

## Troubleshooting

### "ModuleNotFoundError: No module named 'pandas'"

Install dependencies:
```bash
pip install -r CLI_requirements.txt
```

### "Input file not found: input.xlsx"

Make sure the file exists and path is correct:
```bash
python excel_to_json_converter.py /full/path/to/input.xlsx
```

### "No valid ID found" - Rows are skipped

Ensure your Excel has at least one `objectId`, `object_id`, or `userId` column.

### Empty output JSON

Check if:
1. Excel file has data rows
2. At least one ID column exists
3. Run with `-v` flag to see detailed logs

## Command Reference

```
usage: excel_to_json_converter.py [-h] [-v] [-p] input_file [output_file]

positional arguments:
  input_file            Input Excel file path
  output_file           Output JSON file path (default: input_output.json)

optional arguments:
  -h, --help           show this help message and exit
  -v, --verbose        Enable verbose logging
  -p, --pretty         Pretty print JSON (default: compact)
```

## Quick Start

1. **Install**
   ```bash
   pip install -r CLI_requirements.txt
   ```

2. **Convert**
   ```bash
   python excel_to_json_converter.py your_file.xlsx
   ```

3. **Check Output**
   ```bash
   # Look for your_file_output.json
   ```

That's it! 🎉

## Distribution to Team

### For Windows Users
1. Download `excel_to_json_converter.py` and `CLI_requirements.txt`
2. Run: `pip install -r CLI_requirements.txt`
3. Convert: `python excel_to_json_converter.py input.xlsx`

### For Mac/Linux Users
Same steps as Windows.

### For Non-Technical Users
Share the `.py` file and `requirements.txt`, with a pre-made batch script or alias:

**Windows batch file (run.bat):**
```batch
@echo off
python %~dp0\excel_to_json_converter.py %1
pause
```

**Mac/Linux shell script (run.sh):**
```bash
#!/bin/bash
python "$(dirname "$0")/excel_to_json_converter.py" "$1"
```

Make it executable: `chmod +x run.sh`

## Support

For issues or questions, check:
1. Run with `-v` (verbose) flag for detailed logs
2. Ensure input Excel file is valid
3. Verify all required columns exist

## License

Same as main project

---

**No cloud upload. No internet required. Fully offline.** ✅
