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

		lines = self.findRows(points=self.savedPoints)

		self.matrix = self.linesToMatrix(lines)
	
				
		#print("neghthhhh",len(self.matrix))

	def linesToMatrix(self, lines):

		lines.sort(key=lambda x: x.avg_y, reverse=False)
		width = 30
		matrix = list()
		for i in range(0, len(lines)):
			#print(lines[i].avg_y)
			points = lines[i].points
			#print("for everyline")
			row = list()
			for j in range(0, len(points)):
				#print("insert points")
				
				#print("appending ", points[j])
				row.append(points[j])
			#for p in row:
			#	print(p.x, p.y)
			#print("----------------------")
			matrix.append(row)
		#print("neghthhhh",len(self.matrix))
		return matrix

	def getCurrentMesh(self,points):
		self.currPoints = points

	def findRows(self,points):

		#print(self.points[0])
		
		for point in points:
	

			neighs = cp.findNeighbours(point,points)
			bestn = cp.makeConnectionByMinYdiff(point, neighs)
	
			point.write(bestn, 32)
			bestn.write(point, 32)

	
		lines = self.defineLines(points)
		return lines

	def defineLines(self, points):

		lines = []
		mem = []
		for point in points:
			#print("point ", point.x, point.y)
			f = False
			for i in mem:
				if i == point:
					f = True
					break
			if not f:
				#print("not in mem")
				frontl = queue.Queue()
				collected = []
				
				frontl.put(point)
				mem.append(point)
				collected.append(point)
				while(frontl.qsize()>0):
					
					curr = frontl.get()
					#print("loop", len(frontl), curr.x, curr.y)
					
					#print(len(curr.neighbors))
					for neigh in curr.neighbors:
						
						n = neigh[0]
						#print("neighbor ", n.x, n.y)
						found = False
						for i in mem:
							#print(i,n)
							if i == n:
								#print("passed")
								found = True
								break

						if not found and n!=PointNode(0,0):
							#print("neighbor not in mem")
							mem.append(n)
							frontl.put(n)
							collected.append(n)
			#print(len(collected))
				#if len(collected) >=5:
				lines.append(Line(collected))
		#print (lines)
		return lines

	def compareWithPattern(self,currMatrix):

		coords = list()
		for i in range(0, len(currMatrix)):
			for p in range(0, len(currMatrix[i])):


				saved_point = self.matrix[i][p]
				X0 = saved_point.X
				Y0 = saved_point.Y
				Z0 = saved_point.Z

				X = X0*(self.d/(X0+self.L*self.kx))
				Y = Y0*(self.d/(X0+self.L*self.kx))
				Z = self.L*(self.d/(X0+self.L*self.kx))
				coords.append((X,Y,Z))

		self.writeVertices("surface.obj", coords)

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



