# -*- coding: utf-8 -*-

import cv2
import numpy as np

image = cv2.imread("download.jpg")

for i in range (200):               # format of image[y,x] 
    image [100,i]=[255,255,255]   # to make a change color that pointed pixels.

region = image [50:200,50:160]    # taking a defined part of image
# format of take from x1 to x2 and from y1 to y2 .

image [0:150,0:110] = region   # adding again the part to main image  that we have taken 

image [50:100,50:100,0]=255         # we colored the taken pixels to blue 
image [110:140,110:140,1]=255       # we colored the taken pixels to green 
image [150:170,150:170,2]=255       # we colored the taken pixels to red 

cv2.imshow("show",image)
cv2.imshow("parca",region)
cv2.waitKey(0)
cv2.destroyAllWindows()
