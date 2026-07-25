"""Simple model builders used in the Session 1 notebooks and CLI."""

from __future__ import annotations

from sklearn.dummy import DummyClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


def build_majority_baseline() -> DummyClassifier:
    """Predict the most frequent training label for every example."""
    return DummyClassifier(strategy="most_frequent")


def build_text_model(
    *,
    ngram_range: tuple[int, int] = (1, 1),
    min_df: int = 1,
    c: float = 1.0,
    class_weight: str | dict[str, float] | None = None,
) -> Pipeline:
    """Build a TF-IDF plus logistic-regression text classifier.

    Parameters are exposed because the Week 1 experiment changes one thing at a
    time. The default is intentionally simple and forms the first real model.
    """
    return Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    lowercase=True,
                    ngram_range=ngram_range,
                    min_df=min_df,
                    sublinear_tf=True,
                ),
            ),
            (
                "classifier",
                LogisticRegression(
                    C=c,
                    class_weight=class_weight,
                    max_iter=1_000,
                    random_state=42,
                ),
            ),
        ]
    )
