# -*- coding: utf-8 -*-

import cv2
import numpy as np


def main():
    
    kamera = cv2.VideoCapture(0)
    
    fourcc =cv2.VideoWriter_fourcc(*'XVID')     # video formatı belirleme
    
    kayit = cv2.VideoWriter("my_video.avi",fourcc,25,(640,480))   # kayıdın detayları
    
    while True:
        dogru,video= kamera.read()
        
        #ters_goruntu =cv2.flip(video,0)  videoda ters goruntu için 
    
        if dogru == True:
            kayit.write(video)
        
        cv2.imshow("kamera",video)
    
        if cv2.waitKey(25) & 0xFF == ord('e'):
            break
        
    kamera.release()
    cv2.destroyAllWindows()
    
if __name__ =="__main__":
    main()