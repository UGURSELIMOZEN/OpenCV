# -*- coding: utf-8 -*-

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    ret,kare = kamera.read()
    
    laplacian = cv2.Laplacian(kare,cv2.CV_64F)
    
    canny = cv2.Canny(kare,50,100)
    
    cv2.imshow("laplacian_filter",laplacian)
    
    cv2.imshow("canny_filter",canny)
    
    cv2.imshow("orjinal",kare)
    
    if cv2.waitKey(25) & 0xFF == ord('e'):
        break
    
kamera.release()
cv2.destroyAllWindows() 