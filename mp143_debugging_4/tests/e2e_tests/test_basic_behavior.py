"""Test user-facing behavior."""

import shlex
import sys
from pathlib import Path
import subprocess


def test_basic_behavior():
    """Test a simple run of dice_battle.py."""
    # Python executable
    path_root = Path(__file__).parents[2]
    if sys.platform == "win32":
        python_cmd = path_root / ".venv" / "Scripts" / "python"
    else:
        python_cmd = path_root / ".venv" / "bin" / "python"

    path_main = path_root / "dice_battle.py"
    cmd = f"{python_cmd} {path_main}"

    cmd_parts = shlex.split(cmd)
    output = subprocess.run(cmd_parts, capture_output=True)
    stdout = output.stdout.decode()
    stderr = output.stderr.decode()

    if stderr:
        print(stderr)

    assert stdout == "\nPlayer A: 5\nPlayer B: 1\nPlayer A won!\n\nPlayer A: 4\nPlayer B: 4\nTie!\n\nPlayer A: 5\nPlayer B: 1\nPlayer A won!\n\nPlayer A: 2\nPlayer B: 4\nPlayer B won!\n\nPlayer A: 4\nPlayer B: 3\nPlayer A won!\n\nPlayer A: 6\nPlayer B: 2\nPlayer A won!\n\nPlayer A: 1\nPlayer B: 5\nPlayer B won!\n\nPlayer A: 4\nPlayer B: 3\nPlayer A won!\n\nPlayer A: 1\nPlayer B: 2\nPlayer B won!\n\nPlayer A: 6\nPlayer B: 3\nPlayer A won!\n\n\nSummary:\n  Player A won 6 battles.\n  Player B won 3 battles.\n  There were 1 tied battles.\n\nClearly, player A is better at rolling dice.\n"