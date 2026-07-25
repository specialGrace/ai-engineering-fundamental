"""Command-line training entry point for the Session 1 classifier."""

from __future__ import annotations

import argparse
from pathlib import Path

import joblib
import pandas as pd

from src.data import dataset_summary, get_splits, load_dataset, validate_dataset
from src.evaluation import (
    classification_metrics,
    error_frame,
    save_confusion_matrix,
    save_json,
)
from src.modelling import build_majority_baseline, build_text_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train and evaluate the Ormedian Session 1 text classifier."
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=Path("data/processed/support_intents.csv"),
        help="Path to the clean CSV dataset.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("results/session_1"),
        help="Directory for model artefacts, metrics and predictions.",
    )
    parser.add_argument(
        "--experiment",
        choices=("unigram", "bigram"),
        default="unigram",
        help="Feature configuration to run.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    data = load_dataset(args.data)
    validate_dataset(data)
    train, validation, test = get_splits(data)

    baseline = build_majority_baseline()
    baseline.fit(train[["text"]], train["label"])
    baseline_pred = baseline.predict(validation[["text"]])
    baseline_metrics = classification_metrics(validation["label"], baseline_pred)

    ngram_range = (1, 1) if args.experiment == "unigram" else (1, 2)
    model = build_text_model(ngram_range=ngram_range)
    model.fit(train["text"], train["label"])

    validation_pred = model.predict(validation["text"])
    validation_metrics = classification_metrics(validation["label"], validation_pred)

    # Test is used once here as the final report for this fixed experiment.
    test_pred = model.predict(test["text"])
    test_metrics = classification_metrics(test["label"], test_pred)

    payload = {
        "experiment": args.experiment,
        "ngram_range": list(ngram_range),
        "dataset": dataset_summary(data),
        "baseline_validation": baseline_metrics,
        "model_validation": validation_metrics,
        "model_test": test_metrics,
    }
    save_json(payload, args.output_dir / "metrics.json")

    errors = error_frame(test["text"], test["label"], test_pred)
    errors.to_csv(args.output_dir / "test_errors.csv", index=False)

    predictions = pd.DataFrame(
        {
            "text": test["text"],
            "true_label": test["label"],
            "predicted_label": test_pred,
        }
    )
    predictions.to_csv(args.output_dir / "test_predictions.csv", index=False)

    labels = sorted(data["label"].unique())
    save_confusion_matrix(
        test["label"],
        test_pred,
        labels,
        args.output_dir / "confusion_matrix.png",
        title=f"Session 1 test confusion matrix ({args.experiment})",
    )
    joblib.dump(model, args.output_dir / "model.joblib")

    print(f"Experiment: {args.experiment}")
    print(f"Validation macro F1: {validation_metrics['macro_f1']:.3f}")
    print(f"Test macro F1: {test_metrics['macro_f1']:.3f}")
    print(f"Test errors: {len(errors)}")
    print(f"Artefacts written to: {args.output_dir}")


if __name__ == "__main__":
    main()
