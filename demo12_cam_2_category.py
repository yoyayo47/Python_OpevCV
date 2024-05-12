import cv2

import os
import shutil

# IMAGE_DIRS = 'input/images/sample'
POSITIVE_IMAGE_DIRS = 'input/images/positive'
NEGATIVE_IMAGE_DIRS = 'input/images/negative'
# comment these when first run
shutil.rmtree(POSITIVE_IMAGE_DIRS, ignore_errors=True)
shutil.rmtree(NEGATIVE_IMAGE_DIRS, ignore_errors=True)
POSITIVE_IMAGE_FILE = POSITIVE_IMAGE_DIRS + "/%d.jpg"
NEGATIVE_IMAGE_FILE = NEGATIVE_IMAGE_DIRS + '/%d.jpg'
os.makedirs(POSITIVE_IMAGE_DIRS, exist_ok=True)
os.makedirs(NEGATIVE_IMAGE_DIRS, exist_ok=True)

cap = cv2.VideoCapture(1)  # 同學要改成0
pCounter = 0
nCounter = 0
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('sample image', gray)
    k = cv2.waitKey(20)
    if k == ord('q'):
        break
    elif k == ord('p'):  # positive
        cv2.imwrite(POSITIVE_IMAGE_FILE % pCounter, gray)
        pCounter += 1
        print(f"[+]有{pCounter}張樣本")

    elif k == ord('n'):  # negative
        cv2.imwrite(NEGATIVE_IMAGE_FILE % nCounter, gray)
        nCounter += 1
        print(f"[-]有{nCounter}張樣本")


cap.release()
cv2.destroyAllWindows()
