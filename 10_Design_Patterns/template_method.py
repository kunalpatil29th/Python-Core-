# template_method.py

"""
Definition: The Template Method Pattern defines the skeleton of an algorithm in an operation, deferring some steps to subclasses.
"""

class DocumentGenerator:
    def generate(self):
        self.open()
        self.add_content()
        self.save()

    def open(self): print("Opening file...")
    def save(self): print("Saving file...")
    def add_content(self): pass

class PDFGenerator(DocumentGenerator):
    def add_content(self):
        print("Adding PDF content.")

# Usage
pdf = PDFGenerator()
pdf.generate()
