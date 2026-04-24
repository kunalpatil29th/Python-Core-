"""
PROPER DEFINITION:
Color spaces are mathematical models used to represent color information as a set of numbers. 
In computer vision, the most common color spaces are BGR (Blue-Green-Red), which is the default for OpenCV, 
and HSV (Hue-Saturation-Value). While BGR is used for displaying colors on monitors, HSV is more useful for 
segmenting objects based on their color because it separates color information (Hue) from its intensity (Value) 
and purity (Saturation).
"""

import cv2
import numpy as np

def color_space_demo():
    print("--- Color Space Conversion Demo ---")
    
    # Create a synthetic frame (600x600, 3 channels) with some red pixels
    # In OpenCV, Red is roughly H: 0-10 and 170-180
    frame = np.zeros((600, 600, 3), dtype=np.uint8)
    
    # Draw some red rectangles (BGR: (0, 0, 255))
    cv2.rectangle(frame, (100, 100), (300, 300), (0, 0, 255), -1)
    
    # Draw some blue rectangles (BGR: (255, 0, 0))
    cv2.rectangle(frame, (350, 100), (550, 300), (255, 0, 0), -1)
    
    print("Original BGR Frame Created.")
    
    # Convert BGR to HSV
    # cv2.cvtColor(src, code)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    print("Converted BGR Frame to HSV.")
    print(f"BGR Shape: {frame.shape}")
    print(f"HSV Shape: {hsv_frame.shape}")
    
    # HSV components:
    # H (Hue): 0-179 (represents the color itself)
    # S (Saturation): 0-255 (represents the purity/intensity of the color)
    # V (Value): 0-255 (represents the brightness)
    
    # In a real script, you'd use:
    # cv2.imshow("BGR", frame)
    # cv2.imshow("HSV", hsv_frame)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # Save the HSV frame (it will look weird if displayed as BGR)
    cv2.imwrite("hsv_converted_output.jpg", hsv_frame)
    print("HSV frame saved as 'hsv_converted_output.jpg'")

if __name__ == "__main__":
    color_space_demo()
