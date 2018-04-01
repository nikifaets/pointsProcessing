import cv2
import numpy as np  
import pattern
from PointNode import PointNode
import csv
import rotatePoints as rp
import math
from Line import Line

class calibrator:
	d = 21.5
	L = 50
	prop = 0.00218
	kx = 0
	ky = 0
	rotation_angle = -38

	def calibrate(self,points, img):

		coords = list()

		#points = self.fixLines(points)
		for point in points:

			

			#rotate the coordinate system (because it's the rotated on the camera's matrix)
			point.x = 160-point.x
			point.y = 120-point.y

			x = point.x
			y = point.y


			

			self.kx = (x*self.prop)
			self.ky = (y*self.prop)
			X = self.d-self.L*self.kx
			Y = -self.L*self.ky
			Z = self.L

			

			point.setCalibratedCoords((X,Y,Z))

			coords.append((point,(X,Y,Z)))
		self.writeVertices("calibration.obj","pars.txt", coords)
		self.writeCoordinates("coordinates.csv", coords)
		print("CALIBRATED:")


	def writeVertices(self, vertices, parameters, points):

		f = open(vertices, "w+")
		for point in points:
			x,y,z = point[1]
			vert = "v "+str(x) + " " + str(y) + " " + str(z) + "\n"
			f.write(vert)

		f1 = open(parameters, "w+")
		#1.L/ 2.d/ 3.kx/ 4.ky
		pars = str(self.L) + "\n" + str(self.d) + "\n" + str(self.kx) + "\n" + str(self.ky) + "\n" + str(self.prop)+"\n"
		f1.write(pars)
		f1.close()

	def writeCoordinates(self, file, coords):

		f = open(file, "w")
		writer = csv.writer(f)

		for i in coords:
			x = i[0].x
			y = i[0].y

			X,Y,Z = i[1]

			row = [float(x), float(y), float(X), float(Y), float(Z)]
			writer.writerow(row)


	def fixLines(self, lines):

		maxLen = 0

		for i in range(0, len(lines)):

			if i<len(lines):

				if lines[i].length<=3:
					del lines[i]


		for line in lines:

			if line.length > maxLen:
				maxLen = line.length

		for line in lines:

			avgXDist = 0
			xDistSum = 0
			counter = 1

			pointsList = line.getPoints()
			pointsList.sort(key = lambda point:point.x, reverse=False)
			print(pointsList)
			#rp.rotatePoints(pointsList, PointNode(img.shape[1], img.shape[0]), self.rotation_angle)

			for i in range(0, len(pointsList)-1):

				xDistSum += pointsList[i].x
				counter+=1

			avgXDist = xDistSum/counter
			print(avgXDist)


			for i in range(1, len(pointsList)-1):

				if i < len(pointsList)-1:
					print(i, len(pointsList)-1)
					p = pointsList[i]
					p_prev = pointsList[i-1]
					p_next = pointsList[i+1]

					xDist_prev = math.fabs(p.x-p_prev.x)
					xDist_next = math.fabs(p.x-p_next.x)

					if xDist_next <= 0.5*avgXDist or xDist_prev <= 0.5*avgXDist:

						print(xDist_next, xDist_prev)
						del pointsList[i]

			line = Line(pointsList)

		#rp.rotatePoints(pointsList, PointNode(img.shape[1], img.shape[0]), -self.rotation_angle)
		return lines



