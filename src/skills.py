from __future__ import annotations

import re
from typing import List, Set

from .config import (
    ALLOWED_SHORT_SKILLS,
    CANONICAL_SKILLS,
    GENERIC_EXCLUDE,
    REQUIRED_CUES,
    SKILL_PATTERNS,
    SKILL_SYNONYMS,
)
from .text_processing import clean_text


def canonicalize_skill(raw_skill: str) -> str:
    token = raw_skill.strip().lower()
    token = re.sub(r"\s+", " ", token)
    token = token.replace("##", "")
    if token in SKILL_SYNONYMS:
        return SKILL_SYNONYMS[token]
    return token.title()


def extract_pattern_skills(text: str) -> Set[str]:
    lowered = text.lower()
    hits: Set[str] = set()
    for pattern in SKILL_PATTERNS:
        for match in re.finditer(pattern, lowered, flags=re.IGNORECASE):
            hits.add(canonicalize_skill(match.group(0)))
    return hits


def extract_ner_skills(text: str, ner_pipeline) -> Set[str]:
    if not text.strip():
        return set()

    max_chars = 3000
    chunks = [text[i : i + max_chars] for i in range(0, len(text), max_chars)]
    skills: Set[str] = set()

    known_aliases = {key.lower() for key in SKILL_SYNONYMS.keys()}
    known_canonical = set(SKILL_SYNONYMS.values()) | set(CANONICAL_SKILLS)

    for chunk in chunks:
        results = ner_pipeline(chunk)
        if not results:
            continue

        for ent in results:
            word = ent.get("word", "").replace("##", "").strip()
            score = float(ent.get("score", 0))

            if not word:
                continue

            normalized = canonicalize_skill(word)
            lowered = normalized.lower()

            if score < 0.85:
                continue
            if lowered in GENERIC_EXCLUDE:
                continue
            if len(lowered) <= 2 and lowered not in ALLOWED_SHORT_SKILLS:
                continue
            if lowered in known_aliases or normalized in known_canonical:
                skills.add(normalized)

    return skills


def find_requirement_sentences(text: str) -> str:
    sentences = re.split(r"(?<=[\.!?])\s+|\n+", text)
    selected = [
        sentence
        for sentence in sentences
        if any(cue in sentence.lower() for cue in REQUIRED_CUES)
    ]
    return " ".join(selected)


def extract_dictionary_skills(text: str) -> Set[str]:
    cleaned = clean_text(text).lower()
    found: Set[str] = set()

    for alias, canonical in SKILL_SYNONYMS.items():
        if re.search(rf"(?<!\w){re.escape(alias.lower())}(?!\w)", cleaned):
            found.add(canonical)

    for skill in CANONICAL_SKILLS:
        if re.search(rf"(?<!\w){re.escape(skill.lower())}(?!\w)", cleaned):
            found.add(skill)

    return found


def extract_skills(text: str, ner_pipeline, use_requirement_focus: bool = False) -> List[str]:
    cleaned = clean_text(text)
    scoped_text = cleaned

    if use_requirement_focus:
        requirement_zone = find_requirement_sentences(text)
        if requirement_zone.strip():
            scoped_text = clean_text(requirement_zone)

    dict_skills = extract_dictionary_skills(scoped_text)
    pattern_skills = extract_pattern_skills(scoped_text)
    ner_skills = extract_ner_skills(scoped_text, ner_pipeline)

    skills = dict_skills | pattern_skills | ner_skills
    return sorted(skills)
