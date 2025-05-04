# CI/CD Assignment:

# Workflow with GitHub Actions
## Objective

> Set up a GitHub Actions workflow that lints your code on each push. Demonstrate that the workflow correctly fails when code has linting issues and passes when the issues are resolved.

### Instructions

> * Create a GitHub Repository
>   - Use Python (recommended) or another language that supports linting tools.
>   - Add at least one source file (e.g., main.py).
> * Set Up GitHub Actions
> * In your repo, create a file at .github/workflows/ci.yml with a workflow that:
>   - Runs on every push
>   - Installs and runs a linter (flake8, pylint, etc.)
> 
> ### Example for Python:
> 
> ```console
> name: CI
>  
> on: [push]
>  
> jobs:
>   lint:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v3
>       - uses: actions/setup-python@v4
>         with:
>           python-version: '3.11'
>       - name: Install flake8
>         run: pip install flake8
>       - name: Run flake8
>         run: flake8 .
> ```
> 
> * Trigger Two Runs
>   - One failing run: Commit and push code with a linting error.
>   - One passing run: Fix the code and push again.

## What to Submit

> * A single link to your workflow run history, like:
> * https://github.com/<your-username>/<your-repo>/actions/workflows/ci.yml
> * Make sure the run history shows at least one failed and one successful lint run.