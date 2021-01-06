# -*- coding: utf-8 -*-
                                            #### ARKA PLANI FILTRELEME #####
import cv2
import numpy as np

def main():
    
    resim =cv2.imread("mecnun.jpg")
    
    cv2.imshow("MECNUN",resim)
    
    mask =np.zeros(resim.shape[:2],np.uint8)
    
    background_model =np.zeros((1,65),dtype = np.float64)
    forwardground_model =np.zeros((1,65),dtype = np.float64)
    
    rectangle = (200,0,420,400)
    
    cv2.grabCut(resim,mask,rectangle,background_model,forwardground_model,5,cv2.GC_INIT_WITH_RECT)
    
    mask2= np.where((mask == 0) | (mask == 2),0,1).astype(np.uint8)
    
    resim =resim * mask2[:,:,np.newaxis]
    
    cv2.imshow("NEW_MECNUN",resim)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

if __name__ == "__main__":
    main()