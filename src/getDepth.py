import cv2
import numpy as np 
import findLines as fl
import rotatePoints as rp
from PointNode import PointNode


def writeVertices(file, pointsList):


	f = open(file, "w+")
	for point in pointsList:
		x = point.X
		y = point.Y
		z = point.Z

		vert = "v "+str(x) + " " + str(y) + " " + str(z) + "\n"
		f.write(vert)


def calculateDepth(pairs):

	list_c = list()
	list_n = list()

	for pair in pairs:

		point_c = pair[0]
		point_n = pair[1]

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

		list_c.append(point_c)
		list_n.append(point_n)
	return (list_c, list_n)




def getPointPairs(lines_c, lines_n, center):

	pairs = list()
	pointsList = list()
	for line_c in lines_c:

		for line_n in lines_n:

			
			if line_c.avg_y >= line_n.avg_y-15 and line_c.avg_y<=line_n.avg_y+15:

				if line_c.length == line_n.length:

					points_c = line_c.getPoints()
					points_n = line_n.getPoints()

					for i in range(0, len(points_c)):


						c = points_c[i]
						n = points_n[i]
						pairs.append((c,n))
	return pairs



def getDepth(cal, new, angle):


	h,w = cal.shape

	cal_test = np.zeros((h,w,1))
	new_test = np.zeros((h,w,1))

	center = PointNode(w/2, h/2)

	rotation_angle = angle

	ret,cal = cv2.threshold(cal, 100,255, cv2.THRESH_BINARY)
	ret,new = cv2.threshold(new, 100,255, cv2.THRESH_BINARY)

	pointsList_cal = fl.getPoints(cal, w, h)
	pointsList_new = fl.getPoints(new, w, h)

	rp.rotatePoints(pointsList_cal, PointNode(w/2, h/2), rotation_angle)
	rp.rotatePoints(pointsList_new, PointNode(w/2, h/2), rotation_angle)

	lines_cal = fl.collectLines(pointsList_cal)
	lines_new = fl.collectLines(pointsList_new)

	for line in lines_cal:
		line.draw(cal_test)


	for line in lines_new:
		line.draw(new_test)

	#rp.rotatePoints(pointsList_cal, PointNode(w/2, h/2), -rotation_angle)
	#rp.rotatePoints(pointsList_new, PointNode(w/2, h/2), -rotation_angle)



	pairs = getPointPairs(lines_cal, lines_new, center)
	rp.rotatePoints(pointsList_cal, PointNode(w/2, h/2), -rotation_angle)
	rp.rotatePoints(pointsList_new, PointNode(w/2, h/2), -rotation_angle)

	for pair in pairs:
		c = pair[0]
		n = pair[1]

		rp.rotatePoints([c], PointNode(w/2, h/2), -rotation_angle)
		rp.rotatePoints([n], PointNode(w/2, h/2), -rotation_angle)

	pointsList_cal, pointsList_new = calculateDepth(pairs)



	return (pointsList_new, pointsList_cal, cal_test, new_test)


'''
cal = cv2.imread("calibrated.jpg", 0)
new = cv2.imread("newGrid.jpg", 0)
angle = -38

pointsList, cal_test, new_test = getDepth(cal,new,angle)

writeVertices("model.obj", pointsList)



cv2.imshow("cal_test", cal_test)
cv2.imshow("new_test", new_test)
cv2.waitKey()'''

