import cv2
import numpy as np 
from connectPoints import connect 
from connectPoints import sort
from Point import Point
from PointNode import PointNode

# the main file for the moment - the connected lines are processed here
img = cv2.imread("demoEdge.jpg", 0)
#img = cv2.imread("laser/demo.jpg", 0)
width,height = img.shape

def drawConnectLines(nodes, width, height):

	connectedLines = np.zeros((width, height), dtype = np.uint8)

	for i in range(0, len(nodes)):

		node = nodes[i]
		x = node.x
		y = node.y
		xright = node.right.x
		yright = node.right.y
		xleft = node.left.x
		yleft = node.left.y
		xup = node.upcenter.x
		yup = node.upcenter.y
		xdown = node.downcenter.x
		ydown = node.downcenter.y

		#cv2.circle(connectedLines, (x,y), 3, 100, -1)
		cv2.line(connectedLines, (x, y), (xright, yright), 100, 1)
		cv2.line(connectedLines, (x, y), (xleft, yleft), 100, 1)
		cv2.line(connectedLines, (x, y), (xup, yup), 100, 1)
		cv2.line(connectedLines, (x, y), (xdown, ydown), 100, 1)

	return connectedLines


cv2.imshow("img", img)

print(width,height)

points = np.zeros((width,height), np.uint8)
pointsList = list()
nodesList = list()
mem = np.zeros((width, height), np.bool)
draft = np.zeros((width,height), np.uint8)
np.copyto(draft, img)

for i in range(0, height):
	for j in range(0, width):
		if(img[j][i] > 100 and mem[j][i] == False):
			#print(img[j][i], i, j, type(img[j][i]))
			cv2.circle(draft, (i,j), 5, (200,0,0), 1)
			points[j][i] = 255
			point = PointNode(i,j)
			pointsList.append(point)
			radius = 20
			diameter = 2*radius
			
			for x in range(j - radius, j + radius):
				if(x>=width):
					x = width - 1
				for y in range(i, i + diameter):

					if(y>=height):
						y = height-1
					#print(width, x, height, y)
					mem[x][y] = True



print("points: ", len(pointsList))
cv2.imshow("points", points)
cv2.imshow("draft", draft)
cv2.waitKey()

connect(pointsList)

showLines = drawConnectLines(pointsList, width, height)

#print(len(lines), len(pointsList))
cv2.imshow("draftWithLines", showLines)
cv2.waitKey()




  
