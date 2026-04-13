# subprocess_basics.py

"""
Definition: The 'subprocess' module allows you to spawn new processes, connect to their 
input/output/error pipes, and obtain their return codes.
"""

import subprocess

def run_command():
    print("Running system command 'echo'...")
    try:
        # Running a simple echo command
        result = subprocess.run(["echo", "Hello from Subprocess"], capture_output=True, text=True, shell=True)
        print(f"Command Output: {result.stdout.strip()}")
    except Exception as e:
        print(f"Error running command: {e}")

run_command()
