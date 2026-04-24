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

# TODO: import zxcvbn here
# from zxcvbn import zxcvbn


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
    raise NotImplementedError("TODO: call zxcvbn(password) and return its result")


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
    raise NotImplementedError("TODO: map score integer to label string")


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
    raise NotImplementedError(
        "TODO: extract crack_times_display['offline_slow_hashing_1e4_per_second'] "
        "from result and return it"
    )
