# -*- coding: utf-8 -*-
import cv2
import numpy as np

image = cv2.imread("images.jpg")
grayimage = cv2.imread("images.jpg",0)
cv2.imshow("changes",image)
cv2.imshow("grayimage",grayimage)

print(image )
print("type of image = " + str(type(image )))
print("size of image = " + str(image .size) + " piksel")
print("data type of image   = " + str(image .dtype))
print("shape of image   = " + str(image .shape))

print("\nsize of gray image = " + str(grayimage.size) + "pixel")
print("shape of gray image = " + str(grayimage.shape))
print("type of  gray image = " +str(type(grayimage)))
print("data type of gray image  = " + str(grayimage.dtype))

for i in range (0,3):                   # 3D array 
    print(image .item(150,150,i)) # 0 for blue value , 1 for green value ,
                                # 2 for red value in that pixel . 

print(image [150,150])   # second way to learn bgr values

print(grayimage.item(150,150))   # we see the gray value in the pixel here.
                                    # 2D array.
cv2.waitKey(0)
cv2.destroyAllWindows()             # BGR -> BLUE GREEN RED  logic
