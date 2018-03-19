import cv2
import numpy as np 
import time
import laserFindPoints as cpt
import findLines as fl
import transformToPoints as tr
from calibration import calibrator
import pattern as pt


while(not ret):

	cap = cv2.VideoCapture(cam)
	ret,img = cap.read()
	print("initializing camera ", ret)

cap.set(3,240)
cap.set(4,320)
projecting = False
s = 115
a = 97
q = 113
c = 99
b = 98

pat = pt.Pattern()
points = list()

while(True):

	ret, img = cap.read()
	detected = np.zeros((480,640,1), np.uint8)
	
	img = cv2.blur(img,(3,3) )

		points = casc.detectMultiScale(img)

		for(x, y, h, w) in points:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
			detected[int(y+h/2)][int(x+w/2)] = 255

		cv2.imshow("img", img)
		cv2.imshow("points", detected)

		k = cv2.waitKey(1)
		if k == s:

			cl = calibrator()
			cl.calibrate(points)
			pat = pt.Pattern()
			cv2.imwrite("calibrated.jpg", points)

		if k == c:

			print("got C")
			pat.getDepth(pointsList)
			cv2.imwrite("newGrid.jpg", points)

	k = cv2.waitKey(1)
	if k == a:
		print("got A")
		projecting = not projecting

	if k == q:
		break
