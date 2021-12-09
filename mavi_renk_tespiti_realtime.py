import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    frame = cv.flip(frame, 1)
    # hsv renk araligina ceviyoruz bunun nedeni renkleri alt tonlarina daha rahat ayirabilmeiz icin
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    hsv_frame_blur = cv.medianBlur(hsv_frame, 35)


    '''
    
    s = degerini solukluk degerini arttirilidiginda daha canli bir renk olur
    v = parlaklik
    h = renk regeri  renki degistiriyor
    
    '''

    # [H,S,V]

    lower_blue = np.array([85, 120, 0])
    upper_blue = np.array([126, 255, 255])
    # alt ve ust renkleri tutacak digerlerini silecektir.
    green_mask = cv.inRange(hsv_frame_blur, lower_green, upper_green)
    green_mask_blur = cv.inRange(hsv_frame_blur, lower_green, upper_green)

    #mavi reng gozukmesi icin yazildi
    green = cv.bitwise_and(frame, frame, mask=green_mask_blur)

    cv.imshow('webcam', frame)
    cv.imshow('green_mask', green_mask)
    cv.imshow('green_blur', green)
    if cv.waitKey(1) & 0XFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
