"""
PROPER DEFINITION:
Object-Oriented Programming (OOP) in computer vision allows for the encapsulation of 
complex processing pipelines into reusable classes. For instance, an `InvisibilityCloak` 
class can manage its own background reference, HSV parameters, and processing methods. 
This approach promotes code reuse, easier testing, and clear separation of concerns 
between hardware interfacing (camera), image processing (masks), and UI (display).
"""

import cv2
import numpy as np

class CloakProcessor:
    """Encapsulates the image processing logic for the Invisibility Cloak."""
    
    def __init__(self, lower_hsv, upper_hsv):
        self.lower_hsv = np.array(lower_hsv)
        self.upper_hsv = np.array(upper_hsv)
        self.background = None

    def set_background(self, frame):
        """Stores the static background frame."""
        self.background = frame
        print("Background frame stored.")

    def process_frame(self, frame):
        """Applies the cloak algorithm to a single frame."""
        if self.background is None:
            return frame

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_hsv, self.upper_hsv)
        
        # Simple refinement
        mask = cv2.medianBlur(mask, 3)
        mask_inv = cv2.bitwise_not(mask)

        # Combine background and current frame
        part1 = cv2.bitwise_and(self.background, self.background, mask=mask)
        part2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
        
        return cv2.addWeighted(part1, 1, part2, 1, 0)

def oop_cv_demo():
    print("--- OOP Principles in Computer Vision ---")
    
    # Initialize processor with Red HSV range
    processor = CloakProcessor([0, 120, 70], [10, 255, 255])
    
    # Simulate background and frame
    bg = np.zeros((400, 400, 3), dtype=np.uint8)
    bg[:] = (0, 255, 0) # Green background
    
    frame = bg.copy()
    cv2.circle(frame, (200, 200), 50, (0, 0, 255), -1) # Red object
    
    processor.set_background(bg)
    result = processor.process_frame(frame)
    
    print(f"Frame processed using CloakProcessor class.")
    print(f"Resulting pixel at center: {result[200, 200]} (Expected Green: [0 255 0])")

if __name__ == "__main__":
    oop_cv_demo()
