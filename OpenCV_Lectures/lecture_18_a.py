# -*- coding: utf-8 -*-

import cv2
import numpy as np

def main():
    
    image = cv2.imread("figures.jpg")
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    gray_image = np.float32(gray_image)
    
    
    corners = cv2.goodFeaturesToTrack(gray_image,30,0.1,65)
    corners = np.int0(corners)
    
    for corner in corners:
        x,y =corner.ravel()
        cv2.circle(image,(x,y),3,(255,0,0),-1)
        
        
    cv2.imshow("corner_detection",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()
