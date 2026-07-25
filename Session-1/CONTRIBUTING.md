<p align="center">
  <img src="assets/ormedian_logo.png" alt="Ormedian" width="320" />
</p>

# Contributing to the Session 1 repository

This project is also a rehearsal for future Scaggle tickets. Contributions should therefore be small, testable and easy to review.

## Branch naming

Create one branch per task:

```bash
git switch -c learning/add-error-analysis
```

Suggested prefixes:

- `learning/` for an exercise or educational improvement
- `fix/` for a defect
- `docs/` for documentation only
- `test/` for test improvements

## Commit discipline

Prefer several understandable commits over one giant commit.

Good examples:

```text
Add class-distribution check to notebook
Explain why test data must remain unseen
Add test for duplicate text-label pairs
Record unigram and bigram comparison
```

Avoid messages such as `changes`, `stuff`, `final` or `fix everything`.

## Before opening a pull request

Run:

```bash
python -m pytest -q
python -m src.train --experiment unigram --output-dir results/session_1
```

Then check:

- The notebook runs from top to bottom.
- New code has comments where the reason is not obvious.
- Generated files have not been committed accidentally.
- The README or relevant documentation has been updated.
- You can explain every submitted line.

## Pull-request description

Use this structure:

```markdown
## What changed

## Why it changed

## How I tested it

## Result

## What I learned

## Questions or limitations
```

A draft pull request is encouraged. It makes work visible early and allows review before the change becomes too large.
