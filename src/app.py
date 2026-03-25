from __future__ import annotations

import requests
import streamlit as st

from .config import APP_NAME
from .job_ingestion import prepare_job_description
from .loaders import load_embedding_model, load_skill_ner_pipeline
from .matching import classify_match, semantic_similarity
from .skills import extract_skills
from .styling import inject_premium_css
from .text_processing import clean_text, extract_text
from .ui import render_chips, render_hero, render_match_banner


def run_app() -> None:
    st.set_page_config(
        page_title=APP_NAME,
        page_icon="🎯",
        layout="wide",
        initial_sidebar_state="collapsed",
    )

    inject_premium_css()
    render_hero()

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### Candidate Resume")
    st.caption("Upload a clean PDF, DOCX, or TXT file for analysis.")
    uploaded_file = st.file_uploader(
        "Upload candidate resume",
        type=["pdf", "docx", "txt"],
        label_visibility="collapsed",
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.markdown("#### Target Job")
    st.caption("Paste the full job description for the most reliable analysis, or provide a job post link.")
    job_link = st.text_input(
        "Job post link",
        placeholder="https://company.com/jobs/product-analyst",
    )
    job_description = st.text_area(
        "Job description",
        placeholder="Paste the full job description here...",
        height=260,
    )
    analyze = st.button("Run Match Analysis", type="primary", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    if not analyze:
        st.markdown(
            "<div class='muted-note'>Ready when you are. Upload the resume and add the target role context to generate the analysis.</div>",
            unsafe_allow_html=True,
        )
        return

    try:
        if uploaded_file is None:
            raise ValueError("Please upload a resume before running the analysis.")

        with st.spinner("Loading models and processing inputs..."):
            embedding_model = load_embedding_model()
            ner_pipeline = load_skill_ner_pipeline()
            resume_text = extract_text(uploaded_file)

            if embedding_model is None:
                raise RuntimeError("Embedding model failed to load.")

            if ner_pipeline is None or not callable(ner_pipeline):
                raise RuntimeError(
                    "Skill extraction pipeline failed to load. Please clear Streamlit cache and rerun."
                )

            if not resume_text.strip():
                raise ValueError("No readable text was extracted from the uploaded resume.")

            jd_text, scraped_title, source_label = prepare_job_description(job_link, job_description)
            if not jd_text.strip():
                raise ValueError(
                    "The job description appears empty after processing. Please paste the description manually."
                )

            cleaned_resume = clean_text(resume_text)
            cleaned_jd = clean_text(jd_text)

            similarity = semantic_similarity(cleaned_resume, cleaned_jd, embedding_model)
            match_label, match_css, match_caption = classify_match(similarity)

            candidate_skills = extract_skills(resume_text, ner_pipeline, use_requirement_focus=False)
            required_skills = extract_skills(jd_text, ner_pipeline, use_requirement_focus=True)
            candidate_skill_set = set(candidate_skills)
            required_skill_set = set(required_skills)

            matched_skills = sorted(candidate_skill_set & required_skill_set)
            missing_skills = sorted(required_skill_set - candidate_skill_set)

        st.divider()
        render_match_banner(match_label, match_css, match_caption, scraped_title)

        metric_1, metric_2, metric_3 = st.columns(3)
        with metric_1:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Assessment</div>
                    <div class="metric-value">{match_label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with metric_2:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Candidate skills found</div>
                    <div class="metric-value">{len(candidate_skills)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        with metric_3:
            st.markdown(
                f"""
                <div class="metric-card">
                    <div class="metric-label">Missing / required skills</div>
                    <div class="metric-value">{len(missing_skills)}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        tab_skills, tab_source = st.tabs(["Skills", "Job Source"])

        with tab_skills:
            skill_col_1, skill_col_2 = st.columns(2, gap="large")
            with skill_col_1:
                st.markdown("### Candidate Skills")
                render_chips(
                    candidate_skills[:30],
                    "chip-candidate",
                    "No skills were extracted from the resume.",
                )
                st.markdown("### Skills Already Matched")
                render_chips(
                    matched_skills[:30],
                    "chip-match",
                    "No overlapping skills were detected between the resume and the job description.",
                )

            with skill_col_2:
                st.markdown("### Required / Target Skills")
                render_chips(
                    required_skills[:30],
                    "chip-candidate",
                    "No clear requirement skills were extracted from the job description.",
                )
                st.markdown("### Missing Skills")
                render_chips(
                    missing_skills[:30],
                    "chip-missing",
                    "No notable missing skills were detected.",
                )

        with tab_source:
            st.markdown("### Job Description Source")
            st.caption(source_label or "No source label available")

            if job_link:
                st.markdown(f"**Reference link:** {job_link}")

            st.markdown("### Processed Description Preview")
            preview_text = jd_text[:2000] + ("..." if len(jd_text) > 2000 else "")
            st.text_area(
                "Preview",
                preview_text,
                height=260,
                disabled=True,
                label_visibility="collapsed",
            )

    except requests.HTTPError as exc:
        st.error(
            "The job link could not be retrieved successfully. Some job boards restrict automated access. Paste the full job description manually and rerun the analysis."
        )
        st.caption(str(exc))
    except Exception as exc:
        st.error(str(exc))
