"""Parse raw post data, and generate neatly formatted
code block titles.
"""

from pathlib import Path

# Read post file and template file.
post = Path('raw_post.html').read_text()
template = Path('my_template.eml').read_text()