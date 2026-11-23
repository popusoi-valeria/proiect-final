from pathlib import Path

def test_readme_exists():
    assert Path("README.md").exists()

def test_license_exists():
    assert Path("LICENSE").exists()

def test_contributing_exists():
    assert Path("CONTRIBUTING.md").exists()