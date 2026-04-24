"""
passforge.scorer
----------------
Wraps the zxcvbn library to produce a structured score result for a
given password.

Score levels returned by zxcvbn (0 – 4):
    0  Too guessable  – risky password
    1  Very guessable – protection from throttled online attacks
    2  Somewhat guessable – protection from unthrottled online attacks
    3  Safely unguessable – moderate protection from offline slow-hash scenario
    4  Very unguessable – strong protection from offline slow-hash scenario

TODO: Implement the functions below.
"""

from __future__ import annotations
from zxcvbn import zxcvbn




def score_password(password: str) -> dict:
    """Analyze *password* with zxcvbn and return the raw result dict.

    Parameters
    ----------
    password:
        The plaintext password to analyze.  It is **never** stored or
        logged inside this function.

    Returns
    -------
    dict
        The full zxcvbn result dictionary.  Relevant keys include:
        ``"score"``, ``"guesses"``, ``"crack_times_display"``,
        ``"feedback"``, and ``"sequence"``.

    Raises
    ------
    ValueError
        If *password* is empty or not a string.
    """
    if not isinstance(password, str) or not password:
        raise ValueError("Password must be a non-empty string.")
    return zxcvbn(password) 


def get_score_label(score: int) -> str:
    """Return a human-readable label for a zxcvbn integer *score* (0–4).

    Parameters
    ----------
    score:
        Integer score value from a zxcvbn result (0, 1, 2, 3, or 4).

    Returns
    -------
    str
        A short label such as ``"Very Weak"``, ``"Weak"``,
        ``"Fair"``, ``"Strong"``, or ``"Very Strong"``.

    Raises
    ------
    ValueError
        If *score* is outside the range 0–4.
    """
    if not isinstance(score, int) or not (0 <= score <= 4):
        raise ValueError("Score must be an integer between 0 and 4.")
    switcher = {
        0: "Very Weak",
        1: "Weak",
        2: "Fair",
        3: "Strong",
        4: "Very Strong"
    }
    return switcher.get(score, "Invalid Score")


def get_crack_time_display(result: dict) -> str:
    """Extract a human-readable offline crack-time estimate from *result*.

    Parameters
    ----------
    result:
        The dictionary returned by :func:`score_password`.

    Returns
    -------
    str
        A display string for the estimated crack time under an offline,
        slow-hash scenario (e.g. ``"3 hours"``).
    """
    if not isinstance(result, dict) or "crack_times_display" not in result:
        raise ValueError("Result must be a dict containing 'crack_times_display'.")
    return result["crack_times_display"]["offline_slow_hashing_1e4_per_second"]
