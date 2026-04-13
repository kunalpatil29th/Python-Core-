# logging_basics.py

"""
Definition: The 'logging' module defines functions and classes which implement a flexible 
event logging system for applications and libraries.
"""

import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')

def perform_task():
    logging.debug("Starting the task...")
    logging.info("Task is in progress.")
    try:
        x = 1 / 0
    except ZeroDivisionError:
        logging.error("Attempted to divide by zero!")
    logging.warning("Task completed with some issues.")

perform_task()
