## Introduction

Raj shares the `pre-commit` hook script with his team. Two weeks later, a colleague pushes a commit with a long line of dead code. It turns out she never installed the hook. The `.git/hooks/` directory is not tracked by git, so the hook only exists on Raj's machine.

The `pre-commit` framework solves this with a single committed configuration file: `.pre-commit-config.yaml`. It defines which hooks to run, where to download them from, and which version to use. Any developer who runs `pre-commit install` gets the exact same hooks.

![A repository with .pre-commit-config.yaml checked in, and three developers each running pre-commit install to get identical hooks on their machines](images/06_precommit_framework.png)

## Installing the pre-commit Framework

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-06-precommit-framework-001-22dbace986.html"
 width="100%"
></iframe>

## Creating .pre-commit-config.yaml

The configuration file lives at the project root and is committed to the repository:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.4.4      # pin to a specific version
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format   # ruff's black-compatible formatter

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-merge-conflict
```

## Installing Hooks for Developers

After cloning the repository, each developer runs:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-06-precommit-framework-002-7bd4bfc101.html"
 width="100%"
></iframe>

This installs the hooks into `.git/hooks/pre-commit` (and other hook types if configured). Now every `git commit` runs the configured hooks automatically.

## Running Manually

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-06-precommit-framework-003-f24c7374a4.html"
 width="100%"
></iframe>

`pre-commit run --all-files` is useful when first adding hooks to a project: it finds all existing violations at once.

## What Happens on a Commit

When a developer runs `git commit`:

1. `pre-commit` identifies the staged files
2. It runs each configured hook against those files
3. If a hook modifies files (e.g., `ruff --fix` removes unused imports), the files are modified but NOT re-staged automatically
4. Git shows "hook modified files" and aborts the commit
5. The developer runs `git add` to re-stage the changed files and commits again

Some teams configure hooks to auto-stage fixes with `always_run: true` and a `git add` step, but the default behavior (fail on modification) is safer.

## Keeping Hooks Updated

Hook versions are pinned in the config file. To update them to the latest versions:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-06-precommit-framework-004-a04d30078a.html"
 width="100%"
></iframe>

This updates the `rev` field in `.pre-commit-config.yaml` to the latest tagged version for each repo. Commit the updated file so all developers get the same version.

## The pre-commit Framework at a Glance

| Command | What it does |
|---|---|
| `pre-commit install` | Install hooks from `.pre-commit-config.yaml` |
| `pre-commit run --all-files` | Run all hooks on all files |
| `pre-commit run ruff` | Run one specific hook |
| `pre-commit autoupdate` | Update hook versions in config |
| `.pre-commit-config.yaml` | Version-controlled hook configuration |

## Your Turn

Initialize the `pre-commit` framework in your library project:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-06-precommit-framework-005-af591fda10.html"
 width="100%"
></iframe>

Create `.pre-commit-config.yaml` with at least two hooks from the examples above. Then run:

<iframe
 frameBorder="0"
 height="350px"
 src="https://s3.ap-south-1.amazonaws.com/static.bytexl.app/uploads/44sjn9mdv/content/onecompiler-embeds/semester-2-unit-9-code-quality-and-pre-commit-hooks-06-precommit-framework-006-9a98dbbefb.html"
 width="100%"
></iframe>

Fix any issues found, commit the `.pre-commit-config.yaml` file, and test that the hooks run automatically on your next `git commit`.

## Conclusion

The `pre-commit` framework version-controls hook configuration, ensuring every developer gets the same hooks with the same settings. `pre-commit install` sets up hooks locally; `pre-commit run --all-files` finds all existing violations; `pre-commit autoupdate` keeps hook versions current. The next lesson shows how to configure these hooks in detail and add project-specific checks like mypy.
