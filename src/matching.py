from __future__ import annotations

from typing import Tuple

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from .config import GOOD_MATCH_THRESHOLD, STRONG_MATCH_THRESHOLD


def semantic_similarity(text_a: str, text_b: str, embedding_model: SentenceTransformer) -> float:
    embeddings = embedding_model.encode([text_a, text_b], normalize_embeddings=True)
    return float(cosine_similarity([embeddings[0]], [embeddings[1]])[0][0])


def classify_match(similarity: float) -> Tuple[str, str, str]:
    if similarity >= STRONG_MATCH_THRESHOLD:
        return (
            "Strong Match",
            "match-strong",
            "The candidate profile aligns well with the technical and contextual signals in the job description.",
        )

    if similarity >= GOOD_MATCH_THRESHOLD:
        return (
            "Good Match",
            "match-good",
            "There is clear alignment, with a few noticeable gaps that may require targeted upskilling or stronger evidence in the resume.",
        )

    return (
        "Weak Match",
        "match-weak",
        "The resume currently shows limited alignment with the required capabilities and position context in the job description.",
    )
