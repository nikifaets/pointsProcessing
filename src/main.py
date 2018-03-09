import cv2
import numpy as np 
import time
import laserFindPoints as cpt
import findLines as fl
import transformToPoints as tr
from calibration import calibrator
import pattern as pt

cam = 0
cap = cv2.VideoCapture(cam)
cap.set(3,240)
cap.set(4,320)

point_casc = cv2.CascadeClassifier("haar_new_s15/cascade.xml")
projecting = False
haar = False
s = 115
a = 97
q = 113
c = 99
b = 98
d = 100

pat = pt.Pattern()


ret,img = cv2.VideoCapture(cam)
while(not ret):

	cam+=1
	ret,img = cv2.VideoCapture(cam)

while(True):

	ret, img = cap.read()
	cv2.imshow("img", img)
	if projecting:
		
		img = cv2.GaussianBlur(img, (5,5), 3)
		img = cv2.morphologyEx(img, cv2.MORPH_OPEN, (4,4))
		thresh, grayscale = cpt.threshImage(img)
		points, pointsList, stats = fl.createGrid(thresh)


		cv2.imshow("img", img)
		cv2.imshow("thresh", thresh)
		cv2.imshow("grayscale", grayscale)

		cv2.imshow("points", points)


		k = cv2.waitKey(1)
		if k == s:

			points, pointsList = fl.createGrid(thresh)
			cl = calibrator()
			cl.calibrate(pointsList)
			pat = pt.Pattern()
			cv2.imwrite("calibrated.jpg", points)

		if k == c:

			points, pointsList = fl.createGrid(thresh)
			pat.getDepth(pointsList)
			cv2.imwrite("newGrid.jpg", points)

		if haar:

			points = casc.detectMultiScale(img)

			for(x, y, h, w) in points:
        	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

			cv2.imshow("img", img)

	k = cv2.waitKey(1)
	if k == a:
		print("got A")
		projecting = not projecting

	if k == d:
		haar = not haar

	if k == q:
		break

