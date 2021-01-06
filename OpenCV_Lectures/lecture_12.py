# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera =cv2.VideoCapture(0)

low  = np.array([20, 0, 0])
high = np.array([37, 255, 255])     

# low  = np.array([20, 0, 0])
# high = np.array([37, 255, 255])     # filtering for yellow color

# low  = np.array([0, 0, 0])
# high = np.array([10, 255, 255])     # filtering for red color

# low  = np.array([85, 0, 0])
# high = np.array([100, 255, 255])     # filtering for light blue color

# low  = np.array([45, 0, 0])
# high = np.array([75, 255, 255])     # filtering for green color


while True:
    
    ret,frame = camera.read()
    
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    mask =cv2.inRange(hsv,low,high)
    
    last_image = cv2.bitwise_and(frame,frame,mask = mask)
    
    cv2.imshow("hsv goruntusu",hsv)
    cv2.imshow("bgr goruntu",frame)
    cv2.imshow("filtrelenmis goruntu",mask)
    cv2.imshow("istenen_goruntu",last_image)
    
    
    if cv2.waitKey(25)  & 0xFF == ord('e'):
        break
    
camera.release()
cv2.destroyAllWindows()
    

