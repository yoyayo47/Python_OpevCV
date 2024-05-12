import cv2

import os
import shutil

IMAGE_DIRS = 'input/images/sample'
shutil.rmtree(IMAGE_DIRS)
IMAGE_FILE = IMAGE_DIRS + "/%d.jpg"
os.makedirs(IMAGE_DIRS, exist_ok=True)

cap = cv2.VideoCapture(1)  # 同學要改成0
counter = 0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('sample image', gray)
    k = cv2.waitKey(20)
    if k == ord('q'):
        break
    elif k == ord('s'):
        filename = IMAGE_FILE % counter
        print("image saved as:{}".format(filename))
        # cv2.imwrite(filename, frame)
        cv2.imwrite(filename, gray)
        counter += 1

cap.release()
cv2.destroyAllWindows()
