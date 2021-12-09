import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

su2 = cv.imread('data/foto/havuz3.jpg')

# sharpen filitresi
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

su2_hsv = cv.cvtColor(su2, cv.COLOR_BGR2HSV)

su2_hsv_blur = cv.medianBlur(su2_hsv, 35)
# filitrenin uygulanmasi
img_kernel = cv.filter2D(su2_hsv, ddepth=-1, kernel=kernel)

# goruntudeki gurultuyu engelemek icin median blur kullanildi
img_kernel_blur = cv.medianBlur(img_kernel, 35)
img_gausblur = cv.GaussianBlur(su2_hsv, (3, 3), 0)
cv.imshow('hsv', su2_hsv)

lower_blue = np.array([85, 120, 0])
upper_blue = np.array([100, 255, 255])

#inrange fonksiyonu kullanilarak verdigimiz araliklari secmesini istiyoruz
#yani eger araligin icinde ise beyaz, degil ise siyah donusturuluyor
blue_mask = cv.inRange(su2_hsv, lower_blue, upper_blue)
blue_mask_blur = cv.inRange(su2_hsv_blur, lower_blue, upper_blue)
blue_mask_kernel = cv.inRange(img_kernel, lower_blue, upper_blue)
blue_mask_kernel_blur = cv.inRange(img_kernel_blur, lower_blue, upper_blue)
blue_mask_gausblur = cv.inRange(img_gausblur, lower_blue, upper_blue)
while True:
    cv.imshow('normal', su2)
    cv.imshow('mask_blur', blue_mask_blur)
    cv.imshow('blue_mask', blue_mask)
    cv.imshow('kernel_blur', blue_mask_kernel_blur)
    cv.imshow('kernel', blue_mask_kernel)
    cv.imshow('gausblur', blue_mask_gausblur)

    if cv.waitKey(1) & 0XFF == ord('q'):
        break

cv.destroyAllWindows()
