"""
passforge.recommendations
-------------------------
Generates actionable, OWASP-style password improvement tips based on
the zxcvbn analysis result.

Reference: OWASP Authentication Cheat Sheet
https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html

Key OWASP guidelines applied here:
    - Minimum 12-character passwords for user-facing accounts
    - Avoid passwords found in breach databases (zxcvbn covers common ones)
    - Encourage passphrases and random character mixing
    - Warn about keyboard patterns, repetitions, and dictionary words

TODO: Implement the functions below.
"""

from __future__ import annotations

# Minimum recommended password length per OWASP guidelines.
OWASP_MIN_LENGTH: int = 12


def get_feedback(result: dict) -> list[str]:
    """Extract zxcvbn's own feedback suggestions from *result*.

    Parameters
    ----------
    result:
        The dictionary returned by ``passforge.scorer.score_password``.

    Returns
    -------
    list[str]
        A list of suggestion strings from zxcvbn's ``"feedback"`` key.
        Returns an empty list when zxcvbn provides no suggestions.
    """
    raise NotImplementedError(
        "TODO: read result['feedback']['suggestions'] and return it as a list"
    )


def owasp_tips(password: str, result: dict) -> list[str]:
    """Generate OWASP-aligned improvement tips for *password*.

    This function inspects the raw password and the zxcvbn *result* to
    build a list of concrete, actionable tips.  Check for (at minimum):

    - Password length below :data:`OWASP_MIN_LENGTH`
    - Missing character class diversity (uppercase, lowercase, digits,
      symbols)
    - Low zxcvbn score (0 or 1)
    - Presence of keyboard walks, repeats, or dictionary matches
      (available in ``result["sequence"]``)

    Parameters
    ----------
    password:
        The plaintext password being analyzed.
    result:
        The dictionary returned by ``passforge.scorer.score_password``.

    Returns
    -------
    list[str]
        A list of human-readable tip strings.  Returns an empty list
        when no specific issues are found.
    """
    raise NotImplementedError(
        "TODO: build and return a list of OWASP-style tip strings"
    )


def build_recommendation_report(password: str, result: dict) -> dict:
    """Combine all feedback into a single recommendation report.

    Parameters
    ----------
    password:
        The plaintext password being analyzed.
    result:
        The dictionary returned by ``passforge.scorer.score_password``.

    Returns
    -------
    dict
        A dictionary with at least the following keys:

        ``"zxcvbn_feedback"``
            List of suggestion strings from :func:`get_feedback`.
        ``"owasp_tips"``
            List of OWASP-style tip strings from :func:`owasp_tips`.
        ``"has_issues"``
            ``True`` if any issues were found, ``False`` otherwise.
    """
    raise NotImplementedError(
        "TODO: call get_feedback and owasp_tips, merge results, "
        "and return the report dict"
    )
