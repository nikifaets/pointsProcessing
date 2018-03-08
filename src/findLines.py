import cv2
import numpy as np 
import math
from connectPoints import connect 
from connectPoints import sort
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
	#print("labels ", num_labels)

	

	for p in range(1, len(centroids)):

		if p>0:

			i = centroids[p]
			draft.itemset((np.int(i[1]), np.int(i[0]), 0), 255)
			pointsList.append(PointNode(i[0], i[1]))
									

	
	#print(millisnew-millis)
	if len(stats) != 2:
		return (pointsList,draft, 0)
	return (pointsList, draft, stats[1])
	#return pointsList
	
# the main file for the moment - the connected lines are processed here
#img = cv2.imread("demo/edged6.jpg", 0)
#img = cv2.imread("laser/demo.jpg", 0)
#width,height = img.shape

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

		#if(i.length==999):
		#	cv2.line(connectedLines, (x1,y1), (x2,y2), 250, 2)
		

	return connectedLines

def collectLines(points):
	lines = list()
	for i in points:
		received = i.convertToLine()
		lines.extend(received)

	return lines

def createGrid(img):
	#cv2.imshow("img", img)

	height,width = img.shape
	

	#points = np.zeros((width,height), np.uint8)
	pointsList = list()
	nodesList = list()
	draft = np.zeros((height,width), np.uint8)

	pointsList,draft, stats = getPoints(img, width, height)

	'''ret = connect(pointsList)
	if ret == -1:
		return (draft, draft,[PointNode(0,0)])
	lines = list()
	lines = collectLines(pointsList)
	showLines = drawLines(lines, width, height)'''

	#return (draft, showLines, pointsList)

	return draft,pointsList,stats


def test(img):
	draft,showLines = createGrid(img)
	cv2.imshow("draft", draft)
	cv2.imshow("showLines", showLines)
	cv2.waitKey()


'''img = cv2.imread("demo/edged24.jpg",0)
test(img)'''