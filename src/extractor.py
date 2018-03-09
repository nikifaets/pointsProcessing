import cv2
import numpy as np 

def thresh(img):
	
	blur = cv2.GaussianBlur(img,(7,7),1)
	#blur = cv2.medianBlur(img, 3)
	#ret3,th3 = cv2.threshold(img,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#th1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            #cv2.THRESH_BINARY_INV,7,7)
	#th1 = cv2.medianBlur(th1,2)
	#th1 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            #cv2.THRESH_BINARY_INV,3,3)

	ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


	return th3

def threshNormal(img, val):

	return cv2.threshold(img, val, 255, cv2.THRESH_BINARY)[1]

