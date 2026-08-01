# tests/test_readme_examples_smoke.py
# Lightweight smoke test to import the README-referenced top-level module names.
# This file does not assert detailed behavior; it ensures imports run without raising import-time exceptions.
import importlib

TOP_LEVEL_MODULES = [
    "frequency_dialer",
    "text_handler",
    "communication_core",
    "wireless_download",
]

def test_top_level_imports():
    for mod in TOP_LEVEL_MODULES:
        importlib.import_module(mod)
