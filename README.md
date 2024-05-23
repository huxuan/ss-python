# Serious Scaffold Python

An evolving Python project template that covers the full development lifecycle.

[![CI](https://github.com/serious-scaffold/ss-python/actions/workflows/ci.yml/badge.svg)](https://github.com/serious-scaffold/ss-python/actions/workflows/ci.yml)
[![CommitLint](https://github.com/serious-scaffold/ss-python/actions/workflows/commitlint.yml/badge.svg)](https://github.com/serious-scaffold/ss-python/actions/workflows/commitlint.yml)
[![DevContainer](https://github.com/serious-scaffold/ss-python/actions/workflows/devcontainer.yml/badge.svg)](https://github.com/serious-scaffold/ss-python/actions/workflows/devcontainer.yml)
[![Release](https://github.com/serious-scaffold/ss-python/actions/workflows/release.yml/badge.svg)](https://github.com/serious-scaffold/ss-python/actions/workflows/release.yml)
[![Renovate](https://github.com/serious-scaffold/ss-python/actions/workflows/renovate.yml/badge.svg)](https://github.com/serious-scaffold/ss-python/actions/workflows/renovate.yml)
[![Coverage](https://img.shields.io/endpoint?url=https://serious-scaffold.github.io/ss-python/_static/badges/coverage.json)](https://serious-scaffold.github.io/ss-python/reports/coverage)
[![Release](https://img.shields.io/github/v/release/serious-scaffold/ss-python)](https://github.com/serious-scaffold/ss-python/releases)
[![PyPI](https://img.shields.io/pypi/v/ss-python)](https://pypi.org/project/ss-python/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ss-python)](https://pypi.org/project/ss-python/)
[![GitHub](https://img.shields.io/github/license/serious-scaffold/ss-python)](https://github.com/serious-scaffold/ss-python/blob/main/LICENSE)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/5697b1e4c4a9790ece607654e6c02a160620c7e1/docs/badge/v2.json)](https://pydantic.dev)
[![Serious Scaffold Python](https://img.shields.io/endpoint?url=https://serious-scaffold.github.io/ss-python/_static/badges/logo.json)](https://serious-scaffold.github.io/ss-python)
[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/serious-scaffold/ss-python)

> [!WARNING]
> _Serious Scaffold Python_ is in the **Alpha** phase.
> Frequent changes and instability should be anticipated.
> Any feedback, comments, suggestions and contributions are welcome!

[![Serious Scaffold Python](https://serious-scaffold.github.io/ss-python/_static/images/logo.svg)](https://github.com/serious-scaffold/ss-python)

Setting up a project often involves more than just establishing a basic project structure. It involves tasks like integrating GitHub Actions or GitLab CI/CD, configuring lint, test and documentation, as well as implementing settings, logging and other frequently used modules. [Serious Scaffold Python](https://github.com/serious-scaffold/ss-python) streamlines this process. Powered by [copier](https://copier.readthedocs.io/), bootstrapping a new Python project can be done with a single command. By answering a few questions, the project will be fully configured and ready for development. Furthermore, the project can be updated alongside the advancement of the template.

If you find this helpful, please consider [sponsorship](https://github.com/sponsors/huxuan).

## 🛠️ Features

- Project setup and template update with [copier](https://copier.readthedocs.io/).
- Manage dependencies and virtual environments with [pdm](https://pdm-project.org/).
- Build with [pdm-backend](https://backend.pdm-project.org/) and versioned with [SCM tag](https://backend.pdm-project.org/metadata/#read-from-scm-tag-supporting-git-and-hg).
- Lint with [pre-commit](https://pre-commit.com), [mypy](http://www.mypy-lang.org/), [ruff](https://github.com/charliermarsh/ruff), [toml-sort](https://github.com/pappasam/toml-sort) and [commitlint](https://commitlint.js.org/).
- Test with [pytest](https://pytest.org/) and [coverage](https://coverage.readthedocs.io) for threshold and reports.
- Documentation with [sphinx](https://www.sphinx-doc.org/), the [furo](https://pradyunsg.me/furo) theme and [MyST parser](https://myst-parser.readthedocs.io/) for markdown.
- Develop Command Line Interfaces with [typer](https://typer.tiangolo.com/).
- Manage configurations with [pydantic-settings](https://docs.pydantic.dev/latest/usage/pydantic_settings/).
- [Dev container](https://containers.dev/) for development and GitLab CI/CD.
- Automate dependency updates with [Renovate](https://github.com/renovatebot/renovate).
- Automate version management and release with [semantic-release](https://github.com/semantic-release/semantic-release).
- [Versioned documentation](https://docs.readthedocs.io/en/stable/versions.html) and [pull request previews](https://docs.readthedocs.io/en/stable/pull-requests.html) with [Read the Docs](https://readthedocs.org/).
- Adapted configuration for GitHub, GitLab and self-managed GitLab.
- Continuous Integration for Linux, MacOS and Windows [GitHub Only].
- Continuous Integration for multiple Python versions.
- Release with documentation, package and production container.
- Centralize common actions with a unified Makefile.
- VSCode settings with recommended extensions.

## 🔧 Prerequisites

Certain system-level Python applications are needed and it is recommended to use [pipx](https://pypa.github.io/pipx/) to install and run them in isolated environments. Refer to pipx's installation instructions [here](https://pypa.github.io/pipx/installation/). Once `pipx` is set up, install the necessary tools using the following commands.

```bash
# Copier: Template rendering for projects.
pipx install copier==9.2.0
# PDM: A modern Python package and dependency manager supporting the latest PEP standards.
pipx install pdm==2.15.3
# Pre-commit: Automates Git hooks for code quality checks.
pipx install pre-commit==3.7.1
```

## 🚀 Quickstart

1. Generate the project.

   ```bash
   copier copy gh:serious-scaffold/ss-python /path/to/project
   ```

2. Navigate to the project directory and initialize a git repository.

   ```bash
   cd /path/to/project
   git init
   ```

3. Set up the development environment.

   ```bash
   make dev
   ```

4. Commit the initialized project.

   ```bash
   git add .
   git commit -m "Initialize from serious-scaffold."
   ```

5. That's it! Feel free to focus on the coding within `src` folder.

## 📜 License

MIT License, for more details, see the [LICENSE](https://github.com/serious-scaffold/ss-python/blob/main/LICENSE) file.
