import cv2
import numpy as np 
import math
from connectPoints import connect 
from connectPoints import sort
from Point import Point
from PointNode import PointNode
import heapq

def getPoints(img, draft, points, width, height):

	pointsList = list()
	mem = np.zeros((width, height), np.bool)

	for i in range(0, height):
		for j in range(0, width):
			if(img[j][i] > 100 and mem[j][i] == False):
				
				maxw = (0,0)
				minw = (9999,9999)
				maxh = (0,0)
				minh = (9999,9999)
				#search white in the neighbours in a sideXside rectangle
				heap = []
				heapq.heappush(heap,(j,i))

				while len(heap) > 0:
					curr = heapq.heappop(heap)
					side = 3
					for h in range(curr[1]-side, curr[1]+side):
						for w in range(curr[0]-side, curr[0]+side):
							if w >= width:
								w = width-1
							if h >= height:
								h = height-1

							if(mem[w][h] == False):
								mem[w][h] = True
								if img[w][h] == 255:
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
				print(midh,midw)
				pointsList.append(PointNode(midh,midw))
				draft[w][h] = 255
									

	return pointsList
# the main file for the moment - the connected lines are processed here
img = cv2.imread("demo/edged12.jpg", 0)
#img = cv2.imread("laser/demo.jpg", 0)
width,height = img.shape

def drawLines(lines, width, height):

	connectedLines = np.zeros((width, height), dtype = np.uint8)
	minlen = 999
	maxlen = 0
	counter = 0
	summ = 0
	for i in lines:
		x1 = i.start.x
		y1 = i.start.y

		x2 = i.end.x
		y2 = i.end.y
	

		cv2.line(connectedLines, (x1,y1), (x2,y2), 100, 1)

		#if(i.length==999):
		#	cv2.line(connectedLines, (x1,y1), (x2,y2), 250, 2)
		

	return connectedLines

def collectLines(points):
	lines = list()
	for i in points:
		received = i.convertToLine()
		lines.extend(received)

	return lines

cv2.imshow("img", img)
cv2.waitKey()

print(width,height)

points = np.zeros((width,height), np.uint8)
pointsList = list()
nodesList = list()
draft = np.zeros((width,height), np.uint8)
#np.copyto(draft, img)
img = cv2.medianBlur(img,1)

cv2.imshow("img", img)
cv2.waitKey()

pointsList = getPoints(img, draft, points, width, height)

print("points: ", len(pointsList))
cv2.imshow("points", points)
cv2.imshow("draft", draft)
cv2.waitKey()

connect(pointsList)
lines = list();
lines = collectLines(pointsList)

showLines = drawLines(lines, width, height)

#print(len(lines), len(pointsList))
cv2.imshow("draftWithLines", showLines)
cv2.imwrite("doc/connected1.jpg", showLines)
#cv2.imwrite("demo5.jpg", points)
cv2.waitKey()




  
