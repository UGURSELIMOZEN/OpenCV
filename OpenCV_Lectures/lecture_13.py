# -*- coding: utf-8 -*-

import cv2
import numpy as np

kamera =cv2.VideoCapture(0)

dusuk  = np.array([20,100,150])
yuksek = np.array([37,255,255])     

# dusuk  = np.array([20, 0, 0])
# yuksek = np.array([37, 255, 255])     # sarı filtreleme için

# dusuk  = np.array([0, 0, 0])
# yuksek = np.array([10, 255, 255])     # kırmızı filtreleme için

# dusuk  = np.array([85, 0, 0])
# yuksek = np.array([100, 255, 255])     # Açık mavi filtreleme için

# dusuk  = np.array([45, 0, 0])
# yuksek = np.array([75, 255, 255])     # yeşil filtreleme için
while True:
    
    dogru,goruntu = kamera.read()
    
    hsv =cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    
    mask =cv2.inRange(hsv,dusuk,yuksek)
    
    son_resim = cv2.bitwise_and(goruntu,goruntu,mask = mask)
    
    ## 1.SMOOTHED FILTER
#    kernel = np.ones((15,15),dtype= np.float32) / 255
#    smoothed =cv2.filter2D(son_resim,-1,kernel)
    
    ## 2.BLUR FILTER
#    blur =cv2.GaussianBlur(son_resim,(15,15),0)
    
    ## 3.MEDIAN FILTER
    median =cv2.medianBlur(son_resim,15)        ###### EN IYI FILTRE BU DIYEBILIRIZ
    
    ## 4.BILATERAL FILTER
#    bilateral = cv2.bilateralFilter(son_resim,15,15,75)
    
    
   # cv2.imshow("SMOOTHED FİLTER",smoothed)
   # cv2.imshow("BLUR FILTER",blur)
    cv2.imshow("MEDIANBLUR FILTER",median)
   # cv2.imshow("BILATERAL FILTER",bilateral)
   # cv2.imshow("Filtresiz goruntu",son_resim)
    
    
    if cv2.waitKey(10)  & 0xFF == ord('e'):
        break
    
kamera.release()
cv2.destroyAllWindows()