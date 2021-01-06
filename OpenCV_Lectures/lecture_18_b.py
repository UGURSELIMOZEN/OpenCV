# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera = cv2.VideoCapture(0)

while True:
    
    ret,square = camera.read()
    gray_image = cv2.cvtColor(square,cv2.COLOR_BGR2GRAY)
    gray_image = np.float32(gray_image)
    
    
    corners = cv2.goodFeaturesToTrack(gray_image,30,0.1,15)
    corners = np.int0(corners)
    print(type(corners))
    for corner in corners:
        x,y =corner.ravel()
        cv2.circle(square,(x,y),3,(255,0,0),-1)
        cv2.putText(frame,str(x,y),(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,255,0),2,cv2.LINE_AA)
        
    cv2.imshow("corner_detection",kare)
    
    if cv2.waitKey(25) & 0xFF ==ord('e'):
        break
      
    
camera.release()
cv2.destroyAllWindows()  
