"""
passforge.cli
-------------
Command-line entry point for PassForge.

Usage examples (once implemented):
    passforge --password "MyP@ssw0rd"
    passforge --password "MyP@ssw0rd" --show-hash
    passforge --password "MyP@ssw0rd" --no-color
    passforge --version

Argument reference
------------------
--password TEXT     The password to analyze.  Required.
--show-hash         Print the SHA-256 demo output alongside the report.
                    Off by default.
--no-color          Disable ANSI color codes in output (useful for
                    piping or terminals that don't support color).
--version           Print the PassForge version and exit.

TODO: Implement the functions below and wire up argparse.
"""

from __future__ import annotations

import argparse
import sys

from passforge import __version__

# TODO: import the sub-modules you'll call from the CLI
# from passforge import scorer, entropy, recommendations, hasher


def build_parser() -> argparse.ArgumentParser:
    """Create and return the argument parser for PassForge.

    Returns
    -------
    argparse.ArgumentParser
        A fully configured parser with all supported arguments.
    """
    parser = argparse.ArgumentParser(
        prog="passforge",
        description="PassForge – CLI password strength analyzer powered by zxcvbn",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Examples:\n"
            "  passforge --password \"MyP@ssw0rd\"\n"
            "  passforge --password \"correct horse battery staple\" --show-hash\n"
        ),
    )

    # TODO: Add the following arguments:
    #   --password   (required, str)
    #   --show-hash  (optional flag, store_true)
    #   --no-color   (optional flag, store_true)
    #   --version    (use parser.add_argument with action="version")
    if __version__:
        parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--password", type=str, required=True, help="The password to analyze.")
    parser.add_argument("--show-hash", action="store_true", help="Include the SHA-256 demo in the report.")
    parser.add_argument("--no-color", action="store_true", help="Disable ANSI color codes in output.")
    return parser

def print_report(password: str, *, show_hash: bool = False, color: bool = True) -> None:
    """Analyze *password* and print a formatted report to stdout.

    Parameters
    ----------
    password:
        The plaintext password to analyze.
    show_hash:
        When ``True``, include the SHA-256 avalanche demo in the report.
    color:
        When ``False``, strip ANSI escape codes from all output.
    """
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")
    if not isinstance(show_hash, bool):
        raise ValueError("show_hash must be a boolean.")
    if not isinstance(color, bool):
        raise ValueError("color must be a boolean.")


def main(argv: list[str] | None = None) -> None:
    """Parse arguments and run the PassForge analysis.

    This function is the entry point registered in ``pyproject.toml``.

    Parameters
    ----------
    argv:
        Argument list to parse.  Defaults to ``sys.argv[1:]`` when
        ``None``.
    """
    if argv is None:
        argv = sys.argv[1:]
    parser = build_parser().parse_args(argv)
    print_report(password=parser.password, show_hash=parser.show_hash, color=parser.no_color)
    return None


if __name__ == "__main__":
    main()
