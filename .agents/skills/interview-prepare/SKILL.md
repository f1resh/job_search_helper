---
name: interview-prepare
description: >-
  Use this skill when the user asks to prepare for an interview for a specific vacancy already evaluated in Vacancies/, or asks for an extensive list of interview questions (technical, behavioral, soft and hard skills, scenarios) for a saved position.
---

# Interview Preparation & Comprehensive Question Bank Skill

This skill generates a comprehensive, tailored question bank and interview preparation dossier for a specific job vacancy previously saved in the `Vacancies/` directory.

---

## Trigger Conditions

Activate this skill when:
- The user asks: *"Prepare me for the interview for [Company / Role]"*, *"Generate interview questions for [Vacancy]"*, or *"Run interview_prepare for [Vacancy]"*.
- The user wants mock interview questions, technical deep-dives, or behavioral prep for an existing vacancy.

---

## Workflow Steps

### Step 1: Identify the Target Vacancy

1. **Locate the vacancy folder in `Vacancies/`:**
   - Scan `d:\JobSearch\Vacancies\` (including regional subfolders like `US/`, `EU/`, etc.).
   - If the user specifies the company or role (e.g., "Stripe" or "Frontend Lead at Acme"), match it against folder names.
   - If ambiguous or not specified:
     - List available vacancy folders found in `Vacancies/` with their dates/titles.
     - Prompt the user to select which one they are preparing for.
2. **Read the vacancy artifacts:**
   - `<vacancy_folder>/job_description.md` (role details, requirements, tech stack)
   - `<vacancy_folder>/match_report.md` (identified pros/cons, fit score, gap analysis)
   - `<vacancy_folder>/tailored_cv.md` (the tailored narrative presented to this employer)

---

### Step 2: Read Candidate Ground Truth from `Base/`

Read:
- **[`Base/CV_Base.md`](file:///d:/JobSearch/Base/CV_Base.md)**: Full project and achievement history (used to craft realistic STAR stories).
- **[`Base/About_Me.md`](file:///d:/JobSearch/Base/About_Me.md)**: Candid personality, work style, genuine strengths, imposter/brush-up areas.
- **[`Base/Skills_Matrix.md`](file:///d:/JobSearch/Base/Skills_Matrix.md)**: Proficiency tiers for technical accuracy.

---

### Step 3: Generate the Comprehensive Interview Question Bank

Create a file named `interview_questions.md` inside that target vacancy's folder:
`<vacancy_folder>/interview_questions.md`

The document must contain five extensive sections tailored to the target role:

#### Section 1: Role & Company Context
- **The Core Mission:** What the engineering team is solving and why they opened this role.
- **The Tech Stack in Focus:** Primary technologies, libraries, and tools expected during technical rounds.
- **Key Challenges of the Domain:** Specific challenges (e.g. high-throughput systems, latency constraints, state management, distributed consistency).

#### Section 2: Technical & Hard Skills Questions (Deep Dive)
*Grouped by topic, tailored strictly to the role's stack and the candidate's background:*
- **Language & Framework Mechanics:**
  - In-depth questions on the target languages and core frameworks (runtime internals, lifecycle, memory, concurrency/async, optimization).
  - Common pitfalls, edge cases, and anti-patterns.
- **Architecture & System Design:**
  - "How would you architect a solution from scratch for [Company's specific product or service requirement]?"
  - Scalability, modularity, data flow, failure recovery, and trade-off analysis.
- **Infrastructure, Tooling & Quality:**
  - CI/CD automation, testing strategies, deployment safety, and production observability.
  - Debugging challenging real-world issues (race conditions, memory leaks, performance bottlenecks).
- **Domain-Specific Scenarios:**
  - Concrete technical problems the company actually faces in their sector.

#### Section 3: Behavioral Questions & STAR Story Mappings
*For each question, provide:*
1. **The Question** (e.g., *"Describe a situation where a critical issue occurred in production."* or *"Tell me about a time you had to manage conflicting technical priorities under a tight deadline."*)
2. **Why they ask this** (what the interviewer is evaluating).
3. **Recommended Story from Candidate's History:** Directly map to a real project from `Base/CV_Base.md`.
4. **STAR Framing Guide:**
   - **Situation:** Real context from candidate's past projects.
   - **Task:** What needed to be accomplished.
   - **Action:** Concrete technical/leadership actions taken.
   - **Result:** Measurable outcome (business metrics, performance improvements, cycle time reductions).

#### Section 4: Soft Skills, Communication & Stakeholder Scenarios
- Handling technical disagreements with peers, cross-functional partners, or product managers.
- Communicating technical trade-offs and complexity to non-technical stakeholders.
- Working effectively in remote or distributed teams across timezones.
- **Reverse-Interview Questions:** 5–7 sharp questions for the candidate to ask the interviewers to vet engineering culture, technical debt, and team autonomy.

#### Section 5: "Night Before the Interview" Cheat Sheet
- 1-page condensed recap:
  - 5 key technical definitions, architectural principles, or patterns to review.
  - 3 main career narrative stories to keep at the top of mind.
  - Key quantifiable metrics from the CV.

---

### Step 4: Optional PDF Compilation

Check if the user would like a printable PDF of the interview guide. If requested or appropriate, run:
```powershell
.\.venv\Scripts\python.exe Scripts\md_to_pdf.py "<vacancy_folder>/interview_questions.md"
```

---

### Step 5: Proactive Inquiry & Behavioral Calibration

> [!IMPORTANT]
> **The Information Maximization Principle:** The deeper and more candid the details shared by the candidate, the more compelling and authentic their interview responses will sound to senior interviewers.

Formulate **2–3 specific calibration questions** to refine their interview answers:
1. **Real Conflict / Disagreement Story:** *"The guide highlights handling pushback on [architecture/release timeline]. Did you experience a specific real disagreement in a past role you'd prefer to use for this question?"*
2. **Handling Failure / Tough Bugs:** *"Interviews for this role will probe production incidents. Is there a specific mistake or production issue from your past you feel comfortable dissecting?"*
3. **Deep Technical Defense:** *"They will likely grill you on trade-offs between [Tech A] and [Tech B]. How would you personally defend your past choice of [Tech A] in your own words?"*

---

### Step 6: Deliver Response to User

Output a clear summary in chat:
1. Confirmation of the target vacancy analyzed.
2. Breakdown of the key themes covered in the preparation guide.
3. Top 3 highest-probability questions the candidate must master for this role.
4. **Targeted Follow-up Questions:** Present the 2–3 calibration questions from Step 5 to gather real stories and sharpen the STAR responses.
5. Direct clickable link to the generated [`interview_questions.md`](file:///path/to/interview_questions.md) file.
