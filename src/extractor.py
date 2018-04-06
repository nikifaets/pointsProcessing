import cv2
import numpy as np 
from PointNode import PointNode

def getPoints(img, classifier, rois):


	points = list()

	for roi in rois:

		rx,ry = roi[1]
		points_roi = classifier.detectMultiScale(roi[0])
		for p in points_roi:
			p[0] +=rx
			p[1] +=ry

		points.extend(points_roi)



	pointsList = list()
	for(x, y, h, w) in points:

		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3)
		p_x = x+w/2
		p_y = y+h/2
		pointsList.append(PointNode(p_x, p_y))

	return pointsList


