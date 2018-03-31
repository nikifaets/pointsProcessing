import cv2
import numpy as np 
from PointNode import PointNode

def getPoints(img, classiffier):

	points = classiffier.detectMultiScale(img)

	pointsList = list()
	for(x, y, h, w) in points:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 1)
		p_x = x+w/2
		p_y = y+h/2
		pointsList.append(PointNode(p_x, p_y))

	return pointsList


