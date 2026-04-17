# race_conditions_sim.py

"""
Definition: A race condition occurs when two or more threads/tasks access shared data and try to change it at the same time, leading to unpredictable results.
"""

def simulate_race_condition():
    print("Task A reads value: 10")
    print("Task B reads value: 10")
    print("Task A increments value to 11 and saves")
    print("Task B increments value to 11 and saves (OVERWRITING Task A!)")
    print("Final Value: 11 (Expected 12)")
    print("Solution: Use Locks or Mutexes.")

simulate_race_condition()
