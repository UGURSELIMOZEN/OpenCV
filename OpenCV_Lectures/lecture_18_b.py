# -*- coding: utf-8 -*-

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    
    ret,kare = kamera.read()
    gri_resim = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    gri_resim = np.float32(gri_resim)
    
    
    corners = cv2.goodFeaturesToTrack(gri_resim,30,0.1,15)
    corners = np.int0(corners)
    print(type(corners))
    for corner in corners:
        x,y =corner.ravel()
        cv2.circle(kare,(x,y),3,(255,0,0),-1)
        cv2.putText(frame,str(x,y),(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,255,0),2,cv2.LINE_AA)
        
    cv2.imshow("corner_detection",kare)
    
    if cv2.waitKey(25) & 0xFF ==ord('e'):
        break
      
    
kamera.release()
cv2.destroyAllWindows()  
