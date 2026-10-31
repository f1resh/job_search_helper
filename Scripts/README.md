# Helper Scripts

This directory contains automation utilities for the Job Search Assistant.

## Available Scripts

### 1. `md_to_pdf.py` (Markdown to PDF Converter)
Converts Markdown CVs and reports into clean, modern, ATS-friendly PDFs using headless Google Chrome (`C:\Program Files\Google\Chrome\Application\chrome.exe`).

#### Features:
- Professional resume CSS styling with proper typography, spacing, and page break prevention.
- Strips browser default headers/footers (clean document output).
- Automatic title detection from Markdown `# Heading 1`.

#### Usage via Terminal:
```powershell
# Convert a CV in place (generates tailored_cv.pdf alongside tailored_cv.md)
.\.venv\Scripts\python.exe Scripts\md_to_pdf.py Vacancies\US\Google_Senior_Backend\tailored_cv.md

# Convert with explicit output path:
.\.venv\Scripts\python.exe Scripts\md_to_pdf.py Base\CV_Base.md My_Resume.pdf
```

### 2. `convert_to_pdf.bat` (Windows Drag & Drop / Quick Runner)
- Double click or run from terminal:
  ```cmd
  Scripts\convert_to_pdf.bat Vacancies\US\Google_Senior_Backend\tailored_cv.md
  ```
- Or drag-and-drop any `.md` file in Windows File Explorer directly onto `convert_to_pdf.bat`.

### 3. `sync_skills.py` (Skills Sync)
`.agents/skills/` is the single source of truth for the agent skills. Claude Code only discovers skills in `.claude/skills/`, so this script mirrors the source there: it copies new and changed files and removes files that were deleted from the source.

#### Usage via Terminal:
```powershell
# Copy changes from .agents/skills to .claude/skills
.\.venv\Scripts\python.exe Scripts\sync_skills.py

# Only report differences (exit code 1 if out of sync)
.\.venv\Scripts\python.exe Scripts\sync_skills.py --check
```
