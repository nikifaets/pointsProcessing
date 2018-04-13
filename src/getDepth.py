import cv2
import numpy as np 
import findLines as fl
import rotatePoints as rp
from PointNode import PointNode
from Line import Line
import math


def getPointsPairs(cal, new, minYDiff):

	lines_cal = list()
	lines_new = list()
	pairs = list()

	for p in new:

		line_cal = fl.findClosestY(p, cal, minYDiff)
		line_new = fl.findClosestY(p, new, minYDiff)

	return (line_cal, line_new)

def findBestMatch(point, line_cal, line_new):

	line_cal.sort(key = lambda p: p.y, reverse = False)
	line_new.sort(key = lambda p: p.y, reverse = False)

	#check if there is one closest point:

	count = 0
	best = PointNode(0,0)
	for p_cal in line_cal:

		if int(p_cal.y) == int(point.y):
			count+=1
			best = p_cal

			if(count >= 2):
				break
	if count == 1:

		#print("FOUND MATCH: ", point.y, best.y)
		return best
	if count == 0:

		minDiff = 999
		for p_cal in line_cal:

			diff = math.fabs(p_cal.y-point.y)
			if diff < minDiff:
				minDiff = diff
				best = p_cal

		return best
	return PointNode(0,0)


def writeVertices(file, pointsList):


	f = open(file, "w+")
	for point in pointsList:
		x = point.X
		y = point.Y
		z = point.Z

		vert = "v "+str(x) + " " + str(y) + " " + str(z) + "\n"
		f.write(vert)


def calculateDepth(point_c, point_n):

	readp = open("pars.txt","r")
	L = float(readp.readline())
	d = float(readp.readline())
	kx = float(readp.readline())
	ky = float(readp.readline())
	prop = float(readp.readline())
	readp.close()

	point_n.x = 160-point_n.x
	point_n.y = 120-point_n.y

	point_c.x = 160-point_c.x
	point_c.y = 120-point_c.y
	kx = point_c.x*prop
	ky = point_c.y*prop
	point_c.X = d-L*kx
	point_c.Y = -L*ky
	point_c.Z = L

	X0 = point_c.X
	Y0 = point_c.Y

	kx = point_n.x*prop
	ky = point_n.y*prop

	point_n.X = float(X0)*float((d/(float(X0)+L*float(kx))))


	point_n.Y = float(Y0)*(d/(float(X0)+L*kx))
	point_n.Z = L*(d/(X0+L*kx))

	return point_c, point_n




def getLinePairs(lines_c, lines_n, center):

	pairs = list()
	pointsList = list()

	for line_c in lines_c:

		for line_n in lines_n:

			if math.fabs(line_c.avg_y - line_n.avg_y) <= 15:

				pairs.append((line_c, line_n))
	return pairs

def compareLines(line_c, line_n):

	points_c = line_c.getPoints()
	points_n = line_n.getPoints()
	
	for pn in points_n:

		minDiff = 9999
		bestCandidate = PointNode(0,0)

		for pc in points_c:

			diff  = math.fabs(pc.y-pn.y)
			
			if diff<=2:
	
				bestCandidate = pc

		if bestCandidate != PointNode(0,0):
			bestCandidate.sameRayCandidates.append(pn)

	pointsWithDepth_c = list()
	pointsWithDepth_n = list()


	for pc in points_c:

		if len(pc.sameRayCandidates)>0:

			pc,pn = calculateDepth(pc, pn)
			pointsWithDepth_c.append(pc)
			pointsWithDepth_n.append(pn)

	return (pointsWithDepth_c, pointsWithDepth_n)



def getDepth(cal, new, h,w, angle):

	cal_lines = np.zeros((h,w), np.uint8)
	new_lines = np.zeros((h,w), np.uint8)

	center = PointNode(w/2, h/2)

	rotation_angle = angle

	pointsList_cal = cal
	pointsList_new = new

	minYDiff = 5
	
	pairs = getPointsPairs(pointsList_cal, pointsList_new, minYDiff)

	points3d_c = list()
	points3d_n = list()

	for pair in pairs:

		p_c, p_n = pair
		p_c, p_n = calculateDepth(p_c, p_n)
		points3d_c.append(p_c)
		points3d_n.append(p_n)

	return (points3d_c, points3d_n)


