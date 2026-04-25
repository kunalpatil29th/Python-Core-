"""
PROPER DEFINITION:
The Invisibility Cloak algorithm is a multi-step computer vision process that creates the 
illusion of transparency. It involves: 1) Capturing a static background frame. 2) Identifying 
a specific color (the cloak) in the current frame using HSV thresholding. 3) Creating a 
mask of the cloak and its inverse. 4) Extracting the background where the cloak is present. 
5) Extracting the current frame where the cloak is NOT present. 6) Combining both 
results to produce the final "invisible" output.
"""

import cv2
import numpy as np

def cloak_logic_demo():
    print("--- Virtual Invisibility Cloak Logic ---")
    
    # 1. Create a synthetic background (Blue room)
    background = np.zeros((500, 500, 3), dtype=np.uint8)
    background[:] = (255, 0, 0) # BGR Blue
    
    # 2. Create a current frame (Blue room with a Red cloak)
    frame = background.copy()
    cv2.rectangle(frame, (150, 150), (350, 350), (0, 0, 255), -1) # BGR Red cloak
    
    # 3. Convert to HSV and create mask for Red
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    
    # 4. Refine mask (Morphological Ops)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))
    
    # 5. Invert mask
    mask_inv = cv2.bitwise_not(mask)
    
    # 6. Extract parts
    # res1: background where cloak is
    res1 = cv2.bitwise_and(background, background, mask=mask)
    # res2: frame where cloak is NOT
    res2 = cv2.bitwise_and(frame, frame, mask=mask_inv)
    
    # 7. Final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)
    
    print("Cloak logic executed: Background revealed where Red was detected.")
    print(f"Original Frame has Red; Final Output at (250, 250) is {final_output[250, 250]} (Blue).")
    
    # Save for verification
    cv2.imwrite("cloak_final_demo.jpg", final_output)
    print("Demo output saved as 'cloak_final_demo.jpg'")

if __name__ == "__main__":
    cloak_logic_demo()
