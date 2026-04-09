# url_shortener.py

"""
Project: URL Shortener
A simple logic to map long URLs to short codes using a dictionary.
"""

import hashlib

url_mapping = {}

def shorten_url(long_url):
    short_code = hashlib.md5(long_url.encode()).hexdigest()[:6]
    url_mapping[short_code] = long_url
    return f"http://short.ly/{short_code}"

def resolve_url(short_code):
    return url_mapping.get(short_code, "URL not found")

# Example
long_url = "https://www.google.com/search?q=python+programming"
short_url = shorten_url(long_url)
print(f"Long URL: {long_url}")
print(f"Short URL: {short_url}")
