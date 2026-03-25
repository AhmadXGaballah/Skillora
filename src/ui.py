from __future__ import annotations

import html
from typing import List, Optional

import streamlit as st

from .config import APP_NAME, APP_SUBTITLE, APP_TAGLINE


def render_hero() -> None:
    hero_html = f"""
<div class="premium-hero">
    <h1 class="premium-hero-title">🎯 {APP_NAME}</h1>
    <div class="hero-tagline">{APP_TAGLINE}</div>
    <p class="premium-hero-subtitle">
        {APP_SUBTITLE}
    </p>
</div>
"""
    st.markdown(hero_html, unsafe_allow_html=True)


def render_section_header(title: str, text: str) -> None:
    st.markdown(
        f"""
        <div class="glass-card">
            <div class="section-title">{html.escape(title)}</div>
            <div class="section-text">{html.escape(text)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_chips(items: List[str], variant: str, empty_message: str) -> None:
    if not items:
        st.markdown(f"<div class='small-note'>{html.escape(empty_message)}</div>", unsafe_allow_html=True)
        return

    chips = "".join(
        [f"<span class='chip {variant}'>{html.escape(item)}</span>" for item in items]
    )
    st.markdown(f"<div class='chip-wrap'>{chips}</div>", unsafe_allow_html=True)


def render_match_banner(
    match_label: str,
    match_css: str,
    caption: str,
    job_title: Optional[str],
) -> None:
    title_line = match_label if not job_title else f"{match_label} · {html.escape(job_title)}"
    st.markdown(
        f"""
        <div class="match-banner {match_css}">
            <div class="match-label">{title_line}</div>
            <p class="match-caption">{html.escape(caption)}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
