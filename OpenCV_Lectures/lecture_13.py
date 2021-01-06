# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera =cv2.VideoCapture(0)

low  = np.array([20,100,150])
high = np.array([37,255,255])     

# low  = np.array([20, 0, 0])
# high = np.array([37, 255, 255])     # filtering for yellow color

# low  = np.array([0, 0, 0])
# high = np.array([10, 255, 255])     # filtering for red color

# low  = np.array([85, 0, 0])
# high = np.array([100, 255, 255])     # filtering for light blue color

# low  = np.array([45, 0, 0])
# high = np.array([75, 255, 255])     # filtering for green color
while True:
    
    ret,frame = camera.read()
    
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    mask =cv2.inRange(hsv,low,high)
    
    last_image = cv2.bitwise_and(frame,frame,mask = mask)
    
    ## 1.SMOOTHED FILTER
#    kernel = np.ones((15,15),dtype= np.float32) / 255
#    smoothed =cv2.filter2D(last_image,-1,kernel)
    
    ## 2.BLUR FILTER
#    blur =cv2.GaussianBlur(last_image,(15,15),0)
    
    ## 3.MEDIAN FILTER
    median =cv2.medianBlur(last_image,15)        ###### may be best choice for the filter types
    
    ## 4.BILATERAL FILTER
#    bilateral = cv2.bilateralFilter(last_image,15,15,75)
    
    
   # cv2.imshow("SMOOTHED FİLTER",smoothed)
   # cv2.imshow("BLUR FILTER",blur)
    cv2.imshow("MEDIANBLUR FILTER",median)
   # cv2.imshow("BILATERAL FILTER",bilateral)
   # cv2.imshow("Not filtered frame",last_image)
    
    
    if cv2.waitKey(10)  & 0xFF == ord('e'):
        break
    
camera.release()
cv2.destroyAllWindows()
