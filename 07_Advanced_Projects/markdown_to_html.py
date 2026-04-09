# markdown_to_html.py

"""
Project: Basic Markdown to HTML Converter
Converts simple markdown syntax (headers and bold) to HTML tags.
"""

import re

def convert_markdown(text):
    # Headers
    text = re.sub(r'^# (.*)$', r'<h1>\1</h1>', text, flags=re.M)
    text = re.sub(r'^## (.*)$', r'<h2>\1</h2>', text, flags=re.M)
    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
    return text

markdown_input = "# Welcome\nThis is a **bold** statement.\n## Subtitle"
html_output = convert_markdown(markdown_input)
print("Markdown Input:\n", markdown_input)
print("\nHTML Output:\n", html_output)
