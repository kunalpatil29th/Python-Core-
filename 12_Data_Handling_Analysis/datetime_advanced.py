# datetime_advanced.py

"""
Definition: The 'datetime' module supplies classes for manipulating dates and times. 
Advanced usage includes timezones, deltas, and formatting.
"""

from datetime import datetime, timedelta

# Current time
now = datetime.now()
print(f"Now: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Adding time (Timedelta)
tomorrow = now + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

# Difference between dates
bday = datetime(now.year, 1, 1)
diff = now - bday
print(f"Days passed this year: {diff.days}")
