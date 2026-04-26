# PassForge

> A CLI password strength analyzer powered by [zxcvbn](https://github.com/dwolfhub/zxcvbn-python).

---

> ⚠️ **Personal project notice**
>
> PassForge is a **personal project**. The repository is public for transparency
> and portfolio purposes, but it is **not intended for general use** nor for a
> wide audience. It is not actively maintained as a product, comes with **no
> support, no guarantees, and no roadmap**, and may change or break at any time.
>
> Feel free to read the code or take inspiration from it, but please do not rely
> on it in production. For real-world password handling, prefer well-known and
> audited libraries.

---

## Overview

PassForge analyzes the strength of a password directly from your terminal.
It uses the **zxcvbn** algorithm (originally developed at Dropbox) to produce a
realistic crack-time estimate and actionable feedback, supplemented with
**OWASP-aligned recommendations** and an optional **SHA-256 avalanche demo**.

### Features

| Feature | Module |
|---|---|
| Password scoring (0 – 4) | `passforge/scorer.py` |
| Entropy explanation | `passforge/entropy.py` |
| OWASP-style improvement tips | `passforge/recommendations.py` |
| SHA-256 hashing demo (educational) | `passforge/hasher.py` |
| Clean CLI with argparse | `passforge/cli.py` |

### Current Status

- Core modules (`scorer`, `entropy`, `recommendations`, `hasher`) are implemented.
- CLI argument parsing is in place (`--password`, `--show-hash`, `--no-color`, `--version`).
- Some test files are still scaffolded with `pytest.skip(...)` and are pending completion.
- `print_report` in the CLI remains to be wired to the module outputs.

---

## Project Structure

```
PassForge/
├── passforge/               # Main package
│   ├── __init__.py
│   ├── cli.py               # CLI entry point
│   ├── scorer.py            # zxcvbn wrapper & score labelling
│   ├── entropy.py           # Entropy calculation & explanation
│   ├── recommendations.py   # OWASP-style tips
│   └── hasher.py            # SHA-256 demo (educational only)
├── tests/                   # Unit tests (pytest)
│   ├── __init__.py
│   ├── test_scorer.py
│   ├── test_entropy.py
│   ├── test_recommendations.py
│   └── test_hasher.py
├── .gitignore
├── LICENSE                  # MIT
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.9 or newer
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/PISSARAW/PassForge.git
cd PassForge

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install the package in editable mode (optional, enables the `passforge` command)
pip install -e .
```

### Usage

```bash
# Analyze a password
passforge --password "MyP@ssw0rd"

# Include the SHA-256 avalanche demo
passforge --password "MyP@ssw0rd" --show-hash

# Disable color output (useful for piping)
passforge --password "MyP@ssw0rd" --no-color

# Print version
passforge --version
```

> **Note:** The command interface is available. Output formatting in `print_report`
> is still in progress.

---

## Running the Tests

Simplified commands:

```bash
make test
make test-verbose
make test-cov
# Run one specific test file/function
make test TEST=tests/test_scorer.py
make test TEST=tests/test_scorer.py::test_score_password_returns_expected_keys
```

Equivalent direct command:

```bash
pytest
```

To include a coverage report:

```bash
pytest --cov=passforge --cov-report=term-missing
```

---

## Development Notes

- The project keeps rich docstrings in each module to describe expected behavior.
- Tests currently mix implemented checks and scaffolded cases.
- Recommended next milestone is finishing CLI report rendering and unskipping
  the remaining test suites.

---

## Security Notes

- PassForge **never stores, logs, or transmits** any password.
- The SHA-256 demo in `hasher.py` is **educational only**.  SHA-256 is a
  fast hash and is **not** suitable for password storage.  For real
  applications, use Argon2, bcrypt, or scrypt.

---

## License

Distributed under the [MIT License](LICENSE).
