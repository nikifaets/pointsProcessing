import cv2
import numpy as np 
import math
from connectPoints import connect 
from Point import Point
from PointNode import PointNode
import queue
import time

def getPoints(img,  width, height):


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
									

	
	if len(stats) != 2:
		return (pointsList,draft, 0)
	return (pointsList, draft, stats[1])

	

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

def collectLines(points):
	lines = list()
	for i in points:
		received = i.convertToLine()
		lines.extend(received)

	return lines

def createGrid(img):

	height,width = img.shape
	

	#points = np.zeros((width,height), np.uint8)
	pointsList = list()
	nodesList = list()
	draft = np.zeros((height,width), np.uint8)

	pointsList,draft, stats = getPoints(img, width, height)

	return draft,pointsList,stats


def test(img):
	draft,showLines = createGrid(img)
	cv2.imshow("draft", draft)
	cv2.imshow("showLines", showLines)
	cv2.waitKey()
