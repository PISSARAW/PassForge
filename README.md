# PassForge

> A CLI password strength analyzer powered by [zxcvbn](https://github.com/dwolfhub/zxcvbn-python).

---

## Overview

PassForge analyzes the strength of a password directly from your terminal.
It uses the **zxcvbn** algorithm (originally developed at Dropbox) to produce a
realistic crack-time estimate and actionable feedback, supplemented with
**OWASP-aligned recommendations** and an optional **SHA-256 avalanche demo**.

### Features (to be implemented)

| Feature | Module |
|---|---|
| Password scoring (0 – 4) | `passforge/scorer.py` |
| Entropy explanation | `passforge/entropy.py` |
| OWASP-style improvement tips | `passforge/recommendations.py` |
| SHA-256 hashing demo (educational) | `passforge/hasher.py` |
| Clean CLI with argparse | `passforge/cli.py` |

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

> **Note:** These commands will work once you have implemented the modules.

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

## Implementation Guide

Each Python file in `passforge/` contains skeleton functions with:

- Full **docstrings** describing parameters, return types, and exceptions.
- A `raise NotImplementedError("TODO: …")` placeholder where the logic goes.
- Inline comments and hints to guide the implementation.

The matching test files in `tests/` contain `pytest.skip("TODO: …")` stubs
that list exactly what needs to be verified for each function.

**Suggested order of implementation:**

1. `scorer.py` – the foundation (used by every other module)
2. `entropy.py` – depends only on `scorer.py` results
3. `recommendations.py` – depends on `scorer.py` results
4. `hasher.py` – standalone; no cross-module dependency
5. `cli.py` – ties everything together

---

## Security Notes

- PassForge **never stores, logs, or transmits** any password.
- The SHA-256 demo in `hasher.py` is **educational only**.  SHA-256 is a
  fast hash and is **not** suitable for password storage.  For real
  applications, use Argon2, bcrypt, or scrypt.

---

## License

Distributed under the [MIT License](LICENSE).
