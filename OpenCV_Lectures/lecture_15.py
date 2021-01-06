# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    
    ret,square = camera.read()
    
    
    gray_square = cv2.cvtColor(square,cv2.COLOR_BGR2GRAY)
    
    object1 = cv2.imread("kalem.jpg",0)
    
    width,height = object1.shape
    
    res = cv2.matchTemplate(gray_square,object1,cv2.TM_CCOEFF_NORMED)
    
    threshold = 0.8
    
    loc = np.where(res>threshold)
    
    for n in zip(*loc[::-1]):
        cv2.rectangle(square,n,(n[0]+height,n[1]+width),(255,0,0),1)
        cv2.putText(square,"kitap",(n[0]+10,n[1]+10),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
    
    cv2.imshow("square",square)
    
    
    if cv2.waitKey(25)  & 0xFF == ord('e'):
        break
    
camera.release()
cv2.destroyAllWindows()
