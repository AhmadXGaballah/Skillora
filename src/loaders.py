from __future__ import annotations

import streamlit as st
from sentence_transformers import SentenceTransformer
from transformers import AutoModelForTokenClassification, AutoTokenizer, pipeline

from .config import EMBEDDING_MODEL_NAME, SKILL_NER_MODEL_NAME


@st.cache_resource(show_spinner=False)
def load_embedding_model() -> SentenceTransformer:
    return SentenceTransformer(EMBEDDING_MODEL_NAME)


@st.cache_resource(show_spinner=False)
def load_skill_ner_pipeline():
    tokenizer = AutoTokenizer.from_pretrained(SKILL_NER_MODEL_NAME)
    ner_model = AutoModelForTokenClassification.from_pretrained(SKILL_NER_MODEL_NAME)

    ner = pipeline(
        "ner",
        model=ner_model,
        tokenizer=tokenizer,
        aggregation_strategy="simple",
    )

    if ner is None or not callable(ner):
        raise RuntimeError("Failed to initialize the skill NER pipeline.")

    return ner
