# METHOD 3: SHARED FOLDER DISTRIBUTION - COMPLETE SETUP GUIDE

**Everything your company needs to distribute the Excel to JSON tool via shared drive**

---

## **📋 Complete Checklist**

### **Files You Need to Download from GitHub:**

```
From: https://github.com/naveenreddy1405/Excel-to-JSON_specificpayload

📥 DOWNLOAD THESE FILES:

Root Level:
  ✅ excel_to_json_converter.py
  ✅ run.bat
  ✅ run.sh
  ✅ CLI_requirements.txt
  ✅ QUICK_START.md
  ✅ README_WINDOWS.md
  ✅ README_MAC_LINUX.md
  ✅ SHARED_DRIVE_README.md
  ✅ INSTALLATION_GUIDE.md
  ✅ CLI_README.md

Optional (Sample Files):
  ✅ Examples folder (if available)
```

---

## **🗂️ Step 1: Create Shared Folder Structure**

On your company's shared drive (OneDrive, SharePoint, Network Drive, etc.), create this folder:

```
📁 Excel_to_JSON_Tool/
   │
   ├── 📄 README.md ← Copy content from SHARED_DRIVE_README.md
   ├── 📄 QUICK_START.md
   ├── 📄 TROUBLESHOOTING.md (if needed)
   │
   ├── 📁 Windows/
   │   ├── run.bat
   │   ├── excel_to_json_converter.py
   │   ├── CLI_requirements.txt
   │   └── README_WINDOWS.md
   │
   ├── 📁 Mac_Linux/
   │   ├── run.sh
   │   ├── excel_to_json_converter.py
   │   ├── CLI_requirements.txt
   │   └── README_MAC_LINUX.md
   │
   ├── 📁 Documentation/
   │   ├── INSTALLATION_GUIDE.md
   │   ├── CLI_README.md
   │   ├── QUICK_START.md (copy)
   │   └── TROUBLESHOOTING.md
   │
   └── 📁 Examples/
       ├── sample_input.xlsx
       └── sample_output.json
```

---

## **📂 Step 2: Upload Files**

### **For each OS folder (Windows and Mac_Linux):**

1. Copy these 4 files:
   - `run.bat` (or `run.sh` for Mac_Linux)
   - `excel_to_json_converter.py`
   - `CLI_requirements.txt`
   - `README_WINDOWS.md` (or `README_MAC_LINUX.md`)

2. Upload to appropriate folder on shared drive

### **For Documentation folder:**

1. Copy all documentation files
2. Upload to `Documentation/` folder

### **For Examples folder (optional):**

1. Create sample Excel file with test data
2. Create expected JSON output
3. Upload both to `Examples/` folder

---

## **📧 Step 3: Send Team Email**

Copy and paste this email template:

```
═══════════════════════════════════════════════════════════════

Subject: ⭐ Excel to JSON Converter Tool - Now Available

Hi Team,

Great news! The Excel to JSON converter tool is now available on our shared drive.

🎯 ACCESS:
[Shared Drive Path]
Example paths:
  Windows Network: \\company\shared\Tools\Excel_to_JSON_Tool
  OneDrive: https://company.sharepoint.com/sites/Tools/Excel_to_JSON_Tool
  Mac/Linux: /mnt/shared/Tools/Excel_to_JSON_Tool

🚀 QUICK START:

👉 WINDOWS USERS:
   1. Open: Excel_to_JSON_Tool → Windows folder
   2. Double-click: run.bat
   3. Drag your Excel file onto the window
   4. Done! Your JSON file is ready.

👉 MAC/LINUX USERS:
   1. Open: Excel_to_JSON_Tool → Mac_Linux folder
   2. Open Terminal there
   3. Run: chmod +x run.sh (first time only)
   4. Run: ./run.sh your_file.xlsx
   5. Done! Your JSON file is ready.

📚 NEED HELP?
   • See: QUICK_START.md (simple 5-minute guide)
   • See: Documentation folder (detailed guides)
   • See: Examples folder (sample files)

⭐ WHY USE THIS?
   ✅ Works completely offline
   ✅ No internet needed
   ✅ No company policy issues
   ✅ All files stay on your computer
   ✅ Fast & reliable conversion

❓ QUESTIONS?
   Contact: [Your Name] or [Your Email]
   or see: Documentation/TROUBLESHOOTING.md

═══════════════════════════════════════════════════════════════
```

---

## **🔐 Step 4: Set Permissions (Optional)**

Ask your IT admin to:

- **Read-Only access** for all team members (prevents accidental changes)
- **Read-Write access** if you want team to save output files in the shared folder

---

## **✅ Step 5: Verify Setup**

Test before announcing to team:

1. **Windows:**
   - Double-click `run.bat` in Windows folder
   - Should show help message or accept drag-drop

2. **Mac/Linux:**
   - Open Terminal in Mac_Linux folder
   - Run: `chmod +x run.sh`
   - Run: `./run.sh`
   - Should show help message

---

## **📊 Success Indicators**

Your setup is complete when:

- ✅ All files are uploaded to shared drive
- ✅ Windows users can double-click `run.bat`
- ✅ Mac/Linux users can run `./run.sh`
- ✅ Team can access the shared folder
- ✅ Documentation is readable and clear

---

## **🎯 Maintenance Notes**

### **When you update the tool:**

1. Update files in GitHub
2. Download new versions
3. Replace files in shared folder
4. Send email notifying team: "Version updated - please download latest"

### **If team reports issues:**

1. Check `Documentation/TROUBLESHOOTING.md`
2. Have them run with `-v` flag for verbose output
3. Request error message screenshot
4. Check if Python is installed on their machine

---

## **🚀 Common Shared Drive Paths**

- **Microsoft SharePoint:** `https://company.sharepoint.com/sites/...`
- **OneDrive Business:** `https://company-my.sharepoint.com/personal/...`
- **Windows Network Drive:** `\\servername\sharename\Tools\Excel_to_JSON_Tool`
- **Mac Network:** `/Volumes/ShareName/Tools/Excel_to_JSON_Tool`
- **Linux Network:** `/mnt/company_share/Tools/Excel_to_JSON_Tool`

---

## **📞 Support Resources**

Create this support structure:

| Document | Purpose | For Whom |
|----------|---------|----------|
| QUICK_START.md | 5-min basic setup | Everyone |
| README_WINDOWS.md | Windows detailed guide | Windows users |
| README_MAC_LINUX.md | Mac/Linux detailed guide | Mac/Linux users |
| INSTALLATION_GUIDE.md | Complete installation steps | New users |
| CLI_README.md | Advanced usage options | Power users |
| TROUBLESHOOTING.md | Common issues & solutions | When issues arise |

---

## **🎉 You're All Set!**

Your team can now:
- Access the tool from shared drive
- Convert Excel to JSON offline
- No company policy violations
- Zero setup complexity for most users

---

**Next Step:** Send the team email with the shared drive location!

For updates and support, they can refer to the documentation in the shared folder.

---

**Questions?** Check TROUBLESHOOTING.md or contact your IT admin.
