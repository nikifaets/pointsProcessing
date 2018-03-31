import numpy as np 
import queue
import connectPoints as cp
from PointNode import PointNode
from Line import Line
import csv
import cv2

class Pattern:

	L = 0
	d = 0
	kx = 0
	ky = 0
	Xi = 0
	Yi = 0


	def __init__(self, pars = "pars.txt", coords = "coordinates.csv"):
		readp = open(pars,"r")
		self.L = float(readp.readline())
		self.d = float(readp.readline())
		self.kx = float(readp.readline())
		self.ky = float(readp.readline())
		readp.close()

		self.points3d = list()
		self.points2d = list()
		self.savedPoints = list()
		self.matrix = list()
		self.currPoints = list()
		self.readCoordinates(coords)


	def getMatrix(self):
		return self.matrix

	def readCoordinates(self,file):

		f = open(file, "r")
		reader = csv.reader(f)

		for row in reader:

			x = float(row[0])
			y = float(row[1])
			X = float(row[2])
			Y = float(row[3])
			Z = float(row[4]) 

			x = int(x)
			y = int(y)
			p = PointNode(x,y)

			p.setCalibratedCoords((X,Y,Z))
			self.savedPoints.append(p)
			self.points2d.append(p)
			self.points3d.append(p)

		
	


	def getCurrentMesh(self,points):
		self.currPoints = points


	def getDepth(self,pointsList):

		coords = list()
		readp = open("pars.txt","r")
		L = float(readp.readline())
		d = float(readp.readline())
		kx = float(readp.readline())
		ky = float(readp.readline())
		prop = float(readp.readline())
		readp.close()

		if len(pointsList) == len(self.points2d):

			sortedCal = sorted(self.points2d, key = lambda point: point.y, reverse = True)
			sortedNew = sorted(pointsList, key = lambda point: point.y, reverse = False)

			for i in range(0, len(pointsList)):

				
				calP = sortedCal[i]
				newP = sortedNew[i]

				newP.x = 160-newP.x
				newP.y = 120-newP.y

				print("COMPARE", calP.x, calP.y, newP.x, newP.y)
				kx = prop*newP.x
				ky  = prop*newP.y


				X0 = calP.X
				Y0 = calP.Y
				Z0 = calP.Z
				#print(X0, Y0, Z0)
				#print(type(X0))
				X = X0*(d/(X0+L*kx))
				Y = Y0*(d/(X0+L*kx))
				Z = L*(d/(X0+L*kx))
				Z1 = d/(d-L*prop*(calP.x - newP.x))
				

				newP.setCalibratedCoords((X, Y, Z))
				coords.append((X,Y,Z))

		self.writeVertices("3D.obj", coords)

		for i in self.points2d:
			print(i.X, i.Y, i.Z)

		print("----------------------------------------------------")

		for i in pointsList:
			print(i.X, i.Y, i.Z)

	def writeVertices(self, file, coords):

		f = open(file, "w+")
		for point in coords:
			x,y,z = point
			vert = "v "+str(x) + " " + str(y) + " " + str(z) + "\n"
			f.write(vert)



