#!/usr/bin/python
# new code
import math
import numpy as np
import cv2
import serial
from my_serial import goalfound


#dictionary of all contours
contours = {}
#array of edges of polygon
approx = []
#scale of the text
scale = 2
#camera
cap = cv2.VideoCapture(0)



# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

#calculate angle
def angle(pt1,pt2,pt0):
    dx1 = pt1[0][0] - pt0[0][0]
    dy1 = pt1[0][1] - pt0[0][1]
    dx2 = pt2[0][0] - pt0[0][0]
    dy2 = pt2[0][1] - pt0[0][1]
    return float((dx1*dx2 + dy1*dy2))/math.sqrt(float((dx1*dx1 + dy1*dy1))*(dx2*dx2 + dy2*dy2) + 1e-10)

while True:
    #Capture frame-by-frame
    ret, frame = cap.read()
    if ret==True:
        #grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #Canny
        canny = cv2.Canny(frame,50,100)

        #contours
        canny2, contours, hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        for i in range(0,len(contours)):
            # Approximate the contour with accuracy proportional to the contour perimeter
            approx = cv2.approxPolyDP(contours[i],cv2.arcLength(contours[i],True)*0.025,True)
            vtc = len(approx)
            # Skip small or non-convex objects
            if(not(abs(cv2.contourArea(contours[i]))<200 or not(cv2.isContourConvex(approx)) )):            
                x,y,w,h = cv2.boundingRect(contours[i])
                # polygons
                cv2.putText(frame,str(len(approx)),(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,255,0),2,cv2.LINE_AA)
                if(vtc == 3):
                    cv2.putText(frame,'triangle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,255,255),2,cv2.LINE_AA)
                                       
                if(vtc>=4 and vtc<=6):
                
                    # nb vertices of a polygonal curve
                    
                    # Get cos of all corners
                    cos = []
                    for j in range(2,vtc+1):
                        cos.append(angle(approx[j%vtc],approx[j-2],approx[j-1]))
                    # Sort ascending cos
                    cos.sort()
                    # Get lowest and highest
                    mincos = cos[0]
                    maxcos = cos[-1]

                    if(vtc==4):
                        cv2.putText(frame,'rectangle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(255,0,0),2,cv2.LINE_AA)
                        
                    if(vtc==6):
                        cv2.putText(frame,'hexagon',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,255,0),2,cv2.LINE_AA)                             
                        
                   
                else:
                  
                        #detect and label circle
                    area = cv2.contourArea(contours[i])
                    radius = w/2
                    if(abs(1 - (float(w)/h))<=2 and abs(1-(area/(math.pi*radius*radius)))<=0.2):
                        cv2.putText(frame,'circle',(x,y),cv2.FONT_HERSHEY_SIMPLEX,scale,(0,0,255),2,cv2.LINE_AA)                        
                        

        #Display the resulting frame
        out.write(frame)
        cv2.imshow('frame',frame)
        cv2.imshow('canny',canny)
        if cv2.waitKey(25) & 0xFF == ord('e'):   # when pressing the 'e' key , video will be shut down.
            break

#When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
