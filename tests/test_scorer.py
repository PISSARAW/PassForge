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
from passforge.scorer import score_password, get_score_label, get_crack_time_display


class TestScorePassword:
    def test_returns_dict_for_valid_password(self):
        result = score_password("CorrectHorseBatteryStaple!2026")
        assert isinstance(result, dict)
        assert "score" in result

    def test_raises_value_error_for_empty_string(self):
        assert isinstance(score_password(""), ValueError)

    def test_raises_value_error_for_non_string(self):
        assert isinstance(score_password(12345), ValueError)

    def test_common_password_scores_low(self):
        result = score_password("password")
        assert result["score"] in (0, 1)

    def test_strong_password_scores_high(self):
        result = score_password("CorrectHorseBatteryStaple!2026")
        assert result["score"] in (3, 4)

class TestGetScoreLabel:
    def test_score_0_is_very_weak(self):
        result = score_password("password")
        assert result["score"] == 0
        label = get_score_label(result["score"])
        assert label == "Very Weak" 

    def test_score_4_is_very_strong(self):
        result = score_password("CorrectHorseBatteryStaple!2026")
        assert result["score"] == 4 
        label = get_score_label(result["score"])
        assert label == "Very Strong"


    def test_invalid_score_raises_value_error(self):
        assert isinstance(get_score_label(5), ValueError)
        assert isinstance(get_score_label(-1), ValueError)
        assert isinstance(get_score_label("3"), ValueError)

class TestGetCrackTimeDisplay:
    def test_returns_non_empty_string(self):
        result = score_password("CorrectHorseBatteryStaple!2026")
        crack_time = get_crack_time_display(result)
        assert isinstance(crack_time, str)
        assert len(crack_time) > 0