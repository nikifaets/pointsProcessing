import cv2
import numpy as np 
import time
from extractor import getPoints
import laserFindPoints as cpt
import findLines as fl
import transformToPoints as tr
import calibration as cal
from PointNode import PointNode
from CorrectSignal import CorrectSignal as cr
import rotatePoints as rp
import os
from pathlib import Path
import roiSelector as rs 
import getDepth as gd
import canvas

ret = False
cam = 1
pointsList_cal = list()
taken = 20
#load calibrated image if any

files = os.listdir()
for file in files:
	if file == "calibrated.jpg":
		pointsList_cal = cal.calibrateFromImage(file, "pars.txt")


while(not ret):
 	
	cap = cv2.VideoCapture(cam)
	ret,img = cap.read()
	print("initializing camera ", ret)

cap.set(3,480)
cap.set(4,640)
projecting = False


correct = cr((640, 480), (10,10), 4, 3)
rotate_angle = -38
parent = Path(os.getcwd()).parent
casc = cv2.CascadeClassifier("lbp_s10/cascade.xml")
points = list()


while(True):

	#load images to work with and list of points
	pointsList = list()
	ret, img = cap.read()
	img_pure = np.zeros(img.shape, np.uint8)
	img_pure = np.copy(img)
	img = cv2.GaussianBlur(img, (3,3),2)
	img_h, img_w, img_channels = img.shape
	detected = np.zeros((img_h, img_w, 1), np.uint8)
	fixed = np.zeros((img_h, img_w, 1), np.uint8)
	rois, binary = rs.getROI(img)


	# get list of points and visualize it in the image "detected"
	pointsList = getPoints(img, casc, rois)

	#if len(pointsList) > 0: 
	#	print(pointsList[0].x, pointsList[0].y)
	for p in pointsList:	

		cv2.circle(detected, (int(p.x),int(p.y)), 5, 200, -1)

	correct.update(pointsList)

	# get list of points, which appear more frequently and visualize them in the image "fixed"
	pointsList_new = correct.getFixedData()

	for p in pointsList_new:
		if p.y >=0 and p.y < img_h and p.x >=0 and p.x< img_w:

			cv2.circle(fixed, (int(p.x), int(p.y)), 4, 200, -1)

	points3d_new = list()
	if len(pointsList_cal) > 0: 
			points3d_new = gd.getDepth(pointsList_cal, pointsList_new)

	cv2.imshow("img_pure", img_pure)
	cv2.imshow("img", img)
	cv2.imshow("points", detected)
	cv2.imshow("fixed", fixed)
	cv2.imshow("binary", binary)

	k = cv2.waitKey(1)
	if k == ord('s'):

		pointsList_cal = cal.calibrate(pointsList_new, "pars.txt")
		cv2.imwrite("calibrated.jpg", fixed)

	if k == ord('c'):

		print("C")
		if len(pointsList_cal) > 0: 
			points3d_new = gd.getDepth(pointsList_cal, pointsList_new)
			gd.writeVertices("model.obj", points3d_new)
			cv2.imwrite("newGrid.jpg", fixed)
		else:

			print("Please calibrate first")

	if k == ord('e'):
		print("got E")
		
		cv2.imwrite("pure" + str(taken)+".jpg", img_pure)
		cv2.imwrite("threshold.jpg", binary)
		cv2.imwrite("classifier.jpg", img)
		cv2.imwrite("point"+str(taken)+".jpg", fixed)
		taken+=1
	
	if k == ord('q'):
		break
