from __future__ import annotations

import streamlit as st


def inject_premium_css() -> None:
    st.markdown(
        """
        <style>
        .stApp {
            background: #0b1020;
            color: #f8fafc;
        }

        .block-container {
            max-width: 1120px;
            padding-top: 2.2rem;
            padding-bottom: 3rem;
        }

        .premium-hero {
            background:
                radial-gradient(circle at top right, rgba(59,130,246,0.18), transparent 24%),
                linear-gradient(135deg, #111827 0%, #0f172a 55%, #111827 100%);
            border: 1px solid rgba(148, 163, 184, 0.14);
            border-radius: 28px;
            padding: 2.4rem 2.2rem 2rem 2.2rem;
            box-shadow: 0 20px 50px rgba(0,0,0,0.28);
            margin-bottom: 1.5rem;
        }

        .premium-hero-title {
            font-size: 3.2rem;
            line-height: 1.02;
            font-weight: 800;
            color: #ffffff;
            margin: 0;
            letter-spacing: -0.03em;
        }

        .hero-tagline {
            margin-top: 0.55rem;
            font-size: 1.1rem;
            font-weight: 600;
            color: #60a5fa;
            letter-spacing: 0.01em;
        }

        .premium-hero-subtitle {
            font-size: 1.05rem;
            line-height: 1.8;
            color: #cbd5e1;
            margin: 1rem 0 1.25rem 0;
            max-width: 820px;
        }

        .glass-card {
            background: #121a2b;
            border: 1px solid rgba(148,163,184,0.14);
            box-shadow: 0 12px 30px rgba(0,0,0,0.20);
            border-radius: 22px;
            padding: 1.4rem;
            margin-bottom: 1.2rem;
        }

        .section-title {
            font-size: 1.2rem;
            font-weight: 800;
            color: #ffffff;
            margin-bottom: 0.3rem;
        }

        .section-text, .stCaption {
            color: #94a3b8 !important;
        }

        .match-label {
            color: #ffffff;
        }

        .match-caption, .metric-label, .small-note, .muted-note {
            color: #cbd5e1;
        }

        .metric-card {
            background: #0f172a;
            border: 1px solid rgba(148,163,184,0.12);
            border-radius: 18px;
            padding: 1rem;
            box-shadow: none;
        }

        .metric-value {
            color: #ffffff;
        }

        div[data-testid="stFileUploader"] {
            background: #0f172a;
            border: 1px solid rgba(148,163,184,0.14);
            border-radius: 18px;
            padding: 0.35rem;
        }

        .stTextArea textarea,
        .stTextInput input {
            background-color: #0f172a !important;
            color: #ffffff !important;
            border: 1px solid rgba(148,163,184,0.16) !important;
            border-radius: 14px !important;
        }

        .stButton button {
            background: linear-gradient(135deg, #2563eb, #3b82f6) !important;
            color: white !important;
            border: none !important;
            border-radius: 14px !important;
            font-weight: 700 !important;
            height: 3rem !important;
            box-shadow: 0 10px 24px rgba(37, 99, 235, 0.28);
        }

        .chip-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 0.6rem;
            margin: 0.6rem 0 1rem 0;
        }

        .chip {
            display: inline-flex;
            align-items: center;
            padding: 0.5rem 0.85rem;
            border-radius: 999px;
            font-size: 0.9rem;
            font-weight: 600;
            line-height: 1;
            white-space: nowrap;
        }

        .chip-candidate {
            color: #e5e7eb;
            background: #1e293b;
            border: 1px solid rgba(148,163,184,0.18);
        }

        .chip-match {
            color: #bbf7d0;
            background: rgba(34, 197, 94, 0.10);
            border: 1px solid rgba(34, 197, 94, 0.25);
        }

        .chip-missing {
            color: #fecaca;
            background: rgba(239, 68, 68, 0.10);
            border: 1px solid rgba(239, 68, 68, 0.25);
        }

        .match-banner {
            border-radius: 22px;
            padding: 1.2rem 1.3rem;
            margin-bottom: 1.2rem;
            border: 1px solid rgba(148,163,184,0.14);
            background: #121a2b;
        }

        .match-strong {
            border-left: 4px solid #22c55e;
        }

        .match-good {
            border-left: 4px solid #3b82f6;
        }

        .match-weak {
            border-left: 4px solid #ef4444;
        }

        h4 {
            color: #ffffff !important;
            margin-bottom: 0.35rem !important;
        }

        hr {
            border-color: rgba(148,163,184,0.12) !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
