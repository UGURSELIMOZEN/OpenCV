# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera = cv2.VideoCapture(0)

low =  np.array([26,110,110,])           # THE ARRANGED THRESHOLDS
high = np.array([31,255,255])     # WE DEFINE THE COLOR WE WANT

while True:
    
    ret,square = camera.read()
    
    hsv = cv2.cvtColor(square,cv2.COLOR_BGR2HSV)
    
    mask =cv2.inRange(hsv,low,high)  # We have filtered the square to the proper color that transformed based on hsv range. #                
   
    last_image =cv2.bitwise_and(square,square,mask =mask) # to get the last image we apply to and rule to square and mask objects. #
    
    kernel = np.ones((5,5),np.uint8)
    
    erosion = cv2.erode(mask,kernel,iterations = 1)
    
    diolation = cv2.dilate(mask,kernel,iterations= 1)
    
    opening =   cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)   
    
    closining = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    
    #cv2.imshow("erosion",erosion)   # purpose of making image more black
    #cv2.imshow("diolation",diolation)   # purpose of making image more white
    #cv2.imshow("mask",mask)
    #cv2.imshow("filtered_square",last_image)
    
    cv2.imshow("opening",opening)       # to make more clear all words in the image
    cv2.imshow("closining",closining)   # to destroy all words in the image
    
    if cv2.waitKey(25) & 0xFF == ord('e'):
        break
    
    
camera.release()
cv2.destroyAllWindows()    
