# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 09:13:53 2020

@author: Jatin
"""
import cv2
import numpy as np


def mapp(h):
    h = h.reshape((4,2))
    hnew = np.zeros((4,2),dtype = np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h,axis = 1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew


image=cv2.imread("images/Aadhar3.jpeg")
image=cv2.resize(image,(400,400))
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
frame=gray_image.copy()
blurred = cv2.GaussianBlur(frame, (7, 7), 0)
edged=cv2.Canny(blurred,20,255)



cnts,_ = cv2.findContours(edged, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)
cv2.drawContours(image,cnts, -1, (0, 255, 0), 5)
for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    if len(approx) == 4:
        target=approx
        (x, y, w, h) = cv2.boundingRect(approx)
        break
    
doc=image[y:y+h,x:x+w]


cv2.imshow("doc",doc)
cv2.imshow("edged", edged)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
