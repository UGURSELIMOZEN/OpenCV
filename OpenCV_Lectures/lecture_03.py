# -*- coding: utf-8 -*-

import cv2
import numpy as np

resim = cv2.imread("download.jpg")

for i in range (200):               # image[y,x] şeklindedir.
    resim[100,i]=[255,255,255]   # o piksellerdeki rengi değiştirmek için

bölge = resim[50:200,50:160]    # resimden belirli bir kısım aldık
# y1 den y2 ye kadar ve x1 den x2 ye kadar al şeklinde

resim[0:150,0:110] = bölge   # aldığımız parçayı tekrar ana resme ekleme

resim [50:100,50:100,0]=255        #belirlediğimiz pikselleri maviye boyadık 
resim [110:140,110:140,1]=255       #belirlediğimiz pikselleri yeşile boyadık
resim [150:170,150:170,2]=255       #belirlediğimiz pikselleri kırmızıya boyadık

cv2.imshow("show",resim)
cv2.imshow("parca",bölge)
cv2.waitKey(0)
cv2.destroyAllWindows()