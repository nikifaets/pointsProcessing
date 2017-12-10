import cv2
import numpy as np 
import laserFindPoints as cpt
import findLines as fl

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
while(True):

	ret, img = cap.read()
	thresh, grayscale = cpt.threshImage(img)
	points, connectedPoints = fl.createGrid(thresh)

	cv2.imshow("thresh", thresh)
	cv2.imshow("grayscale", grayscale)

	
	cv2.imshow("points", points)
	cv2.imshow("connected", connectedPoints)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break