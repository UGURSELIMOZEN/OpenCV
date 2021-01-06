# -*- coding: utf-8 -*-
import cv2
import numpy as np

image  = cv2.imread("download.jpg")
image2 = cv2.imread("download.jpg",0) ##to make your image as gray##
print(type(image))
cv2.imwrite("download1.jpg",image2)
cv2.imshow("First_Image",image)
cv2.imshow("Gray_Image",image2)
cv2.waitKey(0)
cv2.destroyAllWindows()
