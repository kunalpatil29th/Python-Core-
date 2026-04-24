"""
PROPER DEFINITION:
Bitwise operations in computer vision are logical operations performed on pixel values of 
binary or grayscale images. They include AND, OR, NOT, and XOR. These operations are highly 
efficient and are used to manipulate specific parts of an image based on a binary mask. 
For instance, `cv2.bitwise_not(mask)` can invert a mask, where white pixels become black and 
vice versa, allowing for easy segmentation of both the object and its background.
"""

import cv2
import numpy as np

def bitwise_demo():
    print("--- Bitwise Operations in OpenCV ---")
    
    # Create two synthetic binary masks
    # (600x600, 1 channel, grayscale)
    mask1 = np.zeros((600, 600), dtype=np.uint8)
    mask2 = np.zeros((600, 600), dtype=np.uint8)
    
    # White rectangle (foreground)
    cv2.rectangle(mask1, (100, 100), (400, 400), 255, -1)
    
    # White circle (foreground)
    cv2.circle(mask2, (300, 300), 150, 255, -1)
    
    # Bitwise AND (Intersection)
    # cv2.bitwise_and(src1, src2)
    bit_and = cv2.bitwise_and(mask1, mask2)
    
    # Bitwise OR (Union)
    # cv2.bitwise_or(src1, src2)
    bit_or = cv2.bitwise_or(mask1, mask2)
    
    # Bitwise XOR (Exclusive OR)
    # cv2.bitwise_xor(src1, src2)
    bit_xor = cv2.bitwise_xor(mask1, mask2)
    
    # Bitwise NOT (Inversion)
    # cv2.bitwise_not(src)
    bit_not = cv2.bitwise_not(mask1)
    
    print("Synthetic masks (rectangle and circle) created.")
    print("Bitwise AND, OR, XOR, and NOT operations performed.")
    
    # Save outputs for verification
    cv2.imwrite("bitwise_mask1.jpg", mask1)
    cv2.imwrite("bitwise_mask2.jpg", mask2)
    cv2.imwrite("bitwise_and.jpg", bit_and)
    cv2.imwrite("bitwise_or.jpg", bit_or)
    cv2.imwrite("bitwise_xor.jpg", bit_xor)
    cv2.imwrite("bitwise_not.jpg", bit_not)
    print("Outputs saved: bitwise_mask1.jpg, bitwise_mask2.jpg, bitwise_and.jpg, bitwise_or.jpg, bitwise_xor.jpg, bitwise_not.jpg")

if __name__ == "__main__":
    bitwise_demo()
