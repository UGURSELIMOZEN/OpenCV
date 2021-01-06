# -*- coding: utf-8 -*-

import cv2
import numpy as np

image = cv2.imread("mecnun.jpg")

laplacian = cv2.Laplacian(image,cv2.CV_64F)

sobel_vertical =cv2.Sobel(image,cv2.CV_64F,1,0,ksize = 5)

sobel_horizontal =cv2.Sobel(image,cv2.CV_64F,0,1,ksize = 5)

##  cv2.imshow("sobel_vertical",sobel_horizontal)
cv2.imshow("sobel_vertical",sobel_vertical)
cv2.imshow("laplacian",laplacian)
cv2.imshow("original",image)

cv2.waitKey(0)
cv2.destroyAllWindows()
