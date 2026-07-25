"""Evaluation helpers for classification experiments."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Sequence

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import (
    ConfusionMatrixDisplay,
    accuracy_score,
    classification_report,
    f1_score,
)


def classification_metrics(
    y_true: Sequence[str], y_pred: Sequence[str]
) -> dict[str, Any]:
    """Return headline metrics and a per-class report in JSON-friendly form."""
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro")),
        "weighted_f1": float(f1_score(y_true, y_pred, average="weighted")),
        "classification_report": classification_report(
            y_true, y_pred, output_dict=True, zero_division=0
        ),
    }


def error_frame(
    texts: Sequence[str], y_true: Sequence[str], y_pred: Sequence[str]
) -> pd.DataFrame:
    """Build a table containing only incorrect predictions."""
    frame = pd.DataFrame(
        {"text": list(texts), "true_label": list(y_true), "predicted_label": list(y_pred)}
    )
    return frame.loc[frame["true_label"].ne(frame["predicted_label"])].reset_index(
        drop=True
    )


def save_json(payload: dict[str, Any], path: str | Path) -> None:
    """Write a dictionary as readable JSON."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def save_confusion_matrix(
    y_true: Sequence[str],
    y_pred: Sequence[str],
    labels: Sequence[str],
    path: str | Path,
    *,
    title: str = "Confusion matrix",
) -> None:
    """Save a confusion matrix image without using seaborn."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(9, 7))
    ConfusionMatrixDisplay.from_predictions(
        y_true,
        y_pred,
        labels=list(labels),
        xticks_rotation=45,
        values_format="d",
        ax=ax,
        colorbar=False,
    )
    ax.set_title(title)
    fig.tight_layout()
    fig.savefig(path, dpi=160, bbox_inches="tight")
    plt.close(fig)
