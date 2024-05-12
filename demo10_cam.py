import cv2

cap = cv2.VideoCapture(1)

while True:
    r, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('this is me!', gray) # gray/frame bw/color

    if cv2.waitKey(50) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
