# -*- coding: utf-8 -*-

import cv2 
import numpy as np

image = cv2.imread("download.jpg")

stretched picture = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_REPLICATE)

mirrored_picture = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_REFLECT)

repeated picture = cv2.copyMakeBorder(image,100,100,100,100,cv2.BORDER_WRAP)

embraced picture = cv2.copyMakeBorder(image,50,50,50,50,cv2.BORDER_CONSTANT,value =[255,0,0])

# frame the desired region
cv2.rectangle(image,(30,200),(160,30),[0,255,0],3)
                 #   x1,y1    x2,y2     color   thickness

cv2.imshow("orjinal resim",image)
cv2.imshow("stretched picture",stretched picture)
cv2.imshow("mirrored_picture",mirrored_picture)
cv2.imshow("repeated picture",repeated picture)
cv2.imshow("embraced picture",embraced picture)

cv2.waitKey(0)
cv2.destroyAllWindows()
