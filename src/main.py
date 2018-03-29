import cv2
import numpy as np 
import time
from extractor import getPoints
import laserFindPoints as cpt
import findLines as fl
import transformToPoints as tr
from calibration import calibrator
import pattern as pt
from PointNode import PointNode
from CorrectSignal import CorrectSignal as cr
import rotatePoints as rp
import os
from pathlib import Path

ret = False
cam = 0
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

parent = Path(os.getcwd()).parent
casc = cv2.CascadeClassifier(str(parent)+"/hog_s10/cascade.xml")
pat = pt.Pattern()
points = list()


while(True):

	#load images to work with and list of points
	pointsList = list()
	ret, img = cap.read()
	img_h, img_w, img_channels = img.shape
	detected = np.zeros((img_h, img_w, 1), np.uint8)
	fixed = np.zeros((img_h, img_w, 1), np.uint8)
	lines_detected = np.zeros((img_h, img_w, 1), np.uint8)

	# get list of points and visualize it in the image "detected"
	pointsList = getPoints(img, casc)

	for p in pointsList:	

		cv2.circle(detected, (int(p.y),int(p.x)), 5, 200, -1)

	correct.update(pointsList)

	# get list of points, which appear more frequently and visualize them in the image "fixed"
	pointsList_new = correct.getFixedData()
	rp.rotatePoints(pointsList_new, PointNode(img_w/2, img_h/2), 30)

	for p in pointsList_new:
		if p.y >=0 and p.y < img_h and p.x >=0 and p.x< img_w:

			cv2.circle(fixed, (int(p.x), int(p.y)), 4, 200, -1)


	#create lines from the points with similar y coordinate and visualize them in image "lines"

	lines = fl.collectLines(pointsList_new)

	for line in lines:
		line.draw(lines_detected)

	cv2.imshow("lines", lines_detected)
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
	
	if k == q:
		break
