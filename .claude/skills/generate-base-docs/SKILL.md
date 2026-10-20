---
name: generate-base-docs
description: >-
  Use this skill when the user provides their CV (PDF, markdown, or text) and/or free-form biography to initialize or overhaul their base candidate profile in Base/. Analyzes the background, extracts personality, cognitive traits, work style, real skill tiers, energizers, deal-breakers, generates Base/Biography_Raw.md, Base/About_Me.md, Base/Skills_Matrix.md, Base/CV_Base.md, and compiles Base/CV_Base.pdf.
---

# Generate Base Documents Skill

This skill automates the onboarding process for a new candidate by ingesting their raw biography narrative and existing CV, extracting deep psychological and professional insights, and generating the foundational profile files in [`Base/`](file:///d:/JobSearch/Base/).

---

## Trigger Conditions

Activate this skill when:
- The user asks: *"generate base docs"*, *"initialize my profile"*, *"build base profile from my bio"*, or provides a free-form biography narrative and CV to set up the system.
- The user provides an updated CV and raw background story and wants their base documents regenerated.

---

## Step-by-Step Workflow

### Step 1: Ingest Inputs

1. **Raw Biography Narrative:**
   - Ingest candidate biography provided either as text in the chat prompt or as a file.
2. **Existing CV / Resume:**
   - If a PDF file is present in `Base/` (e.g. `Base/*.pdf`), inspect and read its text using `view_file`.
   - If text or Markdown is pasted, parse its chronological work history, education, and credentials.

---

### Step 2: Extract Profile Facets

Thoroughly analyze both sources to extract:
1. **Professional Identity & Domain Expertise:**
   - Primary role targets, core value proposition, key industry domains (e.g., SaaS, fintech, cloud infrastructure, consumer platforms).
2. **Cognitive Traits & Working Style:**
   - Problem-solving style (systems thinker, deep researcher, fast prototyper, thorough architect).
   - Focus dynamics (e.g. sustained deep focus vs. multitasking tendencies).
   - Reaction to routine vs. novelty; reaction to feedback and critiques.
3. **Energizers & Deal-Breakers:**
   - Tasks, architectures, and problems that spark genuine enthusiasm.
   - Absolute deal-breakers (e.g. micromanagement, activity tracking software, toxic blame culture, mandatory in-office).
   - Avoidances (e.g. unmaintained legacy stacks, specific frameworks/languages).
4. **Honest Skill Categorization (5 Tiers):**
   - **Tier 1 (Core Expertise):** Technologies used extensively in production; can architect solutions from scratch.
   - **Tier 2 (Working Knowledge):** Solid everyday use; may consult documentation or use AI tools for rapid prototyping.
   - **Tier 3 (Familiar / Conceptual):** Used in past roles or side projects; knows theory but minimal recent production use.
   - **Tier 4 (Target Brush-Up / Want to Learn):** High-leverage growth areas for senior positions.
   - **Tier 5 (Explicitly Avoid):** Technologies or task types the candidate does not want in their daily work.
5. **Logistics & Financial Goals:**
   - Current compensation vs. target compensation (e.g., US remote contractor \$80k–\$120k).
   - Location, work rights, and notice period.

---

### Step 3: Generate Base Files

Write the following four structured files into `Base/`:

1. **[`Base/Biography_Raw.md`](file:///d:/JobSearch/Base/Biography_Raw.md)**:
   - A verbatim copy of the raw candidate biography (especially when provided as prompt text in the chat rather than an existing file) to ensure the original narrative is permanently preserved as a historical source of truth.
2. **[`Base/About_Me.md`](file:///d:/JobSearch/Base/About_Me.md)**:
   - Grounded candid profile capturing cognitive traits, energizers, deal-breakers, real depth vs shallow areas, and career goals.
3. **[`Base/Skills_Matrix.md`](file:///d:/JobSearch/Base/Skills_Matrix.md)**:
   - 5-tier technical and professional matrix with years of experience, confidence scores, and real-world project context.
4. **[`Base/CV_Base.md`](file:///d:/JobSearch/Base/CV_Base.md)**:
   - Comprehensive master resume capturing all roles, quantified achievements (metrics, scale, cycle time reductions), developer tools built, teaching/mentoring, education, and languages.

---

### Step 4: Compile Master PDF

Compile the Markdown CV to a clean, ATS-friendly PDF:
```powershell
.\.venv\Scripts\python.exe Scripts\md_to_pdf.py Base\CV_Base.md Base\CV_Base.pdf
```
Verify via `view_file` that the resulting PDF renders cleanly without orphan page spills.

---

### Step 5: Interactive Calibration & Proactive Inquiry

> [!IMPORTANT]
> **The Radical Honesty & Information Maximization Principle:** The more accurate, nuanced, and brutally honest the information provided by the candidate, the better the system performs. Encourage the candidate to be completely candid—especially regarding what they dislike, gaps in knowledge, or past mistakes—even if uncomfortable to admit.

Present an executive summary to the user in chat:
1. Overview of extracted personality traits, energizers, deal-breakers, and core skills.
2. Direct links to all four generated files.
3. **Mandatory Proactive Questions:** Formulate **3–5 specific clarifying questions** addressing:
   - Missing scale or quantitative impact metrics (e.g. system throughput, team size, cycle time changes).
   - Ambiguous technical depth (e.g. production architecture vs. simple scripting/reading).
   - Real-world friction points, deal-breakers, and genuine compensation targets.
