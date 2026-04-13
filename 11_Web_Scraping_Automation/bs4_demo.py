# bs4_demo.py

"""
Definition: BeautifulSoup (bs4) is a library for parsing HTML and XML documents. 
It creates a parse tree for pages that can be used to extract data easily.
"""

# Simulation of HTML parsing
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time...</p>
</body></html>
"""

def simulate_parse(html):
    print("Parsing HTML content...")
    if "title" in html:
        print("Title found: The Dormouse's story")

simulate_parse(html_doc)
