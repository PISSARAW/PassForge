"""
passforge.hasher
----------------
Optional SHA-256 hashing demo.

⚠️  IMPORTANT – Educational Use Only ⚠️
SHA-256 is a *fast* hashing algorithm.  It is **NOT** suitable for
storing passwords.  Use a memory-hard algorithm such as Argon2, bcrypt,
or scrypt for real password storage.

This module exists purely to demonstrate the concept of one-way hashing
and to show how a password's hash changes with even a tiny input
difference (the avalanche effect).  No hash produced here is ever
written to disk or transmitted.

TODO: Implement the functions below.
"""

from __future__ import annotations

import hashlib


def sha256_hex(password: str) -> str:
    """Return the SHA-256 hex digest of *password*.

    Parameters
    ----------
    password:
        The plaintext password to hash.  It is **not** stored anywhere
        by this function.

    Returns
    -------
    str
        A 64-character lowercase hex string representing the SHA-256
        digest of *password* encoded as UTF-8.

    Raises
    ------
    ValueError
        If *password* is empty or not a string.
    """
    raise NotImplementedError(
        "TODO: encode password as UTF-8, hash with hashlib.sha256, "
        "and return hexdigest()"
    )


def avalanche_demo(password: str) -> dict:
    """Demonstrate the SHA-256 avalanche effect.

    Appends a single extra character (``'!'``) to *password* and
    compares the resulting hash to the original, showing how a tiny
    change produces a completely different digest.

    Parameters
    ----------
    password:
        The original plaintext password.

    Returns
    -------
    dict
        A dictionary with the following keys:

        ``"original_hash"``
            SHA-256 hex digest of *password* (str).
        ``"modified_hash"``
            SHA-256 hex digest of ``password + '!'`` (str).
        ``"bits_flipped"``
            The number of bits that differ between the two digests (int).
    """
    raise NotImplementedError(
        "TODO: hash both passwords, count differing bits (XOR each byte pair), "
        "and return the result dict"
    )
