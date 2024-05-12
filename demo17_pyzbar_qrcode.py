import pyzbar as pyz
from pyzbar import pyzbar
import cv2
import numpy as np

print("pyzbar version=", pyz.__version__)


def decode(image):
    decodedObjects = pyzbar.decode(image)
    print(type(decodedObjects))
    for obj in decodedObjects:
        print(type(obj))
        print(obj.type)
        print(obj.data)
    return decodedObjects


def display(image, decodedObjects):
    for obj in decodedObjects:
        points = obj.polygon
        print("解讀到的多邊型是:", points)
        if len(points) > 4:
            hull = cv2.convexHull(np.array([p for p in points], dtype=float))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        n = len(hull)
        for j in range(0, n):
            cv2.line(image, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)
    cv2.imshow("Result", image)
    cv2.waitKey(0)


FILE_NAME = "./images/sample.png"
# FILE_NAME = "./images/invoice2.png"

image = cv2.imread(FILE_NAME)
decodedObjects = decode(image)
display(image, decodedObjects)
