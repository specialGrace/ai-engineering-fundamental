# Troubleshooting guide

## `python: command not found`

Try:

```bash
python3 --version
```

Use `python3` in place of `python` when creating the environment.

## Environment does not activate

Ubuntu or macOS:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Your prompt will often show `(.venv)` after activation.

## `ModuleNotFoundError`

Confirm the environment is active, then install dependencies:

```bash
python -m pip install -r requirements.txt
```

Check which Python is running:

```bash
which python
python -m pip --version
```

On Windows:

```powershell
where.exe python
python -m pip --version
```

## Dataset file not found

Run Jupyter from the repository root:

```bash
cd ormedian-ai-engineering-fundamentals-session-1
python -m jupyter lab
```

The notebooks also contain root-detection code, but starting from the root is the clearest habit.

## Notebook cells were run out of order

Use:

1. **Kernel -> Restart Kernel**
2. **Run -> Run All Cells**

Then fix the first failing cell rather than running later cells manually.

## Logistic regression convergence warning

The supplied model uses `max_iter=1000`, which should be sufficient. If a modified experiment warns about convergence:

- Confirm the data is correct.
- Increase `max_iter` modestly.
- Do not hide the warning without understanding it.

## Classification report warning about undefined metrics

A class may have no predicted examples. Use `zero_division=0` for a readable report, but investigate why the model never predicted that class.

## Confusion-matrix labels look crowded

Increase the figure size or rotate tick labels. Do not remove class names merely to make the chart prettier.

## Test failure

Run the specific test with more detail:

```bash
python -m pytest tests/test_data.py -vv
```

Read from the first failure. Later failures may be consequences of the first one.

## Git shows many notebook changes

Restart and run all cells, save, and inspect the diff. Avoid repeatedly opening the notebook with different tools that rewrite metadata.

## Asking for help

Use this format:

```text
Goal:
Expected:
Actual:
What I tried:
Full error:
Relevant file and cell:
```
