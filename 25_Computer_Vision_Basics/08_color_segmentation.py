"""
PROPER DEFINITION:
Color segmentation is a computer vision technique for identifying and isolating objects 
of a specific color within an image. It involves converting an image into a color space 
like HSV and then creating binary masks based on a predefined range of color values. 
For instance, to segment red objects, you may need to combine two masks because red 
is represented at both ends of the Hue scale (0-10 and 170-180 in OpenCV). 
The final result is a binary image where white pixels represent the target color.
"""

import cv2
import numpy as np

def color_segmentation_demo():
    print("--- Color Segmentation in HSV ---")
    
    # Create a synthetic image with red shapes (BGR: (0, 0, 255))
    image = np.zeros((600, 600, 3), dtype=np.uint8)
    
    # Red rectangle (BGR: (0, 0, 255))
    cv2.rectangle(image, (100, 100), (300, 300), (0, 0, 255), -1)
    
    # Red circle (BGR: (0, 0, 255))
    cv2.circle(image, (450, 450), 100, (0, 0, 255), -1)
    
    # Blue rectangle (BGR: (255, 0, 0)) - not red
    cv2.rectangle(image, (350, 100), (550, 300), (255, 0, 0), -1)
    
    # Convert image to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define red color range for color segmentation
    # Red 1 (0-10)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    
    # Red 2 (170-180)
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    
    # Create masks for red color
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    
    # Combine both masks using addition
    mask = mask1 + mask2
    
    # Bitwise AND to extract only red objects from the original image
    res = cv2.bitwise_and(image, image, mask=mask)
    
    print("Synthetic Image with red and blue shapes created.")
    print("Red color segmentation performed by combining two HSV masks.")
    print("Red objects isolated from the original image.")
    
    # Save outputs for verification
    cv2.imwrite("segment_original.jpg", image)
    cv2.imwrite("segment_mask.jpg", mask)
    cv2.imwrite("segment_result.jpg", res)
    print("Outputs saved: segment_original.jpg, segment_mask.jpg, segment_result.jpg")

if __name__ == "__main__":
    color_segmentation_demo()
