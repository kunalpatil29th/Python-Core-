"""
PROPER DEFINITION:
Morphological operations are techniques for image processing based on the shape and structure of 
objects in a binary image. The two fundamental operations are dilation and erosion. Dilation 
expands the boundaries of white regions (foreground) while erosion shrinks them. Combining 
these operations gives rise to advanced techniques like opening (erosion followed by dilation) 
to remove noise, and closing (dilation followed by erosion) to fill small holes in the foreground.
"""

import cv2
import numpy as np

def morphological_demo():
    print("--- Morphological Operations Intro ---")
    
    # Create a synthetic mask with white pixels and some noise
    # (600x600, 1 channel, grayscale)
    mask = np.zeros((600, 600), dtype=np.uint8)
    
    # White rectangle (foreground)
    cv2.rectangle(mask, (100, 100), (300, 300), 255, -1)
    
    # Add noise (small white pixels in background)
    mask[50:60, 50:60] = 255
    mask[400:410, 400:410] = 255
    
    # Define a kernel (3x3 square)
    kernel = np.ones((3, 3), np.uint8)
    
    # Erosion (shrinks foreground)
    # cv2.erode(src, kernel, iterations)
    erosion = cv2.erode(mask, kernel, iterations=1)
    
    # Dilation (expands foreground)
    # cv2.dilate(src, kernel, iterations)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    
    # Opening (erosion then dilation)
    # cv2.morphologyEx(src, op, kernel)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    
    # Closing (dilation then erosion)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    print("Synthetic mask with noise created.")
    print("Erosion, Dilation, Opening, and Closing operations performed.")
    
    # Save outputs for verification
    cv2.imwrite("morph_original_mask.jpg", mask)
    cv2.imwrite("morph_erosion.jpg", erosion)
    cv2.imwrite("morph_dilation.jpg", dilation)
    cv2.imwrite("morph_opening.jpg", opening)
    cv2.imwrite("morph_closing.jpg", closing)
    print("Outputs saved: morph_original_mask.jpg, morph_erosion.jpg, morph_dilation.jpg, morph_opening.jpg, morph_closing.jpg")

if __name__ == "__main__":
    morphological_demo()
