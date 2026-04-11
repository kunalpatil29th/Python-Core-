# valid_parentheses.py

"""
Problem: Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
"""

def is_valid(s):
    stack = []
    close_to_open = {")": "(", "}": "{", "]": "["}
    for char in s:
        if char in close_to_open:
            if stack and stack[-1] == close_to_open[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return True if not stack else False

# Example
s = "()[]{}"
print(f"Is '{s}' valid? {is_valid(s)}")
