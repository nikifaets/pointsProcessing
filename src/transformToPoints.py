import numpy as np  
import pattern as pt
import cv2
import findLines as fb
from PointNode import PointNode


def transform(points, img, pat):

	h,w = img.shape
	coords = "coordinates.csv"
	pars = "pars.txt"


	pat.getCurrentMesh(points)
	lines = pat.findRows(points=pat.currPoints)
	currMatrix = pat.linesToMatrix(lines)

	linesimg = np.zeros((h,w),np.uint8)
	

	if lines:

		for line in lines:
			line.draw(linesimg)

	return linesimg, currMatrix