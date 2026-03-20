# HOW TO BUILD WINDOWS .EXE

**For Windows users or Windows developers**

---

## **Prerequisites**

- Windows 10/11 or Windows Server
- Python 3.9 or higher installed
- Internet connection (for first setup)

---

## **Step 1: Download Source Files**

Download the repository from GitHub (or clone it)

---

## **Step 2: Install Dependencies**

Open Command Prompt in the project folder and run:

```cmd
pip install -r CLI_requirements.txt
pip install pyinstaller
```

---

## **Step 3: Build the EXE**

Run this command:

```cmd
pyinstaller --onefile --console excel_to_json_converter.py
```

---

## **Step 4: Find Your EXE**

The executable will be in: `dist\ExcelToJsonConverter.exe`

**File size:** ~15-20 MB (normal)

---

## **Step 5: Test It**

Double-click `ExcelToJsonConverter.exe` or run:

```cmd
ExcelToJsonConverter.exe input.xlsx output.json
```

---

## **Step 6: Distribute**

Share `ExcelToJsonConverter.exe` with your team!

They just need to run it - NO Python required on their machines.

---

## **Alternative: Quick Build Script**

Create `build.bat` with this content:

```batch
@echo off
echo Installing dependencies...
pip install -r CLI_requirements.txt
pip install pyinstaller

echo Building executable...
pyinstaller --onefile --console excel_to_json_converter.py

echo.
echo Build complete!
echo Find ExcelToJsonConverter.exe in the dist folder
echo.
pause
```

Then just double-click `build.bat`

---

## **Troubleshooting**

### **"pip is not recognized"**
→ Python not in PATH. Reinstall Python with "Add Python to PATH" checked.

### **"pyinstaller not found"**
→ Run: `pip install pyinstaller`

### **Build takes a long time**
→ Normal. It's bundling Python + libraries. Wait ~2-5 minutes.

### **EXE doesn't work**
→ Make sure pandas and openpyxl are installed:
```cmd
pip install pandas openpyxl
```

---

## **Result**

You'll have a standalone EXE that:
- ✅ Needs NO Python installation
- ✅ Works on any Windows 10/11 machine
- ✅ All dependencies bundled
- ✅ Perfect for distribution

---

**Questions?** See STANDALONE_EXECUTABLES.md for more info.
