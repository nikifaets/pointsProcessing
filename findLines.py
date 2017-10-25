import cv2
import numpy as np 
from connectPoints import connect 
from connectPoints import sort
from Point import Point
	
img = cv2.imread("edged5.jpg", 0)

cv2.imshow("img", img)

width,height = img.shape
print(width,height)

points = np.zeros((width,height), np.uint8)
pointsList = list()
mem = np.zeros((width, height), np.bool)
draft = np.zeros((width,height), np.uint8)
np.copyto(draft, img)

for i in range(0, height):
	for j in range(0, width):
		if(img[j][i] > 100 and mem[j][i] == False):
			#print(img[j][i], i, j, type(img[j][i]))
			cv2.circle(draft, (i,j), 5, (200,0,0), 1)
			points[j][i] = 255
			point = Point(i,j)
			pointsList.append(point)
			radius = 8
			diameter = 2*radius
			
			for x in range(j - radius, j + radius):
				if(x>=width):
					x = width - 1
				for y in range(i, i + diameter):

					if(y>=height):
						y = height-1
					#print(width, x, height, y)
					mem[x][y] = True




cv2.imshow("points", points)
cv2.imshow("draft", draft)
cv2.waitKey()
pointsList = sort(pointsList)
lines = connect(pointsList)
for i in range(0, len(lines)):
	a = lines[i].start
	b = lines[i].end
	cv2.line(draft, (a.x, a.y), (b.x, b.y), 100, 1)

print(len(lines), len(pointsList))
cv2.imshow("draftWithLines", draft)
cv2.waitKey()




  
