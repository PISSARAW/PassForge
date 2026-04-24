"""
passforge.entropy
-----------------
Explains password entropy in plain language so the user understands
*why* their password scored a particular way.

Entropy (bits) is a measure of unpredictability.  zxcvbn internally
estimates it via guesses; this module converts that to bits and provides
a friendly explanation.

Formula used:
    entropy_bits = log2(guesses)

TODO: Implement the functions below.
"""

from __future__ import annotations

import math


def calculate_entropy_bits(guesses: int | float) -> float:
    """Convert a zxcvbn *guesses* estimate to bits of entropy.

    Parameters
    ----------
    guesses:
        The ``"guesses"`` value from a zxcvbn result dict.  Must be
        a positive number.

    Returns
    -------
    float
        Entropy in bits (``log2(guesses)``).

    Raises
    ------
    ValueError
        If *guesses* is not a positive number.
    """
    raise NotImplementedError("TODO: return math.log2(guesses)")


def describe_entropy(entropy_bits: float) -> str:
    """Return a plain-language description of the given *entropy_bits* value.

    Suggested thresholds (adjust to your taste):
        < 28 bits  → "Very low entropy – extremely easy to guess"
        < 36 bits  → "Low entropy – easy to guess"
        < 60 bits  → "Moderate entropy – reasonable for most uses"
        < 128 bits → "High entropy – difficult to crack offline"
        ≥ 128 bits → "Very high entropy – excellent security"

    Parameters
    ----------
    entropy_bits:
        The entropy value produced by :func:`calculate_entropy_bits`.

    Returns
    -------
    str
        A human-readable sentence describing the entropy level.
    """
    raise NotImplementedError("TODO: map entropy_bits ranges to description strings")


def entropy_summary(result: dict) -> dict:
    """Build a complete entropy summary from a zxcvbn *result* dict.

    Parameters
    ----------
    result:
        The dictionary returned by ``passforge.scorer.score_password``.

    Returns
    -------
    dict
        A dictionary with at least the following keys:

        ``"bits"``
            Entropy in bits (float).
        ``"description"``
            Human-readable description string (str).
        ``"guesses"``
            Raw guesses estimate echoed back (int or float).
    """
    raise NotImplementedError(
        "TODO: combine calculate_entropy_bits and describe_entropy, "
        "then return the summary dict"
    )
