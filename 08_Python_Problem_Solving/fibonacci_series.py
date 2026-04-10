# fibonacci_series.py

"""
Problem: Fibonacci Series
Generate the Fibonacci sequence up to 'n' terms.
"""

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

# Example
n_terms = 10
print(f"Fibonacci series up to {n_terms} terms: {fibonacci(n_terms)}")
