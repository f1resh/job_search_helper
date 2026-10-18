# Candidate Base Profile

This directory stores your core information. The AI agent reads these files every time you share a job vacancy to evaluate match, write tailored CVs, and prepare study plans.

> [!IMPORTANT]
> ### Provide the Most Honest Answers Possible (Even If Hurtful)
> When creating your biography, filling out documents, or answering the assistant's clarifying questions, be **radically honest**. Do not sugarcoat your skills, hide what you hate doing, or gloss over past failures. Admitting where you struggle, lack deep knowledge, or burn out may feel uncomfortable, but it is precisely what allows the AI to filter out toxic fits, highlight your authentic strengths, and prepare you for real-world interviews.

---

## Two Setup Options

### Option 1: Manual Setup via Examples
You can copy and edit the provided `.example` files directly:
1. Copy `CV_Base.md.example` to `CV_Base.md` and fill in your career history.
2. Copy `About_Me.md.example` to `About_Me.md` and document your personality, energizers, and deal-breakers.
3. Copy `Skills_Matrix.md.example` to `Skills_Matrix.md` and adjust your proficiency tiers.
4. (Optional) Write your background narrative in `Biography_Raw.md`.
5. Run `.\.venv\Scripts\python.exe Scripts\md_to_pdf.py Base\CV_Base.md Base\CV_Base.pdf` to compile your master PDF.

### Option 2: Automated Generation via AI (`generate-base-docs` Skill)
1. Place your current CV (PDF, Markdown, or text) into this folder or paste it into the chat.
2. Write a free-form biography about yourself in chat (the more detailed and honest, the better—covering early interests, job history, what you enjoyed/disliked, and financial goals). See [`Biography_Raw.md.example`](file:///d:/JobSearch/Base/Biography_Raw.md.example) for inspiration.
3. Ask the assistant: *"generate base docs"* (or use the `generate-base-docs` skill).
4. The assistant will automatically extract all traits, categorize skills into 5 tiers, build your master CV, compile the PDF, and ask a few follow-up questions to fine-tune.

---

## Active Files in this Directory

- **[`CV_Base.md`](file:///d:/JobSearch/Base/CV_Base.md)**: Master career history, quantified achievements, and credentials.
- **[`CV_Base.pdf`](file:///d:/JobSearch/Base/CV_Base.pdf)**: Compiled ATS-friendly master PDF.
- **[`About_Me.md`](file:///d:/JobSearch/Base/About_Me.md)**: Candid personality, work style, energizers, deal-breakers, and real experience levels.
- **[`Skills_Matrix.md`](file:///d:/JobSearch/Base/Skills_Matrix.md)**: Categorized proficiency tiers (Tier 1 Core through Tier 5 Avoid).
- **[`Biography_Raw.md`](file:///d:/JobSearch/Base/Biography_Raw.md)**: Raw, unedited background narrative provided by candidate.

---

## Generic Template Examples

- **[`CV_Base.md.example`](file:///d:/JobSearch/Base/CV_Base.md.example)**: Generic React frontend developer resume template example.
- **[`About_Me.md.example`](file:///d:/JobSearch/Base/About_Me.md.example)**: Generic personality, working style, and preference template.
- **[`Skills_Matrix.md.example`](file:///d:/JobSearch/Base/Skills_Matrix.md.example)**: Generic 5-tier technical and soft skills matrix template.
- **[`Biography_Raw.md.example`](file:///d:/JobSearch/Base/Biography_Raw.md.example)**: Sample free-form biography narrative.
