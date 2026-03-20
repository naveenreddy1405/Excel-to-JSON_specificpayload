# Quick Start Guide - 5 Minutes

**Choose your operating system:**

---

## **For Windows Users**

### **Setup (First Time Only - 2 Minutes)**

1. Make sure Python is installed
   - Type `python --version` in Command Prompt
   - If not installed: Download from https://www.python.org/downloads/
   - Check "Add Python to PATH" during installation

2. That's it! You're ready to use the tool

### **Usage (Every Time - 1 Minute)**

**Option A: Drag & Drop (Easiest)**
```
1. Double-click run.bat
2. Drag your Excel file onto the window
3. Press Enter
4. Look for your_file_output.json in the same folder
```

**Option B: Command Line**
```
run.bat input.xlsx
run.bat input.xlsx custom_output.json
```

---

## **For Mac/Linux Users**

### **Setup (First Time Only - 2 Minutes)**

1. Check if Python is installed:
   ```bash
   python3 --version
   ```

2. If not installed:
   - Mac: `brew install python3`
   - Linux: `sudo apt-get install python3`

3. Make the script executable (one-time):
   ```bash
   chmod +x run.sh
   ```

### **Usage (Every Time - 1 Minute)**

```bash
# Basic usage
./run.sh input.xlsx

# With custom output filename
./run.sh input.xlsx output.json

# Verbose mode (see details)
./run.sh input.xlsx output.json -v
```

---

## **Your Excel File**

### **Required:**
At least ONE of these columns:
- `objectId`
- `object_id`
- `userId`

### **Example:**

| objectId | objectType | method | path      | value |
|----------|------------|--------|-----------|-------|
| OBJ001   | Report     | POST   | /update   | 100   |
| OBJ002   | Report     | GET    | /status   | 200   |

---

## **Output**

You'll get a JSON file like:

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
      "requestId": "OBJ001"
    }
  ]
}
```

---

## **That's it! 🎉**

You're all set to convert Excel files to JSON!

For detailed help, see `INSTALLATION_GUIDE.md` in the Documentation folder.
