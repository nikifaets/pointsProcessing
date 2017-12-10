import cv2
import numpy as np 
import math
from connectPoints import connect 
from connectPoints import sort
from Point import Point
from PointNode import PointNode
import heapq

def getPoints(img, draft, width, height):

	print(height,width)
	pointsList = list()
	mem = np.zeros((height, width), np.bool)

	for i in range(0, width):
		for j in range(0, height):
			#print("kur ", img[j][i]>100, mem[j][i] == False)
			if(img[j][i] > 100 and not mem[j,i]):
				
				maxw = (0,0)
				minw = (9999,9999)
				maxh = (0,0)
				minh = (9999,9999)
				#search white in the neighbours in a sideXside rectangle
				heap = []
				heapq.heappush(heap,(i,j))

				while len(heap) > 0:
					curr = heapq.heappop(heap)
					side = 2
					for h in range(curr[1]-side, curr[1]+side):
						for w in range(curr[0]-side, curr[0]+side):
							if w >= width:
								w = width-1
							if h >= height:
								h = height-1

							if(mem[h][w] == False):
								mem[h][w] = True
								if img[h][w] == 255:
									heapq.heappush(heap,(w,h))
									
									if h > maxh[1]:
										maxh = (w,h)
									if h < minh[1]:
										minh = (w,h)
									if w > maxw[0]:
										maxw = (w,h)
									if w < minw[0]:
										minw = (w,h)

				midh = int((maxh[1] + minh[1] + maxw[1] + minw[1])/4)
				midw = int((maxh[0] + minh[0] + maxw[0] + minw[0])/4)
				#print(midh,midw)
				pointsList.append(PointNode(midh,midw))
				draft[h][w] = 255
									

	return (pointsList,draft)
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
	print(width,height)

	#points = np.zeros((width,height), np.uint8)
	pointsList = list()
	nodesList = list()
	draft = np.zeros((height,width), np.uint8)

	pointsList,draft = getPoints(img, draft, width, height)

	ret = connect(pointsList)
	if ret == -1:
		return (draft, draft)

	lines = list()
	lines = collectLines(pointsList)

	showLines = drawLines(lines, width, height)

	return (draft, showLines)


def test(img):
	draft,showLines = createGrid(img)
	cv2.imshow("draft", draft)
	cv2.imshow("showLines", showLines)
	cv2.waitKey()


  
