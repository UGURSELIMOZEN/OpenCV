# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    ret,square = camera.read()
    
    laplacian = cv2.Laplacian(square,cv2.CV_64F)
    
    canny = cv2.Canny(square,50,100)
    
    cv2.imshow("laplacian_filter",laplacian)
    
    cv2.imshow("canny_filter",canny)
    
    cv2.imshow("original",square)
    
    if cv2.waitKey(25) & 0xFF == ord('e'):
        break
    
camera.release()
cv2.destroyAllWindows() 
