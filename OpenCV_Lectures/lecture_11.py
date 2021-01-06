# -*- coding: utf-8 -*-

import cv2
import numpy as np


def main():
    
    camera = cv2.VideoCapture(0)
    
    fourcc =cv2.VideoWriter_fourcc(*'XVID')     # defining video format
    
    record = cv2.VideoWriter("my_video.avi",fourcc,25,(640,480))   # record details
    
    while True:
        dogru,video= camera.read()
        
        #reverse_frame =cv2.flip(video,0)  # to take reverse frame in video 
    
        if dogru == True:
            record.write(video)
        
        cv2.imshow("camera",video)
    
        if cv2.waitKey(25) & 0xFF == ord('e'):
            break
        
    camera.release()
    cv2.destroyAllWindows()
    
if __name__ =="__main__":
    main()
