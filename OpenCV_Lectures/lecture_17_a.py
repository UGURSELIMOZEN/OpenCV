# -*- coding: utf-8 -*-

import cv2
import numpy as np

resim = cv2.imread("mecnun.jpg")

laplacian = cv2.Laplacian(resim,cv2.CV_64F)

sobel_dikey =cv2.Sobel(resim,cv2.CV_64F,1,0,ksize = 5)

sobel_yatay =cv2.Sobel(resim,cv2.CV_64F,0,1,ksize = 5)

##  cv2.imshow("sobel_yatay",sobel_yatay)
cv2.imshow("sobel_dikey",sobel_dikey)
cv2.imshow("laplacian",laplacian)
cv2.imshow("orjinal",resim)

cv2.waitKey(0)
cv2.destroyAllWindows()