# Job Search Assistant - Workspace Instructions

This workspace is a specialized assistant system for evaluating job vacancies, validating fit against the candidate's real profile, generating tailored Markdown and PDF CVs, and creating interview study guides.

## Core Rules

1. **Candidate Profile Source of Truth:**
   - Candidate data is stored in [`Base/`](file:///d:/JobSearch/Base/):
     - [`CV_Base.md`](file:///d:/JobSearch/Base/CV_Base.md): Master CV and career achievements.
     - [`About_Me.md`](file:///d:/JobSearch/Base/About_Me.md): Candid personality, work style, likes/dislikes, deal-breakers, and real experience levels.
     - [`Skills_Matrix.md`](file:///d:/JobSearch/Base/Skills_Matrix.md): Skill tiers (Tier 1 Core through Tier 5 Avoid).
     - [`Biography_Raw.md`](file:///d:/JobSearch/Base/Biography_Raw.md): Verbatim candidate background story.
   - Never fabricate experience or qualifications. Always stay grounded in the candidate's actual background while framing and positioning achievements for maximum relevance.

2. **When Initializing or Overhauling Candidate Profile:**
   - Activate the [`generate-base-docs`](file:///d:/JobSearch/.claude/skills/generate-base-docs/SKILL.md) skill.
   - Ingest CV and free-form biography.
   - Save the raw biography verbatim to [`Base/Biography_Raw.md`](file:///d:/JobSearch/Base/Biography_Raw.md) as a permanent historical source of truth.
   - Extract personality traits, work approach, 5-tier skills matrix, and master CV.
   - Compile master PDF via `Scripts/md_to_pdf.py`.
   - Ask clarifying questions to resolve ambiguities or missing metrics.

3. **When the User Shares a Vacancy Link or Text:**
   - Activate the [`job-match-analyst`](file:///d:/JobSearch/.claude/skills/job-match-analyst/SKILL.md) skill workflow.
   - Fetch the URL content or process the job text.
   - Run the eligibility pre-check (Ineligible / Unclear / Open) before the fit analysis; for Ineligible vacancies, ask before doing the full package.
   - Evaluate match percentage and honest pros/cons.
   - Create a dedicated folder under `Vacancies/<Region>/<YYYY-MM-DD>_<Company>_<Role>/` (e.g., `Vacancies/US/2026-10-18_Company_Role/`).
   - Generate:
     - `job_description.md`
     - `match_report.md`
     - `tailored_cv.md`
     - `study_guide.md`
   - Convert `tailored_cv.md` to `tailored_cv.pdf` using `.\.venv\Scripts\python.exe Scripts\md_to_pdf.py`.
   - Provide an executive summary and clickable links in the chat.

4. **When the User Asks for Interview Preparation / Questions:**
   - Activate the [`interview-prepare`](file:///d:/JobSearch/.claude/skills/interview-prepare/SKILL.md) skill.
   - Target an existing vacancy from `Vacancies/`.
   - Generate an extensive `interview_questions.md` covering technical deep-dives, STAR behavioral stories, soft skills, and reverse-interview questions.
   - Ask clarifying questions about specific past scenarios to ground STAR stories in genuine experience.

5. **Proactive Inquiry & Radical Honesty Across All Skills:**
   - **The Information Maximization Principle:** The more detailed and accurate the information, the better the output. Always ask targeted clarifying questions in each workflow.
   - **Radical Honesty:** Encourage the user to provide the most brutally honest answers possible—even if admitting gaps, failures, or strong dislikes feels uncomfortable. Transparent honesty is what guarantees authentic CV positioning, prevents toxic job matches, and produces bulletproof interview preparation.

6. **Helper Scripts:**
   - Script directory: [`Scripts/`](file:///d:/JobSearch/Scripts/)
   - PDF generation uses Google Chrome at `C:\Program Files\Google\Chrome\Application\chrome.exe` via `Scripts/md_to_pdf.py`.
   - Python environment: `.\.venv\Scripts\python.exe`.
