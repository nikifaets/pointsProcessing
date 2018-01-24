import cv2
import numpy as np  
import pattern
from PointNode import PointNode
import csv

class calibrator:
	d = 21.5
	L = 50
	prop = 0.00218
	kx = 0
	ky = 0

	def calibrate(self,points):

		coords = list()
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
		self.writeVertices("vertices.obj","pars.txt", coords)
		self.writeCoordinates("coordinates.csv", coords)
		print("CALIBRATED")


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


