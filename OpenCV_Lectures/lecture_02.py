# -*- coding: utf-8 -*-
import cv2
import numpy as np

resim = cv2.imread("images.jpg")
griresim = cv2.imread("images.jpg",0)
cv2.imshow("changes",resim)
cv2.imshow("griresim",griresim)

print(resim)
print("resmin tipi = " + str(type(resim)))
print("resimin büyüklüğü = " + str(resim.size) + " piksel")
print("resimin data tipi   = " + str(resim.dtype))
print("resimin boyutu   = " + str(resim.shape))

print("\ngri resmin büyüklüğü = " + str(griresim.size) + "piksel")
print("gri resmin boyutu = " + str(griresim.shape))
print("gri resmin tipi = " +str(type(griresim)))
print("gri resimin data tipi   = " + str(griresim.dtype))

for i in range (0,3):                   #BU 3 BOYUTLU ARRAYDIR.
    print(resim.item(150,150,i)) # 0 olursa mavi değeri ,, 1 olursa yeşil değeri,,
                                # 2 olursa  o pikseldeki kırmızı değeri görünür. 

print(resim[150,150])   # bgr değerlerini öğrenmek için 2.yöntem

print(griresim.item(150,150))   # burada ise bu pikseldeki gri değeri görünür.
                                    #BU 2 BOYUTLU ARRAYDIR.
cv2.waitKey(0)
cv2.destroyAllWindows()             # BGR -> BLUE GREEN RED  logic