"""
PROPER DEFINITION:
Image blending is the process of combining two or more images into a single composite image. 
In computer vision, this is often done using a weighted sum, where each pixel's color in the 
final image is a weighted average of corresponding pixels in the input images. 
The function `cv2.addWeighted` is used for this purpose. In applications like the 
Invisible Cloak, blending is used to combine the background (revealed where the cloak is) 
with the original frame (visible everywhere else).
"""

import cv2
import numpy as np

def image_blending_demo():
    print("--- Image Blending and Composite Images ---")
    
    # Create two synthetic images (600x600, BGR)
    # Background (Blue-ish)
    background = np.zeros((600, 600, 3), dtype=np.uint8)
    background[:] = (255, 100, 100)  # BGR
    
    # Current Frame (Green-ish)
    frame = np.zeros((600, 600, 3), dtype=np.uint8)
    frame[:] = (100, 255, 100)  # BGR
    
    # Create a mask (e.g., a circle in the middle)
    mask = np.zeros((600, 600), dtype=np.uint8)
    cv2.circle(mask, (300, 300), 200, 255, -1)
    
    # Invert the mask
    mask_inv = cv2.bitwise_not(mask)
    
    # Extract background part where mask is white
    res1 = cv2.bitwise_and(background, background, mask=mask)
    
    # Extract frame part where mask is black (mask_inv is white)
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # Blend/Combine both results
    # final = alpha*res1 + beta*res2 + gamma
    # Here alpha=1, beta=1, gamma=0 for simple combination
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    print("Synthetic background and frame images created.")
    print("Circular mask and its inverse applied to extract parts from both.")
    print("Results combined using cv2.addWeighted to create the final composite image.")
    
    # Save outputs for verification
    cv2.imwrite("blend_background.jpg", background)
    cv2.imwrite("blend_frame.jpg", frame)
    cv2.imwrite("blend_mask.jpg", mask)
    cv2.imwrite("blend_final.jpg", final_output)
    print("Outputs saved: blend_background.jpg, blend_frame.jpg, blend_mask.jpg, blend_final.jpg")

if __name__ == "__main__":
    image_blending_demo()
