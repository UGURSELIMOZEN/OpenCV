# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera =cv2.VideoCapture(0)

low  = np.array([20, 0, 0])
high = np.array([37, 255, 255])     

# dusuk  = np.array([20, 0, 0])
# yuksek = np.array([37, 255, 255])     # sarı filtreleme için

# dusuk  = np.array([0, 0, 0])
# yuksek = np.array([10, 255, 255])     # kırmızı filtreleme için

# dusuk  = np.array([85, 0, 0])
# yuksek = np.array([100, 255, 255])     # Açık mavi filtreleme için

# dusuk  = np.array([45, 0, 0])
# yuksek = np.array([75, 255, 255])     # yeşil filtreleme için


while True:
    
    dogru,goruntu = camera.read()
    
    hsv =cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    
    mask =cv2.inRange(hsv,dusuk,yuksek)
    
    son_resim = cv2.bitwise_and(goruntu,goruntu,mask = mask)
    
    cv2.imshow("hsv goruntusu",hsv)
    cv2.imshow("bgr goruntu",goruntu)
    cv2.imshow("filtrelenmis goruntu",mask)
    cv2.imshow("istenen_goruntu",son_resim)
    
    
    if cv2.waitKey(25)  & 0xFF == ord('e'):
        break
    
camera.release()
cv2.destroyAllWindows()
    

