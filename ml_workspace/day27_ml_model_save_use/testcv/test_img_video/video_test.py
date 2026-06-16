import cv2
import sys
import os
import matplotlib.pyplot as plt

basepath = os.path.dirname(__file__)
print(basepath)
video_path = os.path.join(basepath, "../multi/vtest.avi")
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error opening video stream or file")
    sys.exit()

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(cap.get(cv2.CAP_PROP_FPS))




if True:
    video_name = "output.avi"
    out = cv2.VideoWriter(video_name,
                          cv2.VideoWriter_fourcc(*'XVID'),
                          10,
                          (768, 576))
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)

    out.release()
    cv2.destroyAllWindows()