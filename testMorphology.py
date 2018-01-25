import cv2
import numpy as np  
import extractor as ext  
import findLines as fl 
import laserFindPoints as lfp 


imgpath = "laser/laser4.jpg"
imgorg = cv2.imread(imgpath)

img = cv2.resize(imgorg,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC)
img, grayscale = lfp.threshImage(img)
cv2.imshow("img", img)
cv2.imshow("gray", grayscale)
cv2.imshow("original", imgorg)
cv2.waitKey()