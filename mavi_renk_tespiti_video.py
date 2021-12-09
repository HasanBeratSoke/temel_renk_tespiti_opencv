import cv2 as cv
import numpy as np

cap = cv.VideoCapture('data/video/pool2.mp4')

while True:
    ret, frame = cap.read()

    frame_hvs = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    frame_hvs_blur = cv.medianBlur(frame, 5)

    '''
    lower_blue = np.array([80, 90, 0])
    upper_blue = np.array([150, 255, 255])

    '''
    lower_blue = np.array([80, 60, 60])
    upper_blue = np.array([126, 300, 255])

    blue_mask = cv.inRange(frame_hvs, lower_blue, upper_blue)
    cv.imshow('orj', frame)
    cv.imshow('video', blue_mask)

    if cv.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
