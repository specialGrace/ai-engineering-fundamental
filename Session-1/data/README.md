# Dataset directory

The dataset is a small, synthetic collection of support messages created solely for teaching.

## Files

- `raw/support_intents_raw.csv`: deliberately imperfect input used for data-quality checks.
- `processed/support_intents.csv`: cleaned and validated data used for modelling.
- `DATA_CARD.md`: purpose, schema, limitations and responsible-use notes.

## Schema

| Column | Meaning | Used as a model feature? |
|---|---|---|
| `example_id` | Stable identifier for the example | No |
| `text` | Support message | Yes |
| `label` | Correct intent | Target, not an input feature |
| `split` | Train, validation or test assignment | No |
| `difficulty` | Teaching metadata | No |
| `source` | How the example was created | No |

Using `label`, `split` or a label-derived field as an input would create data leakage.
