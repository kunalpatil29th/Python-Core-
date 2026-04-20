# subprocess_async.py

"""
Definition: Asynchronous subprocesses allow Python programs to run external shell commands or applications 
without blocking the main event loop. This is achieved using 'asyncio.create_subprocess_exec()' 
or 'asyncio.create_subprocess_shell()'. 
These methods return a 'Process' object that can be awaited to get the output or status.
"""

import asyncio

async def run_shell_command(command):
    """Runs a shell command asynchronously and returns the output."""
    print(f"Executing command: {command}")
    
    # Create the subprocess
    process = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )

    # Wait for the process to complete and capture output
    stdout, stderr = await process.communicate()

    if stdout:
        print(f"[stdout]\n{stdout.decode().strip()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode().strip()}")
    
    print(f"Command finished with exit code: {process.returncode}")

async def main():
    # Example 1: Run a simple command
    await run_shell_command("echo Hello from Async Subprocess!")

    # Example 2: Run a directory listing command
    await run_shell_command("dir") # Windows command

if __name__ == "__main__":
    asyncio.run(main())
