import cv2
import numpy as np

def selectROI(img):
	
	gray = rgb2gray(img)
	gray = np.subtract(gray, 200)
	#ret,gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

	return gray

cap = cv2.VideoCapture(1)
cap.set(3,480)
cap.set(4,640)

def rgb2gray(img):

	h,w,channels = img.shape
	b,g,r = cv2.split(img)

	return g

while True:

	ret,img = cap.read()
	img = selectROI(img)

	cv2.imshow("img", img)
	k = cv2.waitKey(1)

	if k == ord('q'):
		break




