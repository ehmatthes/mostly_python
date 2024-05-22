from pygments import highlight
from pygments.lexers import PythonLexer, TextLexer, JsonLexer
from pygments.formatters import ImageFormatter, RtfFormatter

from pathlib import Path

# Get all snippets.
raw_dir = Path("raw_snippets")
raw_files = [
    path
    for path in raw_dir.iterdir()
    if path.suffix in [".py", ".json", ".txt"]
    ]

# Highlight all snippets.
hl_dir = Path("processed_snippets")
for file in raw_files:
    code = file.read_text()

    if file.suffix == ".py":
        lexer = PythonLexer()
    elif file.suffix == ".json":
        lexer = JsonLexer()
    else:
        lexer = TextLexer()

    hl_filename = file.stem + ".png"
    hl_file = hl_dir / hl_filename
    with open(hl_file, "wb") as f:
        # Set better parameters for ImageFormatter.
        formatter = ImageFormatter(
            line_pad=15,
            font_size=60,
            line_numbers=False,
        )

        highlighted_code = highlight(code, lexer, formatter)
        f.write(highlighted_code)
        print("Wrote file:", hl_file.as_posix())