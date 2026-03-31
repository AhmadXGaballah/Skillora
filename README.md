
<div align="center">

<img src="https://github.com/user-attachments/assets/8e34f404-8d92-45c2-bbc5-6ec45bf7b1f2" alt="Skillora Logo" width="300" />

# Skillora

### **Where Skills Meet Opportunity**

<p align="center">
  AI-powered candidate fit analysis for smarter resume screening, skill-gap detection, and role alignment.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/SentenceTransformers-Embeddings-1F6FEB?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Transformers-Skill%20Extraction-FCC624?style=for-the-badge&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/Use%20Case-Resume%20%26%20Job%20Matching-222222?style=for-the-badge" />
</p>

<p align="center">
  <strong>Upload a resume. Compare it to a role. Surface fit, skills, and gaps with clarity.</strong>
</p>

</div>

---

## Product Overview

### What is Skillora?
**Skillora** is an AI-powered candidate fit analysis platform that compares resumes against job descriptions to reveal how well a profile aligns with a target role.

### Why does it matter?
Traditional resume screening is often manual, inconsistent, and overly dependent on keyword matching. Skillora introduces a more structured workflow by helping users quickly understand:

- whether a candidate appears to be a **Strong Match**, **Good Match**, or **Weak Match**
- which skills are already present in the resume
- which capabilities are expected by the target role
- where meaningful gaps still remain

### Core workflow
Skillora is built around a simple product flow:

1. **Upload a resume**
2. **Add a target job link/description**
3. **Run the analysis**
4. **Review fit, matched skills, and missing skills**

> **Skillora turns resumes and job descriptions into clear fit insights.**
---


## Preview

<p align="center">
  <img src="https://github.com/user-attachments/assets/bf97f0f6-6773-43e1-a644-a28c8049e135" alt="Skillora UI Preview" width="900"/>
</p>




---
## How It Works

Skillora follows a structured resume-to-role analysis pipeline that combines text extraction, skills intelligence, and semantic similarity to evaluate candidate fit.

### Step 1 — Resume Parsing
The user uploads a resume in **PDF**, **DOCX**, or **TXT** format.

Skillora extracts the text content from the uploaded file and prepares it for downstream analysis.

### Step 2 — Job Description Ingestion
The target role is provided through either:

- a pasted **job description**
- a **job post link**

If a full description is pasted, Skillora uses it directly. If a link is provided, the app attempts to retrieve the job content and convert it into usable text.

### Step 3 — Text Cleaning and Normalization
Both the resume text and the job description are cleaned and normalized to reduce formatting noise and improve analytical consistency.

This step helps standardize the inputs before matching and skill extraction.

### Step 4 — Skills Extraction
Skillora extracts relevant skills from both the resume and the job description using a hybrid skills pipeline that combines:

- **pattern-based extraction**
- **dictionary / synonym normalization**
- **NER-assisted skill detection**

This allows the app to identify:

- candidate skills reflected in the resume
- target or required skills implied by the role description

### Step 5 — Semantic Role Matching
To evaluate overall alignment, Skillora converts the resume text and job description into **text embeddings** using a **Sentence Transformer** model.

The two embeddings are then compared using **cosine similarity** to measure how closely the candidate profile aligns with the target role at the semantic level, beyond simple keyword overlap.

### Step 6 — Match Classification
The cosine similarity result is mapped into a recruiter-friendly verdict:

- **Strong Match**
- **Good Match**
- **Weak Match**

This keeps the output interpretable and professional without exposing raw model scores to the user.

### Step 7 — Skills Gap Analysis
Skillora compares the extracted resume skills against the extracted target-role skills to identify:

- **matched skills**
- **missing skills**
- **underrepresented capability areas**

This gives users a clearer view of both alignment and gaps.

### Step 8 — Structured Output
The final analysis is presented through a clean interface that surfaces:

- overall fit verdict
- candidate skills
- required / target skills
- matched skills
- missing skills
- processed job description preview
---

## Example Output

A typical Skillora analysis may answer:

- The candidate is a **Good Match**
- The resume already demonstrates **SQL, Python, Excel, and Power BI**
- The role also expects **Tableau, A/B Testing, and BigQuery**
- The strongest overlap is in reporting, dashboarding, and analytical tooling
- The main gaps are in additional analytics platforms or experimentation workflows

This allows the output to support actual screening decisions rather than just showing model internals.

---
## How to run 

1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Run the application
```bash
streamlit run app.py 
```








