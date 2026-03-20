# WINDOWS EXE - Quick Start Guide

**NO Python Installation Needed. Just Download and Run!**

---

## **📥 Step 1: Download**

Download `ExcelToJsonConverter.exe` from the GitHub releases or shared folder.

**File size:** ~15-20 MB (normal for bundled app)

---

## **🚀 Step 2: Run the App**

### **Option A: Double-Click (Easiest)**

1. Right-click `ExcelToJsonConverter.exe`
2. Click "Open"
3. Click "Open" again (security warning - this is normal)
4. Command Prompt window opens
5. Drag your Excel file onto the window
6. Press Enter
7. ✅ Your JSON file appears!

### **Option B: Command Line**

Open Command Prompt where the `.exe` file is located:

```cmd
ExcelToJsonConverter.exe input.xlsx
ExcelToJsonConverter.exe input.xlsx output.json
ExcelToJsonConverter.exe input.xlsx output.json -v --pretty
```

---

## **✅ Your Excel File**

**Needs at least ONE of:**

| Column Name | Purpose |
|------------|---------|
| `objectId` | Product/Transaction ID |
| `object_id` | Legacy naming |
| `userId` | User ID |

**Example:**

| objectId | method | path     | value |
|----------|--------|----------|-------|
| OBJ001   | POST   | /update  | 100   |
| OBJ002   | GET    | /status  | 200   |

---

## **📤 Your Output**

JSON file with requests array:

```json
{
  "batch_request_id": "update test1",
  "batch_update_url": "https://client-api-domain.com/batch_status_update/",
  "requests": [
    {
      "objectId": "OBJ001",
      "method": "POST",
      "path": "/update",
      "value": "100",
      "requestId": "OBJ001"
    }
  ]
}
```

---

## **❌ Troubleshooting**

### **"Windows protected your PC"**
→ This is normal. Click "More info" → "Run anyway"

### **"File not found"**
→ Make sure Excel file is in same folder or use full path

### **"No valid ID found"**
→ Add objectId, object_id, or userId column

---

## **✨ Key Points**

✅ NO Python required  
✅ NO setup needed  
✅ NO internet needed  
✅ Works completely offline  
✅ Safe for company use  

---

## **🎯 That's It!**

Just download, double-click, drag your file. Done! 🎉
