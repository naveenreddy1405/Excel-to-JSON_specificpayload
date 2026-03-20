# Excel to JSON Converter - Mac & Linux Setup

**For Mac and Linux Users**

---

## **Step 1: Install Python (If Needed)**

### Check if Python is already installed:
```bash
python3 --version
```

### If you see a version number (e.g., "Python 3.9.0"), skip to Step 2

### If "command not found":

**Mac (with Homebrew):**
```bash
brew install python3
```

**Mac (without Homebrew):**
```bash
# Install Homebrew first
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Then install Python
brew install python3
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install python3 python3-pip
```

**Linux (Fedora/RHEL):**
```bash
sudo dnf install python3 python3-pip
```

---

## **Step 2: First Time Setup**

1. Open Terminal
2. Navigate to the Mac_Linux folder:
   ```bash
   cd /path/to/Excel_to_JSON_Tool/Mac_Linux
   ```
3. Make the script executable (one-time):
   ```bash
   chmod +x run.sh
   ```
4. First run (auto-installs dependencies):
   ```bash
   ./run.sh
   ```

---

## **Step 3: Convert Your Excel File**

### **Basic Usage:**
```bash
cd /path/to/Excel_to_JSON_Tool/Mac_Linux

# Convert Excel file
./run.sh input.xlsx

# With custom output filename
./run.sh input.xlsx my_output.json
```

### **Verbose Mode (see details):**
```bash
./run.sh input.xlsx output.json -v
```

### **Pretty-print JSON (readable format):**
```bash
python3 excel_to_json_converter.py input.xlsx output.json --pretty
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

### ❌ "command not found: python3"
- **Solution:** Install Python (see Step 1)
- Verify: `python3 --version`

### ❌ "ModuleNotFoundError: pandas"
- **Solution:** Install manually:
  ```bash
  pip3 install pandas openpyxl
  ```
- Or run the script again, it will auto-install

### ❌ "Permission denied"
- **Solution:** Make script executable (one-time):
  ```bash
  chmod +x run.sh
  ```

### ❌ "File not found"
- **Solution:** Use full path to Excel file
  ```bash
  ./run.sh "/Users/YourName/Documents/input.xlsx"
  ```

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

### **Using Python directly:**
```bash
python3 excel_to_json_converter.py input.xlsx output.json
```

### **With all options:**
```bash
python3 excel_to_json_converter.py input.xlsx output.json -v --pretty
```

### **Check Python version:**
```bash
python3 --version
```

### **Create an alias for easy access:**
```bash
# Add to ~/.bashrc or ~/.zshrc
alias excel2json="python3 /path/to/excel_to_json_converter.py"

# Then use as:
excel2json input.xlsx output.json
```

---

## **Files in This Folder**

- `run.sh` - Quick launcher script (make executable with chmod +x)
- `excel_to_json_converter.py` - Main converter script
- `CLI_requirements.txt` - Dependencies list
- `README_MAC_LINUX.md` - This file

---

## **Need More Help?**

1. See `QUICK_START.md` for basic instructions
2. See `INSTALLATION_GUIDE.md` in Documentation folder
3. See `TROUBLESHOOTING.md` for common issues
4. See `Examples/` folder for sample files

---

**You're all set! Happy converting!** 🎉
