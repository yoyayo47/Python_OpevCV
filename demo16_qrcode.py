import cv2
import os

import numpy
from matplotlib import pyplot as plt


def drawBBOX(image, bbox, result):
    color1 = (255, 0, 255)
    print(type(bbox), bbox.dtype)
    bbox = bbox.astype(int)
    print("轉換後", type(bbox), bbox.dtype)
    box1 = bbox[0]
    print(box1)
    p1 = (box1[0][0], box1[0][1])
    p2 = (box1[1][0], box1[1][1])
    p3 = (box1[2][0], box1[2][1])
    p4 = (box1[3][0], box1[3][1])

    # p1 = (int(bbox[0][0][0]), int(bbox[0][0][1]))
    # p2 = (int(bbox[0][1][0]), int(bbox[0][1][1]))
    # p3 = (int(bbox[0][2][0]), int(bbox[0][2][1]))
    # p4 = (int(bbox[0][3][0]), int(bbox[0][3][1]))
    cv2.line(image, p1, p2, color1, 4)
    cv2.line(image, p2, p3, color1, 4)
    cv2.line(image, p3, p4, color1, 4)
    cv2.line(image, p4, p1, color1, 4)
    cv2.imwrite(OUTPUT_FILE_NAME, image)
    plt.imshow(image)
    plt.title(result)
    plt.show()


BARCODE_FILE_NAME = "./images/barcode4.jpg"
OUTPUT_FILE_NAME = "./images/barcode4_output.jpg"
image = cv2.imread(BARCODE_FILE_NAME)
print(type(image))
result, bbox, rectifiedImage = cv2.QRCodeDetector().detectAndDecode(image)
print(type(result))
print("QR code解出的是:", result)
print("原始的bbox是:\n", bbox)
cv2.imshow("rectified image", rectifiedImage)
plt.imshow(rectifiedImage)
plt.show()
# cv2.waitKey(0)
if result != None:
    drawBBOX(image, bbox, result)

print(bbox)
