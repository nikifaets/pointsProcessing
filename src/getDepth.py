import cv2
import numpy as np 
import findLines as fl
import rotatePoints as rp
from PointNode import PointNode
import math


def getPointsPairs(cal, new, minYDiff):

	cal.sort(key = lambda point:point.y, reverse=False)
	new.sort(key = lambda point:point.y, reverse=False)

	lines_cal = list()
	line_curr = list()
	line_curr.append(cal[0])
	cal_idx = 0
	for i in range(0, len(cal)-1):

		diff = math.fabs(cal[i].y-cal[i+1].y)
		if diff <= minYDiff:
			line_curr.append(cal[i+1])
		else:
			lines_cal.append(Line(line_curr))
			line_curr = []


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
			
			if diff<=5:
	
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
	lines_cal = fl.collectLines(pointsList_cal, minYDiff)
	lines_new = fl.collectLines(pointsList_new, minYDiff)


	for line in lines_cal:

		line.draw(cal_lines)

		#for p in line.pointsList:
			#cv2.circle(cal_lines, (p.x, p.y), 4, 200, -1)
	print("first")
	for line in lines_new:
		line.draw(new_lines)

		#for p in line.pointsList:
			#cv2.circle(new_lines, (p.x, p.y), 4, 200, -1)

	print("sdf")
	point3d_c = list()
	points3d_n = list()

	return (points3d_c, points3d_n, cal_lines, new_lines)


