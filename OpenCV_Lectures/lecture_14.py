# -*- coding: utf-8 -*-

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

dusuk =  np.array([26,110,110,])           # BUNLAR AYARLADIGIMIZ TRESHOLDLAR
yuksek = np.array([31,255,255])     # HANGI RENGI ALGILAYACAK ONU BELIRLIYORUZ

while True:
    
    dogru,goruntu = kamera.read()
    
    hsv = cv2.cvtColor(goruntu,cv2.COLOR_BGR2HSV)
    
    mask =cv2.inRange(hsv,dusuk,yuksek)  # BURADA ISE HSV YE DONUSEN GORUNTUYU  
                                         # UYGUN RENGE GORE FILTRELEMIS OLDUK                  
   
    son_resim =cv2.bitwise_and(goruntu,goruntu,mask =mask) # NIHAI GORUNTUYU 
                # ALMAK ICIN GORUNTU VE MASKA VE ISLEMI UYGULADIK 
    
    kernel = np.ones((5,5),np.uint8)
    
    erosion = cv2.erode(mask,kernel,iterations = 1)
    
    diolation = cv2.dilate(mask,kernel,iterations= 1)
    
    opening =   cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)   
    
    closining = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
    
    #cv2.imshow("erosion",erosion)   # RESIMDE SIYAHLASTIRMA BIRAZ DAGITMA AMACLI
    #cv2.imshow("diolation",diolation)   # RESIMDE BUTUNSELLIK (BEYAZLASTIRMA) AMACLI
    #cv2.imshow("mask",mask)
    #cv2.imshow("filtreli goruntu",son_resim)
    
    cv2.imshow("opening",opening)       # RESIMDEKI YAZILARI BELIRGINLESTIRME AMACLI
    cv2.imshow("closining",closining)   #RESIMDEKI YAZILARI YOK ETME AMACLI
    
    if cv2.waitKey(25) & 0xFF == ord('e'):
        break
    
    
kamera.release()
cv2.destroyAllWindows()    