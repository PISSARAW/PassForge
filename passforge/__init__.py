"""
PassForge – CLI password strength analyzer.

Public API surface (all implemented in sub-modules):
    scorer          – score a password with zxcvbn
    entropy         – explain password entropy
    recommendations – OWASP-style improvement tips
    hasher          – optional SHA-256 demo (no storage)
    cli             – command-line entry point
"""

__version__ = "0.1.0"
__all__ = ["scorer", "entropy", "recommendations", "hasher", "cli"]
