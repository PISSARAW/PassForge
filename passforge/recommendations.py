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
    if not isinstance(result, dict) or "feedback" not in result:
        raise ValueError("Result must be a dict containing 'feedback'.")
    feedback = result["feedback"]
    suggestions = []
    if "warning" in feedback and feedback["warning"]:
        suggestions.append(feedback["warning"])
    if "suggestions" in feedback and isinstance(feedback["suggestions"], list):
        suggestions.extend(feedback["suggestions"])
    return suggestions


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
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")
    if not isinstance(result, dict) or "score" not in result or "sequence":
        raise ValueError("Result must be a dict containing 'score' and 'sequence'.")
    if result["score"] >= 2:
        return []  # No tips needed for reasonably strong passwords 
    tips = []
    if len(password) < OWASP_MIN_LENGTH:
        tips.append(f"Use at least {OWASP_MIN_LENGTH} characters.")
    if not any(c.islower() for c in password):
        tips.append("Include lowercase letters.")
    if not any(c.isupper() for c in password):
        tips.append("Include uppercase letters.")
    if not any(c.isdigit() for c in password):
        tips.append("Include digits.")
    if not any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in password):
        tips.append("Include symbols.")
    if "sequence" in result and isinstance(result["sequence"], list):
        for pattern in result["sequence"]:
            if pattern.get("pattern") == "keyboard":
                tips.append("Avoid keyboard patterns.")
            elif pattern.get("pattern") == "repeat":
                tips.append("Avoid repeated sequences.")
            elif pattern.get("pattern") == "dictionary":
                tips.append("Avoid common words or phrases.")
    return tips


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
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")
    if not isinstance(result, dict):
        raise ValueError("Result must be a dict.")
    zxcvbn_feedback = get_feedback(result)
    owasp_feedback = owasp_tips(password, result)
    has_issues = bool(zxcvbn_feedback or owasp_feedback)
    return {
        "zxcvbn_feedback": zxcvbn_feedback,
        "owasp_tips": owasp_feedback,
        "has_issues": has_issues
    }
