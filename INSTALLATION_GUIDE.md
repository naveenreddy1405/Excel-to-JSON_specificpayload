# Excel to JSON Converter - Installation & Usage Guide

**Share this document with your team**

---

## **For Everyone - 30 Second Setup**

### Step 1: Get the Tool
Go to: https://github.com/naveenreddy1405/Excel-to-JSON_specificpayload

Click **Code** → **Download ZIP** → Extract

### Step 2: Install Python (One-Time Only)

**If you don't have Python:**

- **Windows:** Download from https://www.python.org/downloads/
  - ✅ Check "Add Python to PATH"
  - Click Install
  
- **Mac:** 
  - Already have Python 3? Skip to Step 3
  - Otherwise: `brew install python3`
  
- **Linux:** 
  - `sudo apt-get install python3`

### Step 3: Run the Tool

#### **Windows:**
- Double-click `run.bat`
- It will auto-install dependencies (first time only)
- Drag & drop your Excel file
- ✅ Get JSON output!

#### **Mac/Linux:**
- Open Terminal in the tool folder
- Run: `chmod +x run.sh` (one-time)
- Run: `./run.sh input.xlsx`
- ✅ Get JSON output!

---

## **Usage Examples**

### **Windows Users:**

**Option 1: Double-Click (Easiest)**
```
1. Double-click run.bat
2. Drag Excel file onto it
3. Press Enter
```

**Option 2: Command Line**
```
run.bat input.xlsx
run.bat input.xlsx custom_output.json
```

### **Mac/Linux Users:**

**Command Line**
```bash
./run.sh input.xlsx
./run.sh input.xlsx custom_output.json
./run.sh input.xlsx output.json -v  # Verbose output
```

### **Advanced Users:**

```bash
# Pretty-print JSON
python excel_to_json_converter.py input.xlsx output.json --pretty

# Verbose logging
python excel_to_json_converter.py input.xlsx output.json -v

# Both
python excel_to_json_converter.py input.xlsx output.json -v --pretty
```

---

## **Your Excel File Format**

Your Excel file needs:

### **Required Columns (At least ONE):**
- `objectId` - For products/transactions
- `object_id` - Legacy naming
- `userId` - For user operations

### **Optional Columns:**
- `objectType` - Type of object (defaults to "Transaction")
- `method` - HTTP method (POST, GET, etc.)
- `path` - API path
- `value` - Data value
- `requestId` - Unique request ID (auto-generated if missing)
- `metaFields.*` - Custom metadata (old style)
- `metaFields` marker with columns - Custom metadata (new style)

### **Example Excel Layout:**

| objectId | objectType | method | path      | value | metaFields.dept | metaFields.team |
|----------|------------|--------|-----------|-------|-----------------|-----------------|
| OBJ001   | Report     | POST   | /update   | 100   | Finance         | Accounting      |
| OBJ002   | Report     | GET    | /status   | 200   | IT              | Infrastructure  |

---

## **Troubleshooting**

### ❌ "Python not found"
**Solution:** Install Python and check "Add Python to PATH"

### ❌ "ModuleNotFoundError: pandas"
**Solution:** 
- Windows: `pip install pandas openpyxl`
- Mac/Linux: `pip3 install pandas openpyxl`

### ❌ "Input file not found"
**Solution:** Make sure:
1. Excel file is in the same folder as the tool
2. Or use full path: `run.bat C:\Users\Name\Desktop\input.xlsx`

### ❌ "Empty JSON output"
**Solution:** Verify your Excel has:
- At least ONE ID column (objectId, object_id, or userId)
- Data rows below headers

### ❌ "No valid ID found" error
**Solution:** Add at least ONE of these columns to your Excel:
- `objectId`
- `object_id`
- `userId`

---

## **Output Format**

Your JSON file will look like:

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
        "dept": "Finance",
        "team": "Accounting"
      }
    }
  ]
}
```

---

## **Features**

✅ Works completely offline (no internet needed)  
✅ No server required (runs on your computer)  
✅ No cloud upload (all files stay local)  
✅ Windows, Mac, and Linux support  
✅ Auto-installs dependencies  
✅ Supports both old and new metadata formats  
✅ Automatic date formatting  
✅ Detailed error messages  

---

## **Need Help?**

1. **Check if Python is installed:** `python --version`
2. **Verify Excel file format:** Does it have objectId/object_id/userId column?
3. **Run with verbose mode:** `./run.sh input.xlsx -v`
4. **Check the README:** See CLI_README.md for detailed documentation

---

## **Files Included**

- `excel_to_json_converter.py` - Main converter script
- `run.bat` - Quick launcher for Windows
- `run.sh` - Quick launcher for Mac/Linux
- `CLI_requirements.txt` - Dependencies
- `CLI_README.md` - Full documentation

---

**Questions?** Contact your IT department or the tool creator.

**Last Updated:** March 2026
