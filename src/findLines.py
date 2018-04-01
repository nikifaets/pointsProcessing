import cv2
import numpy as np 
import math
from connectPoints import connect 
from Point import Point
from PointNode import PointNode
import queue
import time
from Line import Line

def getPoints(img,  width, height):


	pointsList = list()
	draft = np.zeros((height, width,1), np.uint8)
	ret,img = cv2.threshold(img, 100,255, cv2.THRESH_BINARY)

	connectivity = 8
	output = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_16U)
	num_labels = output[0]
	stats = output[2]

		
	centroids = output[3]
	#print("labels ", num_labels)

	

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

def collectLines(pointsList):

	lines = list()
	
	pointsList.sort(key = lambda point:point.y, reverse=False)

	start = 0
	counter = 0
	for i in range(1, len(pointsList)-1):

		p = pointsList[i]
		p_prev = pointsList[i-1]
		p_next = pointsList[i+1]

		diff_prev = math.fabs(p_prev.y-p.y)
		diff_next = math.fabs(p_next.y-p.y)
		
		counter+=1

		if diff_next >=8 or i == len(pointsList)-2:

			if i < len(pointsList)-2:
				line = Line(pointsList[start:i+1])
			else:
				line = Line(pointsList[start:i+2])
			start = i+1
			counter = 0
			lines.append(line)

	lines = fixLines(lines)

	return lines




def fixLines(lines):

		maxLen = 0

		for i in range(0, len(lines)):

			if i<len(lines):

				if lines[i].length<=3:
					del lines[i]


		for line in lines:

			if line.length > maxLen:
				maxLen = line.length

		for line in lines:

			avgXDist = 0
			xDistSum = 0
			counter = 1

			pointsList = line.getPoints()
			pointsList.sort(key = lambda point:point.x, reverse=False)

			#rp.rotatePoints(pointsList, PointNode(img.shape[1], img.shape[0]), self.rotation_angle)

			for i in range(0, len(pointsList)-1):

				xDistSum += pointsList[i].x
				counter+=1

			avgXDist = xDistSum/counter


			for i in range(1, len(pointsList)-1):

				if i < len(pointsList)-1:

					p = pointsList[i]
					p_prev = pointsList[i-1]
					p_next = pointsList[i+1]

					xDist_prev = math.fabs(p.x-p_prev.x)
					xDist_next = math.fabs(p.x-p_next.x)

					if xDist_next <= 0.5*avgXDist or xDist_prev <= 0.5*avgXDist:

						del pointsList[i]

			line = Line(pointsList)

		#rp.rotatePoints(pointsList, PointNode(img.shape[1], img.shape[0]), -self.rotation_angle)
		return lines