import cv2
import math
from PIL import ImageFont, ImageDraw, Image
import numpy as np

#FONT_PATH = "./fonts/NotoSerifCJK-Regular.ttc"
FONT_PATH = "./fonts/NotoSerifCJKtc-VF.ttf"
FILE_NAME = "./images/google_seminar.jpg"
# MESSAGE = '''press esc to leave, press c to clear'''
MESSAGE = '''按下esc離開, press c to clear'''
WINDOW_NAME = "window1"

center = [0, 0]
circlefence = [(0, 0)]


def drawCircleCallback(action, x, y, flags, userData):
    # print("callback is called", action)
    global center
    global circlefence
    coordinate = (x, y)
    if action == cv2.EVENT_LBUTTONDOWN:
        center = [coordinate]
        cv2.circle(source, center[0], 1, (255, 255, 0), 6, cv2.LINE_AA)
    elif action == cv2.EVENT_LBUTTONUP:
        circlefence = [coordinate]
        radius = math.sqrt(math.pow(center[0][0] - circlefence[0][0], 2) +
                           math.pow(center[0][1] - circlefence[0][1], 2))
        cv2.circle(source, center[0], int(radius), (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow(WINDOW_NAME, source)
        print("左鍵放開", coordinate)
    pass


source = cv2.imread(FILE_NAME, 1)
print("原始影像是", source.shape)
dummy = source.copy()
cv2.namedWindow(WINDOW_NAME)
cv2.setMouseCallback(WINDOW_NAME, drawCircleCallback)
k = 0

font = ImageFont.truetype(FONT_PATH, 36)

while k != 27:  # 使用者按下的不是esc
    # nd-array --> pil image
    imagePillow = Image.fromarray(source)
    draw = ImageDraw.Draw(imagePillow)
    draw.text((40, 40), MESSAGE, font=font, fill=(255, 255, 0, 255))
    # pil image --> ndarray
    source = np.array(imagePillow)
    cv2.imshow(WINDOW_NAME, source)
    k = cv2.waitKey(20)  # parameter --> timeout limit
    # print("輸入的按鈕是:", k)
    if k == ord('c'):
        source = dummy.copy()
