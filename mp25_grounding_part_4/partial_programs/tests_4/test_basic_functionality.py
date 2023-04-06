"""Initial tests of basic functionality."""

import subprocess, filecmp
from pathlib import Path

# --- Tests for correct usage. ---

def test_default_border():
    """Test that calling with just a filename works."""

    # Note: currently, modified image ends up in same dir as source image.
    path_source = Path("tests/source_images/bear_scratching.jpg")
    path_modified = Path("tests/source_images/bear_scratching_bordered.jpg")
    path_reference = Path("tests/reference_images/bear_scratching_default.jpg")

    cmd = f"python main.py {path_source}"
    cmd_parts = cmd.split()

    output = subprocess.run(cmd_parts, capture_output=True)
    output_str = output.stdout.decode()
    assert filecmp.cmp(path_modified, path_reference)
    assert f"New image saved at {path_modified}" in output_str

def test_15px_border():
    """Test that calling with a filename and custom border width works."""

    # Note: currently, modified image ends up in same dir as source image.
    path_source = Path("tests/source_images/bear_scratching.jpg")
    path_modified = Path("tests/source_images/bear_scratching_bordered.jpg")
    path_reference = Path("tests/reference_images/bear_scratching_15px_border.jpg")

    cmd = f"python main.py {path_source} 15"
    cmd_parts = cmd.split()

    subprocess.run(cmd_parts)
    assert filecmp.cmp(path_modified, path_reference)

def test_padding_only():
    """Test that you can add padding to an image."""
    # Note: currently, modified image ends up in same dir as source image.
    path_source = Path("tests/source_images/bear_scratching.jpg")
    path_modified = Path("tests/source_images/bear_scratching_bordered.jpg")
    path_reference = Path("tests/reference_images/bear_scratching_15px_padding.jpg")

    cmd = f"python main.py {path_source} --padding 15"
    cmd_parts = cmd.split()

    subprocess.run(cmd_parts)
    assert filecmp.cmp(path_modified, path_reference)

def test_custom_color_only():
    """Test that you can set a custom border color."""
    # Note: currently, modified image ends up in same dir as source image.
    path_source = Path("tests/source_images/bear_scratching.jpg")
    path_modified = Path("tests/source_images/bear_scratching_bordered.jpg")
    path_reference = Path("tests/reference_images/bear_scratching_black_border.jpg")

    cmd = f"python main.py {path_source} --border-color black"
    cmd_parts = cmd.split()

    subprocess.run(cmd_parts)
    assert filecmp.cmp(path_modified, path_reference)

def test_padding_and_border():
    """Test that you can set custom padding and border width."""
    # Note: This is just one test for combinining options; would add more of
    #   these tests in a widely-used version of the project.

    # Note: currently, modified image ends up in same dir as source image.
    path_source = Path("tests/source_images/bear_scratching.jpg")
    path_modified = Path("tests/source_images/bear_scratching_bordered.jpg")
    path_reference = Path("tests/reference_images/bear_scratching_20px_border_15px_padding.jpg")

    cmd = f"python main.py {path_source} 20 --padding 15"
    cmd_parts = cmd.split()

    subprocess.run(cmd_parts)
    assert filecmp.cmp(path_modified, path_reference)


# --- Tests for incorrect usage. ---

def test_no_arg():
    """Test that calling without a filename specified generates correct error msg."""
    cmd = f"python main.py"
    cmd_parts = cmd.split()

    output = subprocess.run(cmd_parts, capture_output=True)
    error_msg = output.stderr.decode()

    assert "error: the following arguments are required: filename" in error_msg

    # error_msg = output.stdout.decode()
    # assert "You must provide a target image." in error_msg

def test_nonexistent_file():
    """Test that calling with a nonexistent file generates a correct error msg."""
    path_source = Path("tests/source_images/nonexistent_file.txt")

    cmd = f"python main.py {path_source}"
    cmd_parts = cmd.split()

    output = subprocess.run(cmd_parts, capture_output=True)
    error_msg = output.stdout.decode()

    assert "nonexistent_file.txt does not seem to exist." in error_msg

def test_invalid_image_file():
    """Test that calling with an invalid image file generates correct error msg."""
    path_source = Path("tests/source_images/hello.txt")

    cmd = f"python main.py {path_source}"
    cmd_parts = cmd.split()

    output = subprocess.run(cmd_parts, capture_output=True)
    error_msg = output.stdout.decode()

    assert "hello.txt does not seem to be an image file." in error_msg
