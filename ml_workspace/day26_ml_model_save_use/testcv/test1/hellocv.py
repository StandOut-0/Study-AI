# pip install opencv-python

import cv2
import sys

print('Hello OpenCV', cv2.__version__)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    pass
