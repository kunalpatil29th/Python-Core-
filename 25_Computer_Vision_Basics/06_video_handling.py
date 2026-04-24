"""
PROPER DEFINITION:
Video handling in computer vision involves reading, processing, and saving sequences of 
images (frames). OpenCV provides the `cv2.VideoCapture` class to interface with webcams 
or video files. Each frame is treated as a separate image, allowing for real-time 
processing within a loop. Background subtraction often requires capturing an initial 
static frame (background) and comparing it with subsequent dynamic frames to identify 
moving objects or changes.
"""

import cv2
import time

def video_handling_demo():
    print("--- Video Capture and Handling ---")
    
    # Initialize webcam (0 for default camera)
    # cap = cv2.VideoCapture(device_index)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    # Small delay to let camera initialize
    time.sleep(2)
    
    # Capture a static background frame
    # ret, frame = cap.read()
    # ret is a boolean indicating success, frame is the actual image
    ret, background = cap.read()
    
    if ret:
        print("Successfully captured background frame.")
        print(f"Frame dimensions: {background.shape}")
        
        # Save the background for later comparison
        cv2.imwrite("video_background.jpg", background)
        print("Background frame saved as 'video_background.jpg'")
    
    # In a real script, you'd use a loop to process frames
    # while cap.isOpened():
    #     ret, frame = cap.read()
    #     if not ret: break
    #     # Process frame here
    #     cv2.imshow("Frame", frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'): break
    
    # Always release the resource
    cap.release()
    print("Video capture resource released.")

if __name__ == "__main__":
    video_handling_demo()
