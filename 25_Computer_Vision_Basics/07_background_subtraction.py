"""
PROPER DEFINITION:
Background subtraction is a technique in computer vision for extracting moving foreground 
objects from a sequence of images (video frames). It works by comparing the current 
frame with a reference frame (background). The simplest method involves taking the absolute 
difference between pixels in the background and current frame. Pixels with significant 
differences are considered part of the moving foreground. More advanced methods handle 
changing lighting conditions or dynamic backgrounds.
"""

import cv2
import numpy as np

def background_subtraction_demo():
    print("--- Background Subtraction Introduction ---")
    
    # Create a synthetic background image (600x600, BGR)
    background = np.zeros((600, 600, 3), dtype=np.uint8)
    # Fill background with a gray color (BGR: (100, 100, 100))
    background[:] = (100, 100, 100)
    
    # Create a current frame (background with a red rectangle added)
    frame = background.copy()
    cv2.rectangle(frame, (100, 100), (400, 400), (0, 0, 255), -1)
    
    # Compute absolute difference between background and frame
    # cv2.absdiff(src1, src2)
    diff = cv2.absdiff(background, frame)
    
    # Convert difference to grayscale for thresholding
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Thresholding to create a binary mask of moving objects
    # cv2.threshold(src, thresh, maxval, type)
    _, mask = cv2.threshold(gray_diff, 20, 255, cv2.THRESH_BINARY)
    
    print("Synthetic background and current frame (with a red rectangle) created.")
    print("Absolute difference computed and thresholded to isolate the moving object.")
    
    # Save outputs for verification
    cv2.imwrite("bg_sub_background.jpg", background)
    cv2.imwrite("bg_sub_frame.jpg", frame)
    cv2.imwrite("bg_sub_diff.jpg", diff)
    cv2.imwrite("bg_sub_mask.jpg", mask)
    print("Outputs saved: bg_sub_background.jpg, bg_sub_frame.jpg, bg_sub_diff.jpg, bg_sub_mask.jpg")

if __name__ == "__main__":
    background_subtraction_demo()
