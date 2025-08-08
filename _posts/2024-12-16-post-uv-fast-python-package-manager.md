---
title: "UV: The Fast Python Package Manager - A Complete Guide"
header:
  image: /assets/images/uv.jpg
last_modified_at: 2024-12-16
categories:
  - Python
  - DevOps
  - Development
  - Tools
tags:
  - Python
  - Package Management
  - UV
  - Development Tools
  - Performance
toc: true
toc_sticky: true
---

# UV: The Fast Python Package Manager - A Complete Guide

UV is a revolutionary Rust-based Python package manager that's been dubbed "Cargo for Python." Created by Astral (the same team behind Ruff), UV replaces pip, pip-tools, pipx, poetry, pyenv, and virtualenv with a single, blazingly fast tool that delivers **10-100x performance improvements**.

Imagine installing TensorFlow in 25 seconds instead of 3 minutes. That's the kind of speed we're talking about.

**Installation:** [Download and install UV here](https://docs.astral.sh/uv/getting-started/installation/)

## Why Developers Are Switching to UV

After working with Python for over 10 years, I can confidently say that setting up new projects, managing dependencies, and getting everything to work has always been one of my least favorite parts of the language. UV solves all of that.

### Key Benefits

- **🚀 Speed**: CI/CD pipelines drop from 25+ minutes to seconds
- **🎯 Simplicity**: No more juggling multiple tools or activating virtual environments
- **🔄 Modern**: Built-in Python version management and dependency groups
- **🔧 Compatible**: Works seamlessly with existing pip/poetry workflows

But beyond all the technical benefits, UV makes working with Python much more enjoyable. This guide will cover everything you need to know to get started.

## About Astral and Ruff

UV comes from [Astral](https://astral.sh/), the same team behind [Ruff](https://docs.astral.sh/ruff/) - the extremely fast Python linter and formatter that I highly recommend to everyone. Like UV, Ruff is written in Rust and delivers massive performance improvements (100x faster than flake8). If you're not using Ruff yet, you should be - it replaces flake8, isort, black, and more with a single blazingly fast tool.

## Most Common Real-World Workflows

### Starting a New Python Project

Creating a new project with UV is incredibly simple:

```bash
uv init my-ai-app
cd my-ai-app
```

This creates a clean project structure:

```
my-web-app/
├── .gitignore
├── .python-version    # Pins Python version
├── README.md
├── hello.py
└── pyproject.toml     # Modern Python packaging
```

Adding dependencies and running your code:

```bash
uv add openai fastapi
uv run hello.py
```

UV automatically creates the virtual environment, installs dependencies, and generates `uv.lock` for reproducible builds.

### Working with Existing Projects

For existing projects, the workflow is just as smooth:

```bash
git clone https://github.com/org/project.git
cd project
uv sync
```

The `uv sync` command creates the virtual environment and installs exact versions from `uv.lock` for identical team setups.

For production deployments (excluding development dependencies):

```bash
uv sync --no-dev
```

## Python Version Management

UV includes built-in Python version management that replaces pyenv:

```bash
# Install Python versions
uv python install 3.12
uv python install 3.11 3.12 3.13  # Multiple at once

# Pin project to specific version
uv python pin 3.12  # Creates .python-version

# List available versions
uv python list
```

**Automatic Python installation**: UV automatically installs missing Python versions during `uv sync`.

## Development vs Production Dependencies

UV uses modern dependency groups following PEP 735:

```toml
[project]
name = "my-app"
dependencies = [
    "fastapi>=0.100.0",
    "sqlalchemy>=2.0.0",
]

[dependency-groups]
dev = [
    "pytest>=7.4.0",
    "black>=23.0.0",
]
```

Managing dependency groups:

```bash
uv add --dev pytest black        # Add to dev group
uv sync                          # Install everything
uv sync --no-dev                 # Production only
```

## Essential UV Commands

Here are the most common UV commands you'll use:

### Project Setup
```bash
uv init myproject           # Create new project
uv add requests             # Add dependency
uv remove requests          # Remove dependency
uv sync                     # Install from lockfile
```

### Running Code
```bash
uv run script.py            # Run in project environment
uv run pytest               # Run tests
```

### Python Management
```bash
uv python install 3.12      # Install Python version
uv python pin 3.12          # Set project Python
```

### Tool Usage
```bash
uvx black .                 # Run tool temporarily
uv tool install ruff        # Install tool globally
```

### Package Management (pip-compatible)
```bash
uv pip install requests     # Direct pip replacement
uv pip install -r requirements.txt
```

## Complete New Project Flow

Here's a typical workflow for starting a new project:

```bash
uv init my-project
cd my-project
cursor .

uv add openai python-dotenv fastapi
uv add --dev ipykernel
echo "API_KEY=your-key" > .env

git init
git add .
git commit -m "Initial commit"

# Create new repo with GitHub CLI
gh repo create my-project --private --source=. --remote=origin --push
```

## Performance Comparison

The performance improvements are staggering:

| Task | Traditional Tools | UV | Improvement |
|------|------------------|-----|-------------|
| TensorFlow install | 3 minutes | 25 seconds | 7x faster |
| CI/CD pipeline | 25+ minutes | 2-3 minutes | 10x faster |
| Dependency resolution | 30+ seconds | 2-3 seconds | 10x faster |
| Virtual environment creation | 5-10 seconds | <1 second | 10x faster |

## Migration from Existing Tools

If you're currently using other tools, UV makes migration easy:

### From pip + venv
```bash
# Old way
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# New way
uv sync
```

### From Poetry
```bash
# Old way
poetry install
poetry run python script.py

# New way
uv sync
uv run python script.py
```

### From pipenv
```bash
# Old way
pipenv install
pipenv run python script.py

# New way
uv sync
uv run python script.py
```

## Best Practices

1. **Always use `uv.lock`**: Commit this file to version control for reproducible builds
2. **Pin Python versions**: Use `uv python pin` to ensure consistent Python versions across team
3. **Use dependency groups**: Separate production and development dependencies
4. **Leverage `uvx`**: For one-off tool usage without permanent installation
5. **Update regularly**: UV is actively developed with frequent improvements

## Conclusion

UV represents a significant leap forward in Python development tooling. By consolidating multiple tools into a single, fast, and reliable package manager, it eliminates much of the friction that has traditionally made Python project setup and maintenance tedious.

The performance improvements alone make it worth switching, but the improved developer experience is what will keep you using it. No more juggling multiple tools, no more slow dependency resolution, and no more complex virtual environment management.

Whether you're starting a new project or working with existing codebases, UV provides a modern, fast, and enjoyable way to manage Python dependencies and environments.

For more detailed information and advanced use cases, check out the [official UV documentation](https://docs.astral.sh/uv/getting-started/).

---

*Ready to speed up your Python development? Give UV a try and experience the difference for yourself!*
