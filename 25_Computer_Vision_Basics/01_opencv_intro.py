"""
PROPER DEFINITION:
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. 
It provides a common infrastructure for computer vision applications and accelerates the use of machine perception 
in commercial products. It contains more than 2500 optimized algorithms, including tools for image processing, 
video analysis, object detection, and machine learning.
"""

import cv2
import numpy as np

def opencv_basics_demo():
    print("--- OpenCV Basics Introduction ---")
    
    # In a real environment, you would use cv2.imread('path_to_image.jpg')
    # For this simulation, we'll create a synthetic image using NumPy
    # Create a black image (500x500 pixels, 3 channels for BGR)
    image = np.zeros((500, 500, 3), dtype=np.uint8)
    
    # Drawing a blue rectangle
    # cv2.rectangle(image, start_point, end_point, color, thickness)
    # Color in OpenCV is BGR (Blue, Green, Red)
    cv2.rectangle(image, (100, 100), (400, 400), (255, 0, 0), 5)
    
    # Drawing a green circle
    # cv2.circle(image, center, radius, color, thickness)
    cv2.circle(image, (250, 250), 50, (0, 255, 0), -1)  # -1 thickness fills the circle
    
    # Adding text
    # cv2.putText(image, text, org, fontFace, fontScale, color, thickness)
    cv2.putText(image, "OpenCV Basics", (150, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    print("Synthetic image created with a rectangle, circle, and text.")
    print(f"Image Shape: {image.shape}")
    print(f"Total Pixels: {image.size}")
    
    # In a real script, you would use:
    # cv2.imshow("Demo", image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    
    # We can save it to verify
    cv2.imwrite("opencv_intro_output.jpg", image)
    print("Image saved as 'opencv_intro_output.jpg'")

if __name__ == "__main__":
    opencv_basics_demo()
