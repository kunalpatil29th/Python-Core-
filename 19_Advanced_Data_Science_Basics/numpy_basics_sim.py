# numpy_basics_sim.py

"""
Definition: NumPy is the fundamental package for scientific computing in Python. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them.
"""

def simulate_numpy():
    print("Simulating NumPy Array operations...")
    data = [1, 2, 3, 4, 5]
    print(f"Array: {data}")
    print(f"Mean: {sum(data)/len(data)}")
    print(f"Squared: {[x**2 for x in data]}")

simulate_numpy()
