"""Data loading, cleaning and validation helpers for Session 1.

The functions are deliberately small and explicit so a beginner can read them.
They are not intended to be a general-purpose data framework.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

REQUIRED_COLUMNS = {
    "example_id",
    "text",
    "label",
    "split",
    "difficulty",
    "source",
}

ALLOWED_LABELS = {
    "refund_request",
    "cancel_order",
    "invoice_status",
    "technical_support",
    "account_update",
    "general_enquiry",
}

ALLOWED_SPLITS = {"train", "validation", "test"}


def load_dataset(path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset and preserve blank strings for explicit validation."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    return pd.read_csv(path, keep_default_na=False)


def clean_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, int]]:
    """Clean common beginner-level data problems.

    Operations:
    1. Strip whitespace from text labels and split names.
    2. Remove rows with blank text.
    3. Remove rows with labels outside the known label set.
    4. Remove exact duplicate text-label pairs.

    Returns the cleaned frame plus a report of what changed.
    """
    cleaned = df.copy()
    before = len(cleaned)

    for column in ("text", "label", "split"):
        if column in cleaned.columns:
            cleaned[column] = cleaned[column].astype(str).str.strip()

    blank_mask = cleaned["text"].eq("")
    blank_count = int(blank_mask.sum())
    cleaned = cleaned.loc[~blank_mask].copy()

    invalid_label_mask = ~cleaned["label"].isin(ALLOWED_LABELS)
    invalid_label_count = int(invalid_label_mask.sum())
    cleaned = cleaned.loc[~invalid_label_mask].copy()

    duplicate_mask = cleaned.duplicated(subset=["text", "label"], keep="first")
    duplicate_count = int(duplicate_mask.sum())
    cleaned = cleaned.loc[~duplicate_mask].copy()

    cleaned = cleaned.reset_index(drop=True)
    report = {
        "rows_before": before,
        "blank_text_removed": blank_count,
        "invalid_labels_removed": invalid_label_count,
        "duplicates_removed": duplicate_count,
        "rows_after": len(cleaned),
    }
    return cleaned, report


def validate_dataset(df: pd.DataFrame) -> None:
    """Raise a clear error when the dataset does not meet the session contract."""
    missing_columns = REQUIRED_COLUMNS - set(df.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    if df.empty:
        raise ValueError("The dataset is empty.")

    if df["text"].astype(str).str.strip().eq("").any():
        raise ValueError("The dataset contains blank text values.")

    invalid_labels = sorted(set(df["label"]) - ALLOWED_LABELS)
    if invalid_labels:
        raise ValueError(f"Unknown labels found: {invalid_labels}")

    invalid_splits = sorted(set(df["split"]) - ALLOWED_SPLITS)
    if invalid_splits:
        raise ValueError(f"Unknown split values found: {invalid_splits}")

    duplicate_count = int(df.duplicated(subset=["text", "label"]).sum())
    if duplicate_count:
        raise ValueError(f"Found {duplicate_count} duplicate text-label pairs.")

    missing_splits = ALLOWED_SPLITS - set(df["split"])
    if missing_splits:
        raise ValueError(f"Missing required splits: {sorted(missing_splits)}")


def dataset_summary(df: pd.DataFrame) -> dict[str, Any]:
    """Return a compact, serialisable summary for logs and reports."""
    return {
        "n_examples": int(len(df)),
        "n_labels": int(df["label"].nunique()),
        "class_distribution": {
            str(k): int(v) for k, v in df["label"].value_counts().sort_index().items()
        },
        "split_distribution": {
            str(k): int(v) for k, v in df["split"].value_counts().sort_index().items()
        },
        "blank_text": int(df["text"].astype(str).str.strip().eq("").sum()),
        "duplicate_text_label_pairs": int(
            df.duplicated(subset=["text", "label"]).sum()
        ),
        "average_text_length_characters": float(df["text"].str.len().mean()),
    }


def get_splits(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Return train, validation and test frames from the fixed split column."""
    validate_dataset(df)
    train = df.loc[df["split"].eq("train")].reset_index(drop=True)
    validation = df.loc[df["split"].eq("validation")].reset_index(drop=True)
    test = df.loc[df["split"].eq("test")].reset_index(drop=True)
    return train, validation, test
