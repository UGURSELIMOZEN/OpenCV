# -*- coding: utf-8 -*-

import cv2
import numpy as np

kamera = cv2.VideoCapture(0)

# kamera.set(3,200)    #  bu kısmı genişliği set eder
# kamera.set(4,700)    # bu kısmı yukseklıgi set eder

def ayarlama (kare,yuzde =75):
    width  = int(kare.shape[1]*yuzde/100)
    height = int(kare.shape[0]*yuzde/100)
    shape=(width,height)
    return cv2.resize(kare,shape,interpolation =cv2.INTER_AREA)



def main():
    while True:
        
        ret,kare = kamera.read()
        
        gri_img = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY) # resmi grileştirmek için
        
        resim2= ayarlama (kare,60)
        
        cv2.imshow("gray_img",gri_img)
        cv2.imshow("ayarlanan resim",resim2)
        cv2.imshow("usb_cam",kare)
        
        if cv2.waitKey(25) & 0xFF == ord('e'):
            break
        
    kamera.release()
    cv2.destroyAllWindows()     

if __name__ == "__main__":
    main()