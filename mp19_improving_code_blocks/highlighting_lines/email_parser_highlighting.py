"""Parse raw post data, and highlight indicated lines.
"""

from pathlib import Path
import re

def process_code_block(line, lines_iter, modified_lines):
    """Check for highlighting, and convert as needed."""
    if "### hl_lines" in line:
        # Get the lines to highlight.
        numbering_re = r'<pre><code>### hl_lines="(.*)"'
        m = re.match(numbering_re, line)
        hl_line_nums = m.group(1).split(',')
        hl_line_nums = [int(num) for num in hl_line_nums]

        # Get the next line, and add the <pre><code> tags.
        line = next(lines_iter)
        new_line = add_codeblock_styles(line)
        modified_lines.append(new_line)

        # Get the rest of the lines in the code block.
        #   Add highlighting to appropriate lines.
        line_counter = 1
        while True:
            line = next(lines_iter)
            if line_counter in hl_line_nums:
                new_line = add_highlighting(line)
                modified_lines.append(new_line)
            else:
                modified_lines.append(line)

            line_counter += 1

            if "</code></pre>" in line:
                break
    else:
        # There's no highlighting, but we still need
        #   to add Substack's codeblock styles.
        new_line = add_codeblock_styles(line)
        modified_lines.append(new_line)

def add_highlighting(line):
    """Add highlighting style to current line."""
    hl_style = '<span style="background: #ddd; display: block; \
      padding-left: 5px; margin-left: -5px; margin-bottom: -20px">'

    # If we're highlighting the last line, we need to add a blank line
    #  to make up for the negative margin on highlighted lines.
    if "</code></pre>" in line:
        line = line.replace("</code></pre>", "")
        return f"{hl_style}{line}</span>\n</code></pre>"
    else:
        return f"{hl_style}{line}</span>"

def add_codeblock_styles(line):
    """Add Substack's codeblock styles."""
    pre_style = '<pre style="background: #eeeeee; border-radius: 4px; \
      box-sizing: border-box; margin: 32px 0; padding: 16px; \
      position: relative;">'
    code_style = '<code style=3D"font-size: 16px; font-weight: 500; \
      line-height: 20px; white-space: pre-wrap;">'

    line = line.replace("<pre>", pre_style)
    line = line.replace("<code>", code_style)
    line = f"{pre_style}{code_style}{line}"
    
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