"""
PROPER DEFINITION:
Image masking is a process of defining a specific region of an image and performing operations 
only on that region. It uses binary images (masks), where each pixel is either 0 (black, representing 
the background or 'off' state) or 255 (white, representing the foreground or 'on' state). 
In computer vision, masking is commonly used to extract or hide specific objects based on their 
color or shape.
"""

import cv2
import numpy as np

def image_masking_demo():
    print("--- Image Masking Introduction ---")
    
    # Create a synthetic image with blue and red shapes
    # (600x600, 3 channels, BGR)
    image = np.zeros((600, 600, 3), dtype=np.uint8)
    
    # Blue rectangle (BGR: (255, 0, 0))
    cv2.rectangle(image, (100, 100), (300, 300), (255, 0, 0), -1)
    
    # Red rectangle (BGR: (0, 0, 255))
    cv2.rectangle(image, (350, 350), (550, 550), (0, 0, 255), -1)
    
    # Define color range for blue in HSV (Hue: 110-130)
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # Create a mask for blue pixels
    # cv2.inRange(src, lowerb, upperb)
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
    
    # Apply mask to the original image using bitwise AND
    # res = cv2.bitwise_and(src1, src2, mask=mask)
    res = cv2.bitwise_and(image, image, mask=mask)
    
    print("Synthetic Image with blue and red shapes created.")
    print("Blue mask created using cv2.inRange.")
    print("Mask applied to original image to isolate blue pixels.")
    
    # Mask shape: (600, 600) - single channel
    print(f"Mask Shape: {mask.shape}")
    print(f"Mask Type: {mask.dtype}")
    
    # Save outputs for verification
    cv2.imwrite("original_image.jpg", image)
    cv2.imwrite("blue_mask.jpg", mask)
    cv2.imwrite("masked_result.jpg", res)
    print("Outputs saved: original_image.jpg, blue_mask.jpg, masked_result.jpg")

if __name__ == "__main__":
    image_masking_demo()
