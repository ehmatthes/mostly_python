"""Parse raw post data, and generate neatly formatted
code block titles.
"""

from pathlib import Path

def process_code_block(line, lines_iter, modified_lines):
    """Check for a title, and convert as needed."""
    modified_lines.append(line)

# Read post file and template file.
post = Path('raw_post.html').read_text()
template = Path('my_template.eml').read_text()

# Loop over the lines in the raw post.
# When we get to a code block, look for a title.
# If we find a title, rewrite that line and the
#   next line.
modified_lines = []
lines = post.split("\n")
lines_iter = iter(lines)

while True:
    try:
        line = next(lines_iter)
    except StopIteration:
        break
    else:
        if "<pre><code>" in line:
            process_code_block(line, lines_iter, modified_lines)
        else:
            # Keep the line as is.
            modified_lines.append(line)

# Write the modified lines into the template.
post_html = "\n".join(modified_lines)

eml_string = template.replace('post_body', post_html)

output_file = Path('output_files/modified_test_email.eml')
output_file.write_text(eml_string)