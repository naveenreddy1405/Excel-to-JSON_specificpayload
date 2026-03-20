# Shared Folder Setup - Distribution Package

**For uploading to your company's shared drive (OneDrive, SharePoint, Network Drive, etc.)**

---

## **Step 1: Create Shared Folder Structure**

Create this folder structure on your company's shared drive:

```
📁 Excel_to_JSON_Tool/
   ├── 📄 README.md (START HERE)
   ├── 📄 QUICK_START.md (Simple instructions)
   ├── 📁 Windows/
   │   ├── run.bat
   │   ├── excel_to_json_converter.py
   │   ├── CLI_requirements.txt
   │   └── README_WINDOWS.md
   ├── 📁 Mac_Linux/
   │   ├── run.sh
   │   ├── excel_to_json_converter.py
   │   ├── CLI_requirements.txt
   │   └── README_MAC_LINUX.md
   ├── 📁 Examples/
   │   ├── sample_input.xlsx
   │   └── sample_output.json
   └── 📁 Documentation/
       ├── INSTALLATION_GUIDE.md
       ├── CLI_README.md
       └── TROUBLESHOOTING.md
```

---

## **Step 2: Files to Copy to Shared Drive**

Download these files from GitHub and copy to the shared drive:

### **From Root Directory:**
- `excel_to_json_converter.py` (copy to both Windows/ and Mac_Linux/ folders)
- `CLI_requirements.txt` (copy to both Windows/ and Mac_Linux/ folders)
- `CLI_README.md` (copy to Documentation/)
- `INSTALLATION_GUIDE.md` (copy to Documentation/)
- `run.bat` (copy to Windows/ folder)
- `run.sh` (copy to Mac_Linux/ folder)

### **Create Shared Folder README:**
Create a new file called `README.md` in the root of `Excel_to_JSON_Tool/` folder with content below.

---

## **Step 3: Send Team Email**

Once uploaded, send this email to your team:

```
Subject: ⭐ Excel to JSON Converter Tool - Now Available on Shared Drive

Hi Team,

The Excel to JSON converter tool is now available on our shared drive for everyone to use!

📍 LOCATION:
[Paste your shared drive path here]
Example: \\company\shared\Tools\Excel_to_JSON_Tool
         or https://company.sharepoint.com/sites/Tools/Excel_to_JSON_Tool
         or /mnt/shared/Tools/Excel_to_JSON_Tool

🚀 QUICK START:

For Windows:
1. Go to the "Windows" folder
2. Double-click "run.bat"
3. Drag your Excel file onto it
4. Get your JSON instantly!

For Mac/Linux:
1. Go to the "Mac_Linux" folder
2. Open Terminal there
3. Run: chmod +x run.sh
4. Run: ./run.sh your_file.xlsx
5. Get your JSON instantly!

📖 HELP:
- See "QUICK_START.md" for quick instructions
- See "Documentation" folder for detailed guides
- See "Examples" folder for sample files

⭐ KEY BENEFITS:
✅ Works completely offline (no internet needed)
✅ No cloud upload (all files stay on your computer)
✅ No company policy issues
✅ One-click conversion (Windows) or simple command (Mac/Linux)

Questions? Contact: [Your Name] or [Your Email]
```

---

## **Step 4: Set Permissions (Optional)**

If your shared drive allows:
- Set folder to **Read-Only** for team members (prevents accidental changes)
- Set to **Read-Write** if you want team to save output files there

---

## **Files to Create for Shared Drive**

I'll create the specific files you need below.

