from pathlib import Path

from src.data import clean_dataset, get_splits, load_dataset, validate_dataset

ROOT = Path(__file__).resolve().parents[1]


def test_clean_processed_dataset_is_valid() -> None:
    data = load_dataset(ROOT / "data" / "processed" / "support_intents.csv")
    validate_dataset(data)
    assert len(data) == 180
    assert data["label"].nunique() == 6


def test_raw_dataset_cleaning_removes_known_issues() -> None:
    raw = load_dataset(ROOT / "data" / "raw" / "support_intents_raw.csv")
    cleaned, report = clean_dataset(raw)
    validate_dataset(cleaned)
    assert report["blank_text_removed"] == 1
    assert report["invalid_labels_removed"] == 1
    assert report["duplicates_removed"] == 3
    assert len(cleaned) == 180


def test_fixed_splits_have_expected_sizes() -> None:
    data = load_dataset(ROOT / "data" / "processed" / "support_intents.csv")
    train, validation, test = get_splits(data)
    assert len(train) == 120
    assert len(validation) == 30
    assert len(test) == 30
