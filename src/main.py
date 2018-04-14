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
import roiSelector as rs 
import getDepth as gd

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

correct = cr((640, 480), (10,10), 4, 3)
rotate_angle = -38
parent = Path(os.getcwd()).parent
casc = cv2.CascadeClassifier("lbp_s10/cascade.xml")
pat = pt.Pattern()
points = list()


while(True):

	#load images to work with and list of points
	pointsList = list()
	ret, img = cap.read()
	img = cv2.GaussianBlur(img, (3,3),2)
	img_h, img_w, img_channels = img.shape
	detected = np.zeros((img_h, img_w, 1), np.uint8)
	fixed = np.zeros((img_h, img_w, 1), np.uint8)

	rois, binary = rs.getROI(img)


	# get list of points and visualize it in the image "detected"
	pointsList = getPoints(img, casc, rois)

	for p in pointsList:	

		cv2.circle(detected, (int(p.x),int(p.y)), 5, 200, -1)

	correct.update(pointsList)

	# get list of points, which appear more frequently and visualize them in the image "fixed"
	pointsList_new = correct.getFixedData()

	for p in pointsList_new:
		if p.y >=0 and p.y < img_h and p.x >=0 and p.x< img_w:

			cv2.circle(fixed, (int(p.x), int(p.y)), 4, 200, -1)

	cv2.imshow("img", img)
	cv2.imshow("points", detected)
	cv2.imshow("fixed", fixed)
	cv2.imshow("binary", binary)

	k = cv2.waitKey(1)
	if k == s:

		fixed.fill(0)
		
		cl = calibrator()

		for p in pointsList_new:
			if p.y >=0 and p.y < img_h and p.x >=0 and p.x< img_w:

				cv2.circle(fixed, (int(p.x), int(p.y)), 4, 200, -1)

		pat = pt.Pattern()
		cl.calibrate(pointsList_new, fixed)
		cv2.imwrite("calibrated.jpg", fixed)

	if k == c:


		print("got C")
		points3d_n = gd.getDepth(pointsList)
		fixed.fill(0)

		for p in pointsList_new:
			if p.y >=0 and p.y < img_h and p.x >=0 and p.x< img_w:

				cv2.circle(fixed, (int(p.x), int(p.y)), 4, 200, -1)


		gd.writeVertices("model.obj", points3d_n)
		cv2.imwrite("newGrid.jpg", fixed)

	k = cv2.waitKey(1)
	if k == e:
		print("got E")
		
		cv2.imwrite("trainClassifier"+str(taken)+".jpg", img)
		taken+=1
	
	if k == q:
		break
