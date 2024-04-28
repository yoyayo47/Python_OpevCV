import cv2
import sys
from pprint import pprint
pprint("使用的Python是:{}".format(sys.executable))
print("路徑是:")
pprint(sys.path)
print("OpenCV 版本是:",cv2.__version__)