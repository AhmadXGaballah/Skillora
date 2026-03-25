from __future__ import annotations

from typing import List, Optional, Tuple
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from .config import REQUEST_TIMEOUT
from .text_processing import normalize_whitespace


def fetch_job_description_from_url(url: str) -> Tuple[str, Optional[str]]:
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"
        ),
        "Accept-Language": "en-US,en;q=0.9",
    }

    response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    for tag in soup(["script", "style", "noscript", "svg", "img", "header", "footer", "nav", "form"]):
        tag.decompose()

    title = soup.title.get_text(" ", strip=True) if soup.title else None

    selectors = [
        "article",
        "main",
        "section",
        "div[class*='description']",
        "div[class*='job']",
        "div[id*='description']",
        "div[id*='job']",
    ]

    candidate_texts: List[str] = []
    for selector in selectors:
        for element in soup.select(selector):
            text = element.get_text(" ", strip=True)
            if len(text) > 300:
                candidate_texts.append(text)

    if not candidate_texts:
        candidate_texts.append(soup.get_text(" ", strip=True))

    best_text = max(candidate_texts, key=len)
    return normalize_whitespace(best_text), title


def prepare_job_description(
    job_link: str,
    job_description: str,
) -> Tuple[str, Optional[str], Optional[str]]:
    """
    Returns: jd_text, job_title, source_label
    """
    job_description = normalize_whitespace(job_description)
    job_link = job_link.strip()

    if job_description:
        source_label = "Pasted description"
        job_title = None
        if job_link:
            source_label = f"Pasted description + reference link ({urlparse(job_link).netloc or 'job post'})"
        return job_description, job_title, source_label

    if job_link:
        jd_text, job_title = fetch_job_description_from_url(job_link)
        source_label = f"Fetched from {urlparse(job_link).netloc or 'job post link'}"
        return jd_text, job_title, source_label

    raise ValueError("Please provide either a job description or a job post link.")
