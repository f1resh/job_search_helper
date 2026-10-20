---
name: job-match-analyst
description: >-
  Use this skill whenever the user shares a job vacancy link, job posting URL, job description text, or asks to evaluate a position. Investigates the vacancy, validates fit against Base/ profile, generates a match score with pros and cons, produces an ATS-tailored Markdown CV, writes an interview study guide, saves files under Vacancies/, and converts the CV to PDF.
---

# Job Match Analyst & Tailored CV Generator Skill

This skill guides the agent through an end-to-end evaluation of a job vacancy against the candidate's real profile in `Base/`, generating deep analysis, an ATS-tailored Markdown CV, a study/prep guide, and an export-ready PDF.

---

## Workflow Steps

### Step 1: Ingest & Parse the Vacancy

1. **If a URL is provided:**
   - Call `read_url_content` with the provided URL.
   - If the page is blocked by authentication (e.g., LinkedIn login wall, Cloudflare challenge, or CAPTCHA):
     - Politely notify the user and ask them to copy-paste the text of the job description or main requirements directly in the chat.
2. **Extract key vacancy parameters:**
   - **Job Title & Company Name**
   - **Location & Work Mode:** (Remote / Hybrid / On-site, Country / City / Timezone constraints)
   - **Seniority & Experience Level:** (Junior, Mid, Senior, Lead, Staff, etc.)
   - **Core Requirements (Must-haves):** Primary languages, frameworks, years of experience, specific system scales.
   - **Nice-to-haves / Bonus skills:** Secondary tools, domain knowledge.
   - **Key Responsibilities:** What the day-to-day work actually involves.
   - **Compensation / Benefits:** Salary range, equity, bonus (if stated).

---

### Step 2: Ingest the Candidate Profile from `Base/`

Read the current profile files from `d:\JobSearch\Base\`:
1. **[`Base/CV_Base.md`](file:///d:/JobSearch/Base/CV_Base.md)**: Master career history, achievements, and facts.
2. **[`Base/About_Me.md`](file:///d:/JobSearch/Base/About_Me.md)**: Candid personality, preferred pace, energizers, deal-breakers, and honest self-assessment.
3. **[`Base/Skills_Matrix.md`](file:///d:/JobSearch/Base/Skills_Matrix.md)**: Proficiency tiers (Tier 1 Core, Tier 2 Working, Tier 3 Familiar, Tier 4 Want to Learn, Tier 5 Do Not Want).

> [!IMPORTANT]
> **Ground Rule of Truth:** Never fabricate experience, qualifications, or roles that the candidate does not possess. Tailoring means highlighting real relevant achievements, re-ordering emphasis, aligning vocabulary to the company's tech terminology, and framing projects accurately.

---

### Step 3: Verify Fit, Calculate Match Score, and Analyze Pros & Cons

1. **Calculate Fit Score (0 - 100%):**
   - **85 - 100% (High Fit):** Overwhelming alignment with candidate's Tier 1/2 skills and work preferences.
   - **70 - 84% (Strong Fit):** Strong technical overlap; minor gaps in non-critical nice-to-haves.
   - **50 - 69% (Moderate / Stretch):** Missing 1-2 core tools or requires learning on the job; worth applying if candidate is passionate.
   - **Below 50% (Low Fit / Not Recommended):** Major tech stack mismatch, significant deal-breaker conflict, or unrealistic seniority gap.

2. **Identify Honest Pros:**
   - Why this vacancy fits the candidate's strengths and personality.
   - Areas where the candidate can immediately deliver high impact.
   - Career growth opportunities aligned with Tier 4 interests.

3. **Identify Honest Cons & Red Flags:**
   - Direct conflicts with `Base/About_Me.md` deal-breakers (e.g. 24/7 on-call, toxic patterns, legacy tech from Tier 5).
   - Tech stack gaps where candidate has zero prior experience.
   - Ambiguous job descriptions or warning signs (e.g., "fast-paced family environment", wearing 10 unrelated hats).

4. **Identify Study & Gap Areas:**
   - Specific tools, concepts, or system design patterns the candidate must review before interviewing.

---

### Step 3b: Deal‑breaker / Red‑flag Confirmation
- If any **Honest Cons & Red Flags** were identified above, pause the workflow.
- Present the list of red flags to the user and ask for explicit confirmation to continue.
- Only proceed to the next steps if the user replies with a clear affirmative (e.g., “yes, continue”).

### Step 4a: Duplicate Vacancy Check
- Compute the target folder path as described in Step 4.
- If the folder already exists, do **not** overwrite.
- Respond to the user: "A vacancy folder for this role/company/date already exists. Do you want to (a) abort, (b) create a new dated folder, or (c) overwrite?".
- Proceed based on the user’s explicit choice.

### Step 4: Create Vacancy Directory & Output Files
Determine target folder inside `Vacancies/`:
- If region is identifiable (e.g. US, EU, UK, Remote), organize under `Vacancies/<Region>/<YYYY-MM-DD>_<Company>_<Role_Slug>/`. Otherwise, use `Vacancies/<YYYY-MM-DD>_<Company>_<Role_Slug>/`.
- Create the folder and generate the following 4 files:

#### 1. `job_description.md`
Contains clean capture of the job listing, metadata (date, URL, company, title, compensation), and raw requirements.

#### 2. `match_report.md`
A structured report with:
- **Executive Summary & Verdict** (Apply / Caution / Skip)
- **Match Score & Rating Breakdown**
- **Pros & Cons Analysis**
- **Requirements Match Table:**
  | Requirement | Candidate Reality (from Base) | Match Status | Notes |
  | :--- | :--- | :--- | :--- |
- **Interview Positioning Strategy:** How the candidate should pitch themselves in the first round.

#### 3. `tailored_cv.md`
A customized, ATS-friendly Markdown CV tailored specifically for this role:
- Header with candidate's contact info.
- Targeted Professional Summary matching the role's mission and key requirements.
- Core Competencies section organized to feature the role's primary tech stack upfront.
- Re-ordered and emphasized bullet points focusing on metrics and responsibilities directly relevant to the role.
- Clean formatting compliant with `Scripts/md_to_pdf.py` renderer.

#### 4. `study_guide.md`
An actionable interview prep and study guide:
- **Priority 1: Must-Know Technical Concepts** (the specific tools/patterns mentioned in the job).
- **Priority 2: Likely Technical Interview Questions & Model Answers** tailored to this exact role.
- **Priority 3: Architecture & System Design Prep** (if applicable).
- **Behavioral Questions & Story Framing:** Key stories from `Base/CV_Base.md` mapped to this role's leadership / cultural values.
- **Cheat Sheet:** 5-minute quick refresher before the interview.

---

### Step 5: Convert Tailored CV to PDF

Run the PDF conversion script:
```powershell
.\.venv\Scripts\python.exe Scripts\md_to_pdf.py "<path_to_tailored_cv.md>"
```
Verify that the output `.pdf` is created in the same vacancy directory.

---

### Step 6: Proactive Inquiry & Candidate Calibration

> [!IMPORTANT]
> **The Information Maximization Principle:** The more accurate and honest information gathered from the candidate, the higher the quality of the match report, tailored CV, and interview guide.

Formulate **2–4 targeted clarifying questions** for the candidate based on the vacancy's unique demands:
1. **Unlisted / Edge Skills:** *"The vacancy requires [Tool X/Framework Y]. Have you used this in any unlisted capacity, or should we position you as an expert in related [Tool Z] who can pick it up quickly?"*
2. **Preference & Deal-Breaker Checks:** *"The posting mentions [on-call shifts / hybrid in-office / heavy travel]. Does this conflict with your current preferences?"*
3. **Specific Achievement Nuance:** *"They emphasize experience with [System Challenge X]. Do you have a specific real project or metric from your past we can highlight for this?"*

---

### Step 7: Deliver Response to User

Provide a clean, well-formatted response in chat:
1. **Quick Snapshot:** Job Title, Company, Match Score (`XX% - Rating`), Recommendation (Apply / Stretch / Skip).
2. **Top 3 Pros & Top 2 Cons / Caveats.**
3. **Key Study Highlights:** What must be learned or brushed up on immediately.
4. **Targeted Follow-up Questions:** Present the 2–4 calibration questions from Step 6 to gather deeper context and offer to refine the CV based on the answers.
5. **Clickable Links:**
   - [`match_report.md`](file:///path/to/match_report.md)
   - [`tailored_cv.md`](file:///path/to/tailored_cv.md)
   - [`tailored_cv.pdf`](file:///path/to/tailored_cv.pdf)
   - [`study_guide.md`](file:///path/to/study_guide.md)
   - [`job_description.md`](file:///path/to/job_description.md)
