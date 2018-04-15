import cv2
import numpy as np  
from PointNode import PointNode
import math
import getDepth as gd
from Line import Line
import findLines as fl

def calibrate(points, file):

	readp = open(file,"r")
	L = float(readp.readline())
	d = float(readp.readline())
	kx = float(readp.readline())
	ky = float(readp.readline())
	prop = float(readp.readline())
	readp.close()

	#points = .fixLines(points)
	for point in points:

		

		#rotate the coordinate system (because it's the rotated on the camera's matrix)

		x = 160 - point.x
		y = 120 - point.y

		kx = (x*prop)
		ky = (y*prop)
		point.X = d-L*kx
		point.Y = -L*ky
		point.Z = L

		

		gd.writeVertices("calibrated.obj", points)
	return points

def calibrateFromImage(img, file):

	img = cv2.imread(img, 0)
	pointsList = fl.getPoints(img)
	pointsList = calibrate(pointsList, "pars.txt")

	return pointsList

