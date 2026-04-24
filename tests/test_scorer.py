"""
tests/test_scorer.py
--------------------
Unit tests for ``passforge.scorer``.

TODO: Fill in each test body once the module is implemented.
      Replace every ``pytest.skip(...)`` call with real assertions.

Suggested test matrix
---------------------
score_password
    - returns a dict for a valid password
    - raises ValueError for an empty string
    - raises ValueError for a non-string argument
    - "password" scores 0 or 1 (very weak)
    - a long random-looking string scores 3 or 4

get_score_label
    - score 0 → "Very Weak"
    - score 4 → "Very Strong"
    - invalid score → ValueError

get_crack_time_display
    - returns a non-empty string for a valid result dict
"""

import pytest

# TODO: uncomment once scorer is implemented
# from passforge.scorer import score_password, get_score_label, get_crack_time_display


class TestScorePassword:
    def test_returns_dict_for_valid_password(self):
        pytest.skip("TODO: implement scorer.score_password first")

    def test_raises_value_error_for_empty_string(self):
        pytest.skip("TODO: implement scorer.score_password first")

    def test_raises_value_error_for_non_string(self):
        pytest.skip("TODO: implement scorer.score_password first")

    def test_common_password_scores_low(self):
        pytest.skip("TODO: implement scorer.score_password first")

    def test_strong_password_scores_high(self):
        pytest.skip("TODO: implement scorer.score_password first")


class TestGetScoreLabel:
    def test_score_0_is_very_weak(self):
        pytest.skip("TODO: implement scorer.get_score_label first")

    def test_score_4_is_very_strong(self):
        pytest.skip("TODO: implement scorer.get_score_label first")

    def test_invalid_score_raises_value_error(self):
        pytest.skip("TODO: implement scorer.get_score_label first")


class TestGetCrackTimeDisplay:
    def test_returns_non_empty_string(self):
        pytest.skip("TODO: implement scorer.get_crack_time_display first")
