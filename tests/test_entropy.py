"""
tests/test_entropy.py
---------------------
Unit tests for ``passforge.entropy``.

TODO: Fill in each test body once the module is implemented.
      Replace every ``pytest.skip(...)`` call with real assertions.

Suggested test matrix
---------------------
calculate_entropy_bits
    - log2(1024) == 10.0
    - log2(1) == 0.0
    - raises ValueError for guesses ≤ 0

describe_entropy
    - very low entropy (< 28 bits) → description contains "very low"
    - high entropy (≥ 128 bits) → description contains "very high"

entropy_summary
    - returns a dict with keys: "bits", "description", "guesses"
    - "bits" matches calculate_entropy_bits(result["guesses"])
"""

import pytest

# TODO: uncomment once entropy is implemented
# from passforge.entropy import calculate_entropy_bits, describe_entropy, entropy_summary


class TestCalculateEntropyBits:
    def test_known_value(self):
        pytest.skip("TODO: implement entropy.calculate_entropy_bits first")

    def test_guesses_of_one_gives_zero_bits(self):
        pytest.skip("TODO: implement entropy.calculate_entropy_bits first")

    def test_raises_value_error_for_non_positive_guesses(self):
        pytest.skip("TODO: implement entropy.calculate_entropy_bits first")


class TestDescribeEntropy:
    def test_very_low_entropy_label(self):
        pytest.skip("TODO: implement entropy.describe_entropy first")

    def test_very_high_entropy_label(self):
        pytest.skip("TODO: implement entropy.describe_entropy first")


class TestEntropySummary:
    def test_returns_dict_with_required_keys(self):
        pytest.skip("TODO: implement entropy.entropy_summary first")

    def test_bits_matches_calculate_entropy_bits(self):
        pytest.skip("TODO: implement entropy.entropy_summary first")
