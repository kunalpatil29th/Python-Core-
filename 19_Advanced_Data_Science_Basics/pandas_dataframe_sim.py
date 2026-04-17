# pandas_dataframe_sim.py

"""
Definition: Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool. The primary data structure is the DataFrame, a two-dimensional table-like structure.
"""

def simulate_pandas():
    print("Simulating Pandas DataFrame...")
    data = {
        "Name": ["Kunal", "Alice", "Bob"],
        "Score": [95, 88, 92]
    }
    print("DataFrame Preview:")
    for i in range(len(data["Name"])):
        print(f"{data['Name'][i]}: {data['Score'][i]}")
    print(f"Average Score: {sum(data['Score'])/len(data['Score'])}")

simulate_pandas()
