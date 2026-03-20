# MAC EXECUTABLE - Quick Start Guide

**NO Python Installation Needed. Just Download and Run!**

---

## **📥 Step 1: Download**

Download `ExcelToJsonConverter` from the GitHub releases or shared folder.

**File size:** 16.6 MB (normal for bundled app)

---

## **🚀 Step 2: Prepare for First Use**

Since it's from the internet, Mac may warn you. Fix this:

1. Open Terminal
2. Run:
   ```bash
   chmod +x /path/to/ExcelToJsonConverter
   ```
   (Replace `/path/to/` with actual location)

3. Or right-click the file → "Open"
4. Click "Open" button at security warning

---

## **🚀 Step 3: Run the App**

### **Option A: Double-Click**

1. Double-click `ExcelToJsonConverter`
2. Terminal opens
3. Drag your Excel file onto it
4. Press Enter
5. ✅ Your JSON file appears!

### **Option B: Terminal Command**

```bash
./ExcelToJsonConverter input.xlsx
./ExcelToJsonConverter input.xlsx output.json
./ExcelToJsonConverter input.xlsx output.json -v --pretty
```

### **Option C: From Anywhere**

Add to PATH for global use:

```bash
# One-time setup
sudo cp ExcelToJsonConverter /usr/local/bin/

# Then use from anywhere:
ExcelToJsonConverter input.xlsx
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

### **"ExcelToJsonConverter cannot be opened"**
→ Run: `chmod +x /path/to/ExcelToJsonConverter`
→ Then double-click again

### **"File not found"**
→ Make sure Excel file is in same folder or use full path

### **"No valid ID found"**
→ Add objectId, object_id, or userId column

### **Permission denied**
→ Run: `chmod +x ExcelToJsonConverter`

---

## **✨ Key Points**

✅ NO Python required  
✅ NO setup needed  
✅ NO internet needed  
✅ Works completely offline  
✅ Safe for company use  

---

## **🎯 That's It!**

Download, make executable, run. Done! 🎉
