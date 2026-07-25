# Data card: Ormedian support-intent teaching dataset

## Summary

This is a synthetic text-classification dataset for Session 1 of Ormedian AI Engineering Fundamentals. It contains 180 clean examples across six support intents, with fixed train, validation and test assignments.

## Intended use

- Teaching supervised classification.
- Demonstrating data validation and cleaning.
- Comparing a majority baseline with TF-IDF and logistic regression.
- Practising classification metrics, confusion matrices and error analysis.
- Rehearsing reproducible project structure before work on a real repository.

## Not intended for

- Production customer support.
- Measuring real-world language coverage.
- Benchmarking commercial systems.
- Training a safety-critical routing system.
- Making claims about demographic or regional fairness.

## Labels

| Label | Meaning |
|---|---|
| `refund_request` | The user wants money returned or asks about a refund. |
| `cancel_order` | The user wants an order, subscription, booking or service cancelled. |
| `invoice_status` | The user asks whether an invoice or payment is open, paid or overdue. |
| `technical_support` | The user reports an access, application or website problem. |
| `account_update` | The user wants personal, contact or organisational details changed. |
| `general_enquiry` | The user asks a broad question about plans, features or service. |

## Size and splits

- Total clean examples: 180
- Classes: 6
- Training examples: 120
- Validation examples: 30
- Test examples: 30
- Examples per class: 30

The fixed split prevents different learners from obtaining different results merely because of random sampling.

## Data creation

Examples were manually curated and are synthetic. They do not represent real customers, real tickets or private information. Phrases were varied to include direct wording, paraphrases and some intentionally ambiguous cases.

## Known limitations

1. The dataset is very small.
2. Language is mostly standard British English.
3. The class distribution is perfectly balanced, unlike many real support datasets.
4. Synthetic wording is cleaner than real messages.
5. It does not cover code-switching, regional dialects, long conversations or attachments.
6. Labels are mutually exclusive even though real messages may contain several intents.
7. There is no demographic information, so subgroup fairness cannot be evaluated.

## Quality checks

The processed dataset must satisfy:

- Required columns are present.
- Text is non-empty.
- Labels belong to the known label set.
- Split values are `train`, `validation` or `test`.
- Exact text-label duplicates are absent.
- Every split is represented.

## Privacy and security

No real personal data is included. A production version should still consider:

- Removal or masking of names, addresses, account numbers and payment details.
- Access controls for ticket data.
- Retention limits.
- Audit logs for training-data changes.
- Protection against malicious or sensitive input.
- Human review for high-impact routing decisions.

## Maintenance

When examples are added, record the reason, source, label decision and intended split. Never add test examples to training merely to improve the score; that would invalidate the evaluation.
