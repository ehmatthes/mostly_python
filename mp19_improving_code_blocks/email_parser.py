"""Parse raw post data, and generate neatly formatted
code block titles.
"""

from pathlib import Path

def process_code_block(line, lines_iter, modified_lines):
    """Check for a title, and convert as needed."""
    if "### title" in line:
        # Convert the first line to the new title style.
        new_line = get_title_line(line)
        modified_lines.append(new_line)

        # Add the <pre><code> tags to the next line,
        #   and then add styles.
        line = next(lines_iter)
        new_line = f"<pre><code>{line}"
        new_line = add_codeblock_styles(new_line)
        modified_lines.append(new_line)
    else:
        # There's no title, but we still need
        #   to add Substack's codeblock styles.
        new_line = add_codeblock_styles(line)
        modified_lines.append(new_line)

def get_title_line(line):
    """Generate a formatted title line."""
    # Remove the <pre><code> blocks.
    line = line.replace("<pre><code>", "")

    # Get just the title; strip syntax and quotes.
    title = line.replace("### title=", "")
    title = title.replace('"', '')
    title = title.replace("'", "")

    # Define style rule.
    style_rule = '<p style="background: #dddddd; \
      padding: 5px 5px 5px 10px; \
      margin-bottom: -32px; \
      border-radius: 4px 4px 0 0; \
      font-weight: bold; \
      font-size: 14px;">'

    return f"{style_rule}{title}</p>"

def add_codeblock_styles(line):
    """Add Substack's codeblock styles."""
    pre_style = '<pre style="background: #eeeeee; \
      border-radius: 4px; box-sizing: border-box; \
      margin: 32px 0; padding: 16px; \
      position: relative;">'
    code_style = '<code style=3D"font-size: 16px; \
      font-weight: 500; line-height: 20px; \
      white-space: pre-wrap;">'

    line = line.replace("<pre>", pre_style)
    line = line.replace("<code>", code_style)
    
    return line

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