"""
PROPER DEFINITION:
Object tracking in computer vision is the process of locating a moving object (or multiple 
objects) over time using a camera. A common method for simple tracking involves 
creating a binary mask of the target object and then finding its contours (boundary 
points). By calculating the bounding rectangle or the centroid of the contour, 
the object's position in each frame can be identified and tracked across the 
video sequence.
"""

import cv2
import numpy as np

def object_tracking_demo():
    print("--- Simple Object Tracking Concepts ---")
    
    # Create a synthetic image with a moving target (600x600, BGR)
    frame = np.zeros((600, 600, 3), dtype=np.uint8)
    
    # Target (Red rectangle)
    cv2.rectangle(frame, (150, 150), (250, 250), (0, 0, 255), -1)
    
    # Convert image to grayscale for easier segmentation
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Create a binary mask of the target (Red)
    # _, mask = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
    
    # Define red color range for color segmentation
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    
    # Find contours in the binary mask
    # cv2.findContours(src, mode, method)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Track the largest contour (if any)
    if contours:
        # Get the largest contour based on area
        c = max(contours, key=cv2.contourArea)
        
        # Get the bounding rectangle coordinates
        # x, y, w, h = cv2.boundingRect(contour)
        x, y, w, h = cv2.boundingRect(c)
        
        # Draw a green bounding box around the tracked object
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        
        # Draw the centroid (center of the object)
        M = cv2.moments(c)
        if M["m00"] != 0:
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
            print(f"Object Tracked at Centroid: ({cx}, {cy})")
    
    print("Synthetic Image with red target created.")
    print("Contour analysis used to identify and track the target.")
    print("Bounding box and centroid drawn for visualization.")
    
    # Save output for verification
    cv2.imwrite("tracking_output.jpg", frame)
    print("Output saved: tracking_output.jpg")

if __name__ == "__main__":
    object_tracking_demo()
