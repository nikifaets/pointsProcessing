import cv2
import numpy as np 
from pathlib import Path
import os
import sys

path = Path(os.getcwd())
path = str(path.parent)
casc = cv2.CascadeClassifier(path+"/hog_s10/cascade.xml")
sys.path.append(path)

import rotatePoints as rp
from PointNode import PointNode
from findLines import collectLines

points = list()

def test_camera():

	cap = cv2.VideoCapture(0)

	while(True):

		

		ret, img = cap.read()
		detected = np.zeros((480,640,1), np.uint8)
		
		img = cv2.blur(img,(3,3) )

		if not tracking:
			points = casc.detectMultiScale(img)

			for(x, y, h, w) in points:
				cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
				detected[int(y+h/2)][int(x+w/2)] = 255


		cv2.imshow("points", detected)
		cv2.imshow("img", img)
		k = cv2.waitKey(1)

		if k == ord('q'):
			break

def test_pic():

	print(os.getcwd())
	img =  cv2.imread(os.getcwd()+"/sample61.jpg",0)
	detected = np.zeros((img.shape[0], img.shape[1],1))
	rotated = np.zeros((img.shape[0], img.shape[1],1))

	if img is not None:

		points = casc.detectMultiScale(img)
		pointsList = list()

		for(x, y, h, w) in points:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
			pn = PointNode(x+w/2, y+h/2)
			pointsList.append(pn)

			detected[int(pn.y)][int(pn.x)] = 255

		rp.rotatePoints(pointsList, PointNode(img.shape[1]/2, img.shape[0]/2), -41)
		pointsList.sort(key = lambda point:point.y, reverse=False)
		lines = collectLines(pointsList)

		for p in pointsList:

			print(p.y)
			cv2.circle(rotated, (int(p.x), int(p.y)), 4, 200, -1)

		for line in lines:
			line.draw(rotated)



		cv2.imshow("points", detected)
		cv2.imshow("img", img)
		cv2.imshow("rotated", rotated)
		cv2.waitKey()


test_pic()



