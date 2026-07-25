from pathlib import Path

from src.data import get_splits, load_dataset
from src.evaluation import classification_metrics
from src.modelling import build_text_model

ROOT = Path(__file__).resolve().parents[1]


def test_model_returns_one_prediction_per_example() -> None:
    data = load_dataset(ROOT / "data" / "processed" / "support_intents.csv")
    train, validation, _ = get_splits(data)
    model = build_text_model()
    model.fit(train["text"], train["label"])
    predictions = model.predict(validation["text"])
    assert len(predictions) == len(validation)


def test_model_beats_a_low_learning_threshold() -> None:
    data = load_dataset(ROOT / "data" / "processed" / "support_intents.csv")
    train, validation, _ = get_splits(data)
    model = build_text_model()
    model.fit(train["text"], train["label"])
    predictions = model.predict(validation["text"])
    metrics = classification_metrics(validation["label"], predictions)
    # This is a smoke test, not a claim that 0.50 is production quality.
    assert metrics["macro_f1"] >= 0.50
