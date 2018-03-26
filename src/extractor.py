import cv2
import numpy as np 

def thresh(img):
	
	blur = cv2.GaussianBlur(img,(3,3),1)
	

	ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



	return th3

def threshNormal(img, val):

	return cv2.threshold(img, val, 255, cv2.THRESH_BINARY)[1]


