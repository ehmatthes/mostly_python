"""Initial tests for add_border.py."""

import subprocess, filecmp
from pathlib import Path

# --- Tests for correct usage. ---

def test_default_border():
    """Test that calling with just a filename works."""

    # Note: currently, modified image ends up in same dir as source image.
    path_source = Path("tests/source_images/bear_scratching.jpg")
    path_modified = Path("tests/source_images/bear_scratching_bordered.jpg")
    path_reference = Path("tests/reference_images/bear_scratching_bordered_default.jpg")

    cmd = f"python add_border.py {path_source}"
    cmd_parts = cmd.split()

    subprocess.run(cmd_parts)
    assert filecmp.cmp(path_modified, path_reference)

def test_15px_border():
    """Test that calling with a filename and custom border width works."""

    # Note: currently, modified image ends up in same dir as source image.
    path_source = Path("tests/source_images/bear_scratching.jpg")
    path_modified = Path("tests/source_images/bear_scratching_bordered.jpg")
    path_reference = Path("tests/reference_images/bear_scratching_bordered_default_15px_border.jpg")

    cmd = f"python add_border.py {path_source} 15"
    cmd_parts = cmd.split()

    subprocess.run(cmd_parts)
    assert filecmp.cmp(path_modified, path_reference)

# --- Tests for incorrect usage. ---

def test_no_arg():
    """Test that calling without a filename specified generates correct error msg."""
    cmd = f"python add_border.py"
    cmd_parts = cmd.split()

    output = subprocess.run(cmd_parts, capture_output=True)
    error_msg = output.stdout.decode()

    assert "You must provide a target image." in error_msg

def test_invalid_image_file():
    """Test that calling with an invalid image file generates correct error msg."""
    path_source = Path("tests/source_images/hello.txt")

    cmd = f"python add_border.py {path_source}"
    cmd_parts = cmd.split()

    output = subprocess.run(cmd_parts, capture_output=True)
    error_msg = output.stdout.decode()

    assert "hello.txt does not seem to be an image file." in error_msg
