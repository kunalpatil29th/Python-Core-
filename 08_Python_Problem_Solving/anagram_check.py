# anagram_check.py

"""
Problem: Anagram Check
Check if two strings are anagrams of each other (contain the same characters in any order).
"""

def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Example
s1 = "Listen"
s2 = "Silent"
print(f"Are '{s1}' and '{s2}' anagrams? {are_anagrams(s1, s2)}")
