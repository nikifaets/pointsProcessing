import cv2
import numpy as np 
import math
from connectPoints import connect 
from Point import Point
from PointNode import PointNode
import queue
import time
from Line import Line

def getPoints(img):

	height,width = img.shape
	pointsList = list()
	draft = np.zeros((height, width,1), np.uint8)
	ret,img = cv2.threshold(img, 100,255, cv2.THRESH_BINARY)

	connectivity = 8
	output = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_16U)
	num_labels = output[0]
	stats = output[2]

		
	centroids = output[3]
	

	for p in range(1, len(centroids)):

		if p>0:

			i = centroids[p]
			draft.itemset((np.int(i[1]), np.int(i[0]), 0), 255)
			pointsList.append(PointNode(i[0], i[1]))
									

	return pointsList

def drawLines(lines, width, height):

	connectedLines = np.zeros((height, width), dtype = np.uint8)
	minlen = 999
	maxlen = 0
	counter = 0
	summ = 0
	for i in lines:
		x1 = i.start.x
		y1 = i.start.y

		x2 = i.end.x
		y2 = i.end.y
	

		cv2.line(connectedLines, (y1,x1), (y2,x2), 100, 1)


	return connectedLines

def collectLines(pointsList, minYDiff):

	pointsList.sort(key = lambda point:point.y, reverse=False)

	for p in pointsList:
		print (p.y)
	lines = list()
	line_curr = list()
	line_curr.append(pointsList[0])
	avg_y = pointsList[0].y
	cal_idx = 0

	for i in range(0, len(pointsList)-1):

		pointsList[i].x = int(pointsList[i].x)
		pointsList[i].y = int(pointsList[i].y)
		diff = math.fabs(avg_y-pointsList[i+1].y)

		if diff <= minYDiff:

			line_curr.append(pointsList[i+1])

			avg_y = 0

			for p in line_curr:
				avg_y += p.y
			avg_y = avg_y/len(line_curr)

		else:

			lines.append(Line(line_curr))
			line_curr = []
			line_curr.append(pointsList[i+1])
			avg_y = pointsList[i+1].y

	return lines

def findClosestY(point, pointsList, minYDiff):

	pointsList.sort(key = lambda point:point.y, reverse=False)

	line = list()

	minDiff = 999
	for p_new in pointsList:

		if math.fabs(point.y-p_new.y) <= minDiff:
				minDiff = math.fabs(point.y-p_new.y)

		'''else: 
			if p_new.y > point.y:
				break'''

	for p_new in pointsList:

		if math.fabs(point.y-p_new.y) <= minDiff:
				line.append(p_new)

	return line

def fixLines(lines):

		maxLen = 0

		for i in range(0, len(lines)):

			if i<len(lines):

				if lines[i].length<=3:
					del lines[i]

		return lines