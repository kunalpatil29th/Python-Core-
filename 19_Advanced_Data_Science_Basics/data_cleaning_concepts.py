# data_cleaning_concepts.py

"""
Definition: Data cleaning is the process of fixing or removing incorrect, corrupted, incorrectly formatted, duplicate, or incomplete data within a dataset.
"""

def simulate_data_cleaning():
    raw_data = [10, 20, None, 30, 20, 40]
    print(f"Raw Data: {raw_data}")
    
    # Remove None (missing values)
    cleaned = [x for x in raw_data if x is not None]
    # Remove duplicates
    unique_cleaned = list(set(cleaned))
    
    print(f"Cleaned unique data: {unique_cleaned}")

simulate_data_cleaning()
