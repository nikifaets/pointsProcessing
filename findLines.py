import cv2
import numpy as np 
import math
from connectPoints import connect 
from connectPoints import sort
from Point import Point
from PointNode import PointNode

# the main file for the moment - the connected lines are processed here
img = cv2.imread("edged25.jpg", 0)
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
		

		#print(i.length)

		if(i.length > maxlen and i.length!=999):
			maxlen = i.length
			counter+=1
			summ +=i.length
			

		if(i.length<minlen):
			print("kur")
			counter+=1
			minlen = i.length
			summ +=i.length
		#if(i.length==999):
		#	cv2.line(connectedLines, (x1,y1), (x2,y2), 250, 2)

	summ/= counter
	print(int(minlen), int(maxlen), summ)
	minlen = int(minlen)
	maxlen = int(maxlen)
	summ = (summ+maxlen)/2
	maxlen = summ

	step = int(240/(math.fabs(maxlen-minlen)))
	print(step)
	thicknessStep = 24


	for i in lines:
		x1 = i.start.x
		y1 = i.start.y

		x2 = i.end.x
		y2 = i.end.y

		brightness = minlen+int(math.sqrt(math.pow(x1-x2, 2) + math.pow(y1-y2, 2)))*step
		#print(brightness)
		thickness = int(brightness/thicknessStep)
		thickness = int(thickness/3)
		if(thickness > 3):
			thickness = 3
		if(thickness<1):
			thickness =1


		cv2.line(connectedLines, (x1,y1), (x2,y2), brightness, 1)

		#if(i.length==999):
		#	cv2.line(connectedLines, (x1,y1), (x2,y2), 250, 2)
		

	return connectedLines

def collectLines(points):
	lines = list()
	for i in points:
		line1, line2 = i.convertToLine()
		lines.append(line1)
		lines.append(line2)

	return lines

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
			radius = 5
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
lines = list();
lines = collectLines(pointsList)

showLines = drawLines(lines, width, height)

#print(len(lines), len(pointsList))
cv2.imshow("draftWithLines", showLines)
cv2.imwrite("demo4.jpg", showLines)
cv2.imwrite("demo5.jpg", points)
cv2.waitKey()




  
