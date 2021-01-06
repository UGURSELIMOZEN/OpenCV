# -*- coding: utf-8 -*-

import cv2 
import numpy as np

resim = cv2.imread("download.jpg")

uzatilan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REPLICATE)

aynalanan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_REFLECT)

tekrarlanan_resim = cv2.copyMakeBorder(resim,100,100,100,100,cv2.BORDER_WRAP)

sarilan_resim = cv2.copyMakeBorder(resim,50,50,50,50,cv2.BORDER_CONSTANT,value =[255,0,0])

# istenilen bölgeyi çerçeveye alma
cv2.rectangle(resim,(30,200),(160,30),[0,255,0],3)
                 #   x1,y1    x2,y2     renk    kalınlık

cv2.imshow("orjinal resim",resim)
cv2.imshow("uzatilan resim",uzatilan_resim)
cv2.imshow("aynalanan resim",aynalanan_resim)
cv2.imshow("tekrarlanan resim",tekrarlanan_resim)
cv2.imshow("sarilan resim",sarilan_resim)

cv2.waitKey(0)
cv2.destroyAllWindows()