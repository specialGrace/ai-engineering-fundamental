<p align="center">
  <img src="../assets/ormedian_logo.png" alt="Ormedian" width="300" />
</p>

# Week 1 independent assignment

## Goal

Turn Sunday's guided work into an experiment you can run and explain independently.

The assignment is not complete merely because a notebook produces a score. It must show that you understand the problem, data, split, baseline, evaluation and errors.

## Required deliverables

### 1. Completed assignment notebook

Complete `notebooks/02_week_1_assignment.ipynb` from top to bottom.

It must include:

- A problem statement in your own words.
- Input, output, user and costly mistake.
- Dataset size and class distribution.
- Missing-value and duplicate checks.
- Train, validation and test counts.
- Majority baseline.
- TF-IDF plus logistic-regression model.
- Accuracy, macro F1 and classification report.
- Confusion matrix.
- At least three wrong predictions with comments.
- One controlled experiment.
- A final conclusion and next step.

### 2. Reflection answers

Copy `docs/REFLECTION_QUESTIONS.md` into a file named `reflection.md` and answer every core question in your own words.

### 3. Paper notes

Read selected parts of Pedro Domingos, *A Few Useful Things to Know About Machine Learning*, using `docs/PAPER_READING_GUIDE.md`.

Record:

- Five takeaways.
- Two unfamiliar terms.
- One idea that changed your view.
- One question for Sunday.

### 4. Learning log

Use `docs/LEARNING_LOG_TEMPLATE.md` for each work session during the week.

### 5. Reproducibility evidence

From the repository root, run:

```bash
python -m pytest -q
python -m src.train --experiment unigram --output-dir results/my_unigram_run
python -m src.train --experiment bigram --output-dir results/my_bigram_run
```

Record the validation and test macro F1 from each run.

---

## Controlled experiment

Change exactly one main variable. Recommended experiment:

```text
Baseline model features: unigrams, ngram_range=(1, 1)
Experiment features: unigrams and bigrams, ngram_range=(1, 2)
```

Keep fixed:

- Dataset.
- Train, validation and test split.
- Classifier type.
- Metrics.
- Random seed.

Write the experiment before running it:

```markdown
## Question
Will including two-word phrases improve validation macro F1?

## Hypothesis
I expect ... because ...

## Change
Only ngram_range changes from (1, 1) to (1, 2).

## Result
Baseline macro F1: ...
Experiment macro F1: ...

## Interpretation
...
```

A result that does not improve is still useful when it is recorded honestly.

---

## Error-analysis table

Use a table like this:

| Text | True label | Predicted label | Why might the model have failed? | Suggested improvement |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Possible causes:

- Ambiguous wording.
- Too few similar examples in training.
- Overlapping vocabulary between labels.
- Incorrect or debatable label.
- Class definition is too broad.
- Useful phrase not represented by unigram features.

Do not simply write "the model is wrong".

---

## Marking rubric

Total: 100 points.

| Area | Points | Evidence |
|---|---:|---|
| Problem framing | 10 | Clear input, output, user, costly mistakes and metric |
| Data understanding | 15 | Counts, distributions, quality checks and schema explanation |
| Split discipline | 10 | Correct use and explanation of train, validation and test |
| Baseline | 10 | Majority baseline implemented and interpreted |
| Model implementation | 15 | Correct TF-IDF and logistic-regression pipeline |
| Evaluation | 15 | Accuracy, macro F1, class report and confusion matrix |
| Error analysis | 10 | At least three thoughtful examples |
| Controlled experiment | 10 | One variable changed and result interpreted |
| Communication and reproducibility | 5 | Notebook reads clearly and runs in order |

### Completion threshold

- 70 or above.
- No missing core section.
- All submitted code can be explained.
- No test-set tuning.

---

## Submission checklist

- [ ] Notebook runs from a fresh kernel using **Run All**.
- [ ] No absolute paths such as `/home/myname/...`.
- [ ] No secret keys or personal data.
- [ ] Markdown explains each major code section.
- [ ] Results are recorded, not merely printed and forgotten.
- [ ] Wrong predictions are inspected.
- [ ] One change is compared fairly with the baseline.
- [ ] Reflection and paper notes are complete.
- [ ] Git commits are small and understandable.

## Oral review next Sunday

Be prepared to answer:

1. What did your model use as input?
2. What did it learn during training?
3. Why is the test set different from validation?
4. Which class was hardest and why?
5. What changed in your experiment?
6. What evidence supports your conclusion?
7. What would you improve next if given one more week?
