"""
tests/test_hasher.py
--------------------
Unit tests for ``passforge.hasher``.

TODO: Fill in each test body once the module is implemented.
      Replace every ``pytest.skip(...)`` call with real assertions.

Suggested test matrix
---------------------
sha256_hex
    - known value: sha256("") == "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    - known value: sha256("abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    - returns a 64-character lowercase hex string
    - raises ValueError for an empty string (design choice: require non-empty input)
    - raises ValueError for a non-string argument

avalanche_demo
    - returns a dict with keys: "original_hash", "modified_hash", "bits_flipped"
    - "original_hash" matches sha256_hex(password)
    - "modified_hash" matches sha256_hex(password + "!")
    - "bits_flipped" is between 1 and 256 (inclusive) for any input
"""

import pytest

# TODO: uncomment once hasher is implemented
# from passforge.hasher import sha256_hex, avalanche_demo


class TestSha256Hex:
    def test_known_empty_string_hash(self):
        pytest.skip("TODO: implement hasher.sha256_hex first")

    def test_known_abc_hash(self):
        pytest.skip("TODO: implement hasher.sha256_hex first")

    def test_returns_64_char_hex_string(self):
        pytest.skip("TODO: implement hasher.sha256_hex first")

    def test_raises_value_error_for_empty_input(self):
        pytest.skip("TODO: implement hasher.sha256_hex first")

    def test_raises_value_error_for_non_string(self):
        pytest.skip("TODO: implement hasher.sha256_hex first")


class TestAvalancheDemo:
    def test_returns_dict_with_required_keys(self):
        pytest.skip("TODO: implement hasher.avalanche_demo first")

    def test_original_hash_matches_sha256_hex(self):
        pytest.skip("TODO: implement hasher.avalanche_demo first")

    def test_modified_hash_matches_sha256_hex_with_bang(self):
        pytest.skip("TODO: implement hasher.avalanche_demo first")

    def test_bits_flipped_is_within_valid_range(self):
        pytest.skip("TODO: implement hasher.avalanche_demo first")
