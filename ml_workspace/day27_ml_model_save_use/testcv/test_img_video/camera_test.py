# pip install opencv-python

import cv2
import sys

print('Hello OpenCV', cv2.__version__)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print('Error opening video stream or file')
    sys.exit()
print('Fame width:', round(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('Fame height:', round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow('Video', frame)

    edge = cv2.Canny(frame, 50, 150)
    cv2.imshow('Edge', edge)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()