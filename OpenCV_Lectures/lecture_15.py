# -*- coding: utf-8 -*-

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

while True:
    
    ret,goruntu = kamera.read()
    
    
    gri_goruntu = cv2.cvtColor(goruntu,cv2.COLOR_BGR2GRAY)
    
    nesne = cv2.imread("kalem.jpg",0)
    
    width,height = nesne.shape
    
    res = cv2.matchTemplate(gri_goruntu,nesne,cv2.TM_CCOEFF_NORMED)
    
    esik_degeri = 0.8
    
    loc = np.where(res>esik_degeri)
    
    for n in zip(*loc[::-1]):
        cv2.rectangle(goruntu,n,(n[0]+height,n[1]+width),(255,0,0),1)
        cv2.putText(goruntu,"kitap",(n[0]+10,n[1]+10),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
    
    cv2.imshow("goruntu",goruntu)
    
    
    if cv2.waitKey(25)  & 0xFF == ord('e'):
        break
    
kamera.release()
cv2.destroyAllWindows()