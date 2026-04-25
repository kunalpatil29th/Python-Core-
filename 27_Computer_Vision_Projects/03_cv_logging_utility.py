"""
PROPER DEFINITION:
Structured logging in computer vision applications involves recording runtime events, 
configuration parameters, and errors in a consistent format. This is crucial for debugging 
complex pipelines where visual output alone might not explain why a specific frame 
failed to process. Using Python's `logging` module, developers can track application 
flow, performance metrics, and hardware initialization status.
"""

import logging
import sys

def setup_cv_logger():
    # Create a custom logger
    logger = logging.getLogger("CV_Project")
    logger.setLevel(logging.DEBUG)

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler("cv_app.log")
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    # Create formatters and add to handlers
    # Example format: 2026-04-25 10:00:00 - CV_Project - INFO - Message
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    
    return logger

def logging_demo():
    print("--- Structured Logging for CV ---")
    logger = setup_cv_logger()
    
    logger.info("Initializing Camera...")
    # Simulate a check
    camera_ready = True
    if camera_ready:
        logger.info("Camera started successfully.")
    else:
        logger.error("Failed to open camera device!")

    logger.debug("Processing Frame #1245...")
    logger.info("HSV Tuning: L_H=0, U_H=10 applied.")
    
    print("Logs have been printed to console and saved to 'cv_app.log'.")

if __name__ == "__main__":
    logging_demo()
