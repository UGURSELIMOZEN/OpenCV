# -*- coding: utf-8 -*-
import cv2
import numpy as np

resim  = cv2.imread("download.jpg")
resim2 = cv2.imread("download.jpg",0) ##RESMİMİZİ GRİ YAPMAK İÇİN##
print(type(resim))
cv2.imwrite("download1.jpg",resim2)
cv2.imshow("First_Image",resim)
cv2.imshow("Gray_Image",resim2)
cv2.waitKey(0)
cv2.destroyAllWindows()