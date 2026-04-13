# regex_patterns.py

"""
Definition: Regular Expressions (Regex) are a powerful tool for matching patterns in text. 
Python's 're' module provides support for regular expressions.
"""

import re

text = "Contact us at support@example.com or info@python.org"

# Find all emails
emails = re.findall(r'[\w\.-]+@[\w\.-]+', text)
print(f"Text: {text}")
print(f"Found Emails: {emails}")

# Check if text starts with 'Contact'
if re.match(r'^Contact', text):
    print("The text starts with 'Contact'")
