import cv2
import sys
import os
import matplotlib.pyplot as plt

basepath = os.path.dirname(__file__)
print(basepath)
img_path = os.path.join(basepath, "../images/cat.bmp")
imgBGR = cv2.imread(img_path)

if False: 
    img = cv2.imread(img_path)

    if img is None:
        print("Error opening image")
        sys.exit()

    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if False:
    # imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
    # cv2.imshow("Image", imgRGB)
    plt.axis("off")
    # plt.imshow(imgRGB)
    # plt.imshow(imgBGR)


    plt.subplot(121),plt.axis("off"), plt.imshow(imgBGR)
    plt.subplot(122),plt.axis("off"), plt.imshow(imgBGR)
    plt.show()


if False:
    imgGrey = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("Image", imgGrey)
    # cv2.waitKey(0)

    import numpy as np
    result = np.hstack((imgGrey, imgGrey, imgGrey))
    cv2.imshow("Image", result)
    cv2.waitKey(0)
    

