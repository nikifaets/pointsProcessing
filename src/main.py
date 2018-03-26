import cv2
import numpy as np 
import time
import laserFindPoints as cpt
import findLines as fl
import transformToPoints as tr
from calibration import calibrator
import pattern as pt
from PointNode import PointNode
from CorrectSignal import CorrectSignal as cr

ret = False
cam = 1
while(not ret):

	cap = cv2.VideoCapture(cam)
	ret,img = cap.read()
	print("initializing camera ", ret)

cap.set(3,480)
cap.set(4,640)
projecting = False

taken = 20
s = 115
a = 97
q = 113
c = 99
b = 98
e = 101

correct = cr((640, 480), (20,20), 4, 3)
casc = cv2.CascadeClassifier("hog_s10/cascade.xml")
pat = pt.Pattern()
points = list()


while(True):

	pointsList = list()
	ret, img = cap.read()
	detected = np.zeros((480,640,1), np.uint8)
	fixed = np.zeros((480,640,1), np.uint8)
	
	#img = cv2.blur(img,(3,3) )

	points = casc.detectMultiScale(img)

	for(x, y, h, w) in points:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), -1)
		#print(w,h)
		p_x = x+w/2
		p_y = y+h/2
		pointsList.append(PointNode(p_x, p_y))
		detected[int(p_y)][int(p_x)] = 255

	correct.update(pointsList)
	pointsList_new = correct.getFixedData()

	for p in pointsList_new:
		fixed[int(p.y)][int(p.x)] = 255


	cv2.imshow("img", img)
	cv2.imshow("points", detected)
	cv2.imshow("fixed", fixed)

	k = cv2.waitKey(1)
	if k == s:

		cl = calibrator()
		cl.calibrate(pointsList)
		pat = pt.Pattern()
		cv2.imwrite("calibrated.jpg", detected)

	if k == c:

		print("got C")
		pat.getDepth(pointsList)
		cv2.imwrite("newGrid.jpg", detected)

	k = cv2.waitKey(1)
	if k == e:
		print("got E")
		
		cv2.imwrite("trainClassifier"+str(taken)+".jpg", img)
		taken+=1
		#cap = cv2.VideoCapture(cam)
	if k == q:
		break
