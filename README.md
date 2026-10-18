# JobSearch Assistant Workspace

An intelligent, candidate-centric job hunting system that analyzes vacancies, validates candidate fit, generates tailored ATS-friendly Markdown & PDF CVs, and produces targeted study plans and interview question banks.

---

## Workspace Structure

```
d:\JobSearch\
├── Base\                         # Candidate Source of Truth
│   ├── README.md                 # Guide on filling out base profile & onboarding options
│   ├── CV_Base.md.example        # Generic resume template example
│   ├── About_Me.md.example       # Generic candid profile example
│   ├── Skills_Matrix.md.example  # Generic 5-tier skills matrix example
│   └── Biography_Raw.md.example  # Generic narrative biography example
│
├── Scripts\                      # Automation & Utilities
│   ├── README.md                 # Script instructions
│   ├── md_to_pdf.py              # ATS-friendly Markdown-to-PDF converter (Chrome headless)
│   └── convert_to_pdf.bat        # Windows quick runner / drag-and-drop batch script
│
├── Vacancies\                    # Organized vacancy analyses
│   └── <Region>\                 # (e.g. US, EU, Remote)
│       └── <Date>_<Company>_<Role>\
│           ├── job_description.md
│           ├── match_report.md
│           ├── tailored_cv.md
│           ├── tailored_cv.pdf
│           ├── study_guide.md
│           └── interview_questions.md
│
├── .agents\
│   └── skills\
│       ├── generate-base-docs\
│       │   └── SKILL.md          # Profile onboarding: extracts base profile from CV + raw bio
│       ├── job-match-analyst\
│       │   └── SKILL.md          # Vacancy evaluation, fit scoring & tailored CV/PDF generation
│       └── interview-prepare\
│           └── SKILL.md          # Comprehensive interview question bank & STAR story prep
│
├── .venv\                        # Virtual environment (Python 3.13)
├── requirements.txt              # Dependencies (markdown, beautifulsoup4, requests)
└── AGENTS.md                     # Workspace persistent guidelines
```

---

## Core Philosophy: Radical Honesty & Proactive Inquiry

> [!IMPORTANT]
> ### Be Brutally Honest (Even When Uncomfortable)
> When initializing your profile, filling out base documents, or answering the assistant's questions, provide the **most candid, honest answers possible**—even if admitting a lack of knowledge in a trendy technology, past failures, struggle with routine tasks, or strict deal-breakers feels uncomfortable or hurtful.
>
> **Why Radical Honesty is Essential:**
> 1. **Prevents Toxic or Mismatched Jobs:** Glossing over dislikes or exaggerating skills leads to stressful roles that cause rapid burnout.
> 2. **Authentic Positioning:** Hiring managers respect engineers who know their boundaries, articulate past lessons, and speak with authentic credibility rather than scripted buzzwords.
> 3. **The Information Maximization Principle:** All built-in skills actively ask targeted follow-up questions. The more granular, unvarnished detail you provide, the sharper and more compelling your tailored CVs and interview guides will become.

---

## The Three Built-in Skills

### 1. `generate-base-docs` (Profile Onboarding & Initialization)
- **When to use:** When setting up a new candidate or overhauling an existing profile.
- **How it works:**
  - Reads your existing CV (PDF, text, or markdown) and free-form biography narrative (provided as chat prompt or file).
  - Preserves the raw narrative verbatim into `Base/Biography_Raw.md` as a permanent source of truth.
  - Extracts personality traits, working style, real skill depth across 5 tiers, energizers, deal-breakers, and career goals.
  - Generates `Base/About_Me.md`, `Base/Skills_Matrix.md`, `Base/CV_Base.md`, and compiles `Base/CV_Base.pdf`.
  - Prompts you with clarifying questions to resolve missing metrics or ambiguities.

### 2. `job-match-analyst` (Vacancy Evaluation & Tailoring)
- **When to use:** Whenever you paste a job posting URL or job description text in the chat.
- **How it works:**
  - Ingests and parses the vacancy requirements.
  - Evaluates fit against your candidate profile files in `Base/`.
  - Calculates an objective **Match Score (0–100%)** with honest **Pros & Cons / Red Flags**.
  - Generates 4 structured documents in `Vacancies/<Region>/<Date>_<Company>_<Role>/`:
    - `job_description.md`
    - `match_report.md`
    - `tailored_cv.md` (ATS-optimized Markdown CV highlighting real relevant achievements)
    - `study_guide.md` (priority study roadmap and concept review)
  - Automatically compiles `tailored_cv.md` to `tailored_cv.pdf` using headless Chrome.

### 3. `interview-prepare` (Comprehensive Interview Question Bank)
- **When to use:** When you are invited to an interview for any vacancy already evaluated in `Vacancies/`.
- **How it works:**
  - Ask in chat: *"Prepare me for the interview for [Company / Role]"*.
  - Generates an extensive `interview_questions.md` inside that vacancy's folder containing:
    - Technical and framework internals specific to the target stack.
    - System and software architecture design scenarios.
    - Behavioral questions pre-mapped to your real past projects using the **STAR method** (Situation, Task, Action, Result).
    - Soft skills, stakeholder conflict handling, and reverse-interview questions to ask them.
    - 1-page "Night Before the Interview" condensed cheat sheet.

---

## Getting Started: Two Ways to Set Up Your Base Profile

### Way 1: Manual Filling via Examples
1. Copy the `.example` files in [`Base/`](file:///d:/JobSearch/Base/):
   - `CV_Base.md.example` $\rightarrow$ `CV_Base.md`
   - `About_Me.md.example` $\rightarrow$ `About_Me.md`
   - `Skills_Matrix.md.example` $\rightarrow$ `Skills_Matrix.md`
2. Fill them in manually with your details.
3. Compile your master PDF:
   ```powershell
   .\.venv\Scripts\python.exe Scripts\md_to_pdf.py Base\CV_Base.md Base\CV_Base.pdf
   ```

### Way 2: Automated Generation via AI (`generate-base-docs`)
1. Place your current CV file (e.g. PDF) in `Base/` or paste its text in the chat.
2. Provide a candid, free-form biography in chat (the more detailed and honest, the better—covering work history, favorite/disliked tasks, personal habits, and salary goals). See [`Biography_Raw.md.example`](file:///d:/JobSearch/Base/Biography_Raw.md.example) for inspiration.
3. Ask the assistant: *"generate base docs"*.
4. The assistant executes the `generate-base-docs` skill and sets up all your source documents automatically.

---

## Utility Scripts

- **`Scripts/md_to_pdf.py`**: Converts any Markdown CV or report to an ATS-friendly PDF using headless Google Chrome (`C:\Program Files\Google\Chrome\Application\chrome.exe`).
- **`Scripts/convert_to_pdf.bat`**: Windows drag-and-drop batch runner. Drag any `.md` file onto this batch file in File Explorer to produce a `.pdf`.
