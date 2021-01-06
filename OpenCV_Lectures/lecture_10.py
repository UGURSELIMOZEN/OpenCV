# -*- coding: utf-8 -*-

import cv2
import numpy as np

camera = cv2.VideoCapture(0)

# camera.set(3,200)    #  to set width in the video
# camera.set(4,700)    # to set heigth in the video

def arranging (frame,percent =75):
    width  = int(frame.shape[1]*percent/100)
    height = int(frame.shape[0]*percent/100)
    shape=(width,height)
    return cv2.resize(frame,shape,interpolation =cv2.INTER_AREA)



def main():
    while True:
        
        ret,frame = camera.read()
        
        gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # to  make the image as gray
        
        image2= arranging (frame,60)
        
        cv2.imshow("gray_img",gray_img )
        cv2.imshow("arranged image",image2)
        cv2.imshow("usb_cam",frame)
        
        if cv2.waitKey(25) & 0xFF == ord('e'):
            break
        
    camera.release()
    cv2.destroyAllWindows()     

if __name__ == "__main__":
    main()
