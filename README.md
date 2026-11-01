# Gitflow Simulation – Python Task Manager

## Project Description
A Python-based Task Manager developed to demonstrate Git and GitHub workflows, including Gitflow branching, collaboration practices, automation, and continuous integration.

## Features
- Add new tasks
- Mark tasks as completed
- Display all tasks
- Validate task inputs
- Automated unit testing using pytest
- Git hooks for pre-commit, commit-msg, and pre-push checks
- GitHub Actions CI pipeline

## Technologies Used
- Python
- Git
- GitHub
- Pytest
- GitHub Actions
- YAML

## Project Structure

    week7-8-gitflow-simulation/
    ├── .github/
    │   └── workflows/
    │       └── ci.yml
    ├── hooks/
    │   ├── pre-commit
    │   ├── commit-msg
    │   └── pre-push
    ├── src/
    │   ├── __init__.py
    │   └── app.py
    ├── tests/
    │   └── test_app.py
    ├── requirements.txt
    ├── .gitignore
    └── README.md

## Git Concepts Covered
- Repository initialization and cloning
- Staging, committing, pushing, and pulling
- Branching and merging
- Merge conflict resolution
- Git stash
- Pull requests and code reviews
- Rebase and interactive rebase
- Cherry-pick
- Git bisect and reflog
- Git worktree
- Git hooks
- Gitflow branching strategy
- Submodules and subtrees
- GPG-signed commits
- GitHub Actions CI

## How to Run

1. Install Python.
2. Install dependencies using `pip install -r requirements.txt`.
3. Run the application using `python -m src.app`.
4. Run tests using `python -m pytest -v`.

## GitHub Actions
The CI workflow automatically runs unit tests when code is pushed or a pull request is created for the main and develop branches.

## Learning Outcomes
- Understand professional Git workflows.
- Practise Gitflow branch management.
- Learn code quality checks using Git hooks.
- Automate testing using GitHub Actions.
- Understand collaborative development practices.

## Author
Sameer Honnatti