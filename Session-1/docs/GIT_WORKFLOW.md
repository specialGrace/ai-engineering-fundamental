# Beginner Git workflow for Week 1

## 1. Check the repository state

```bash
git status
```

Read the output before changing anything.

## 2. Create a branch

```bash
git switch -c learning/week-1-assignment
```

## 3. Work in small steps

After one meaningful improvement:

```bash
git status
git diff
```

Stage only the files you understand:

```bash
git add notebooks/02_week_1_assignment.ipynb
git add reflection.md
```

Commit with a descriptive message:

```bash
git commit -m "Complete data-quality checks and baseline evaluation"
```

## 4. Run checks before sharing

```bash
python -m pytest -q
```

Restart the notebook kernel and select **Run All**. A notebook that only works because cells were executed out of order is not reproducible.

## 5. Push the branch

```bash
git push -u origin learning/week-1-assignment
```

## 6. Open a draft pull request

Describe:

- What changed.
- Why it changed.
- How it was tested.
- What the result was.
- What remains unclear.

## Notebook caution

Jupyter notebooks store code, Markdown and outputs in one JSON file. This can create noisy diffs. Keep output concise, avoid huge tables and restart-and-run-all before committing.

## Never commit

- `.venv/`
- API keys or passwords
- Private customer data
- Large generated models unless requested
- Temporary cache files
- Code you cannot explain
