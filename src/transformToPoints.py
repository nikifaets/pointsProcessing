import numpy as np  
import pattern as pt
import cv2
import findLines as fb
from PointNode import PointNode


def transform(points, img, pat):

	h,w = img.shape
	coords = "coordinates.csv"
	pars = "pars.txt"

	'''coords = cal.calibrate(points)
	pars = cal.writeVertices("objfile2.obj", coords)'''
	pat.getCurrentMesh(points)
	lines = pat.findRows(points=pat.currPoints)
	currMatrix = pat.linesToMatrix(lines)

	linesimg = np.zeros((h,w),np.uint8)
	
	#print(len(lines))
	if lines:
		#print(len(lines))
		for line in lines:
			line.draw(linesimg)

	return linesimg, currMatrix

'''pat = pt.Pattern()
img = cv2.imread("calibrated.jpg",0)
h,w = img.shape
points = list()
for i in range(0,h):
	for j in range(0,w):
		if img[i][j] >100:
			points.append(PointNode(i,j))

#lines = transform(points, img, pat)
#print(len(lines))
matrix = pat.getMatrix()
print(len(matrix))
for i in matrix:
	for j in i:
		print(j.x, j.y)
print(matrix[0])
#cv2.imshow("lines", lines)
#cv2.waitKey()'''