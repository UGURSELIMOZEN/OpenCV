# -*- coding: utf-8 -*-

import cv2
import numpy as np

def main():
    
    resim = cv2.imread("figures.jpg")
    gri_resim = cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
    gri_resim = np.float32(gri_resim)
    
    
    corners = cv2.goodFeaturesToTrack(gri_resim,30,0.1,65)
    corners = np.int0(corners)
    
    for corner in corners:
        x,y =corner.ravel()
        cv2.circle(resim,(x,y),3,(255,0,0),-1)
        
        
    cv2.imshow("corner_detection",resim)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    main()