# Excel to JSON Converter - Windows Setup

**For Windows Users Only**

---

## **Step 1: Install Python (If Needed)**

### Check if Python is already installed:
```
Press: Windows Key + R
Type: cmd
Press: Enter

In Command Prompt, type:
python --version
```

### If you see a version number (e.g., "Python 3.9.0"), skip to Step 2

### If "python not found" error:

1. Download Python: https://www.python.org/downloads/
2. **IMPORTANT:** During installation, CHECK the box:
   ```
   ☑ Add Python to PATH
   ```
3. Click "Install Now"
4. Restart your computer
5. Verify in Command Prompt: `python --version`

---

## **Step 2: First Time Setup**

1. Open Command Prompt (Cmd)
2. Navigate to this folder:
   ```
   cd "C:\path\to\Excel_to_JSON_Tool\Windows"
   ```
3. Run: `run.bat` (or double-click it)
4. It will auto-install dependencies on first run

---

## **Step 3: Convert Your Excel File**

### **Method 1: Drag & Drop (Easiest)**
1. Double-click `run.bat`
2. Drag your Excel file onto the Command Prompt window
3. Press Enter
4. Your JSON file will be created in the same folder

### **Method 2: Command Line**

In Command Prompt:
```
cd "C:\path\to\Excel_to_JSON_Tool\Windows"

# Basic usage
run.bat input.xlsx

# With custom output name
run.bat input.xlsx my_output.json
```

---

## **Your Excel File Format**

### **Required: At least ONE of these columns**
- `objectId` - Product/Transaction ID
- `object_id` - Legacy naming
- `userId` - User ID

### **Optional Columns**
- `objectType` - Type of object
- `method` - HTTP method (POST, GET, etc.)
- `path` - API endpoint
- `value` - Data value
- `metaFields.*` - Metadata fields

### **Example Excel:**

```
| objectId | objectType | method | path     | value | metaFields.dept |
|----------|------------|--------|----------|-------|-----------------|
| OBJ001   | Report     | POST   | /update  | 100   | Finance         |
| OBJ002   | Report     | GET    | /status  | 200   | IT              |
```

---

## **Output**

You'll get a JSON file:

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
        "dept": "Finance"
      }
    }
  ]
}
```

---

## **Troubleshooting**

### ❌ "python is not recognized"
- **Solution:** Reinstall Python with "Add Python to PATH" checked
- Restart Command Prompt after installation

### ❌ "ModuleNotFoundError: pandas"
- **Solution:** Run the script again, it will auto-install
- Or manually: `pip install pandas openpyxl`

### ❌ "File not found"
- **Solution:** Make sure Excel file is in the same folder OR use full path
- Example: `run.bat "C:\Users\YourName\Documents\input.xlsx"`

### ❌ "No valid ID found" (empty output)
- **Solution:** Add at least ONE of these columns to your Excel:
  - `objectId`
  - `object_id`
  - `userId`

### ❌ "input.xlsx is not an Excel file"
- **Solution:** Save your file as `.xlsx` (Excel format)
- Not `.csv` or `.txt`

---

## **Advanced Usage**

### **Pretty-print JSON (readable format)**
```
python excel_to_json_converter.py input.xlsx output.json --pretty
```

### **Verbose output (see what's happening)**
```
python excel_to_json_converter.py input.xlsx output.json -v
```

### **Both options**
```
python excel_to_json_converter.py input.xlsx output.json -v --pretty
```

---

## **Files in This Folder**

- `run.bat` - Quick launcher (double-click this!)
- `excel_to_json_converter.py` - Main converter script
- `CLI_requirements.txt` - Dependencies list
- `README_WINDOWS.md` - This file

---

## **Need More Help?**

1. See `QUICK_START.md` for basic instructions
2. See `INSTALLATION_GUIDE.md` in Documentation folder
3. See `TROUBLESHOOTING.md` for common issues
4. See `Examples/` folder for sample files

---

**You're all set! Happy converting!** 🎉
