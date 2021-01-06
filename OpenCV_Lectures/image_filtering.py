# -*- coding: utf-8 -*-
                        ##### KIRMIZI VE SARI FİLTRELEME ###
import numpy as np
import cv2


image = cv2.imread("muslera.jpg")

boundaries = [
    ([160, 0, 0], [180, 255, 255]),
    ([20, 0, 0], [30, 255, 255])]

converted = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype = "uint8")
    upper = np.array(upper, dtype = "uint8")
     
    # find the colors within the specified boundaries and apply
    # the mask
    mask = cv2.inRange(converted, lower, upper)
    output = cv2.bitwise_and(image, image, mask = mask)
    
    
    cv2.imshow("images", output)
    
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

