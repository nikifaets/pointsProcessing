from Point import Point
import math

class PointNode(Point):

	def __init__(self, x,y):
		super().__init__(x,y)

		self.nullpoint = Point(self.x, self.y)
		invalidDistance = 999;

		self.X = 0
		self.Y = 0
		self.Z = 0
		self.neighbors = list()
		self.sameRayCandidates = list()


	def write(self, point,dist):

		found = False
		for i in self.neighbors:
			if i[0] == point:
				found = True
				break
		if not found:
			self.neighbors.append((point,dist))

	def setCalibratedCoords(self, coords):
		self.X = coords[0]
		self.Y = coords[1]
		self.Z = coords[2]

	def setConnections(self,list):
		self.upleft = list[0]
		self.upcenter = list[1]
		self.upright = list[2]
		self.right = list[3]
		self.left = list[4]
		self.downright = list[5]
		self.downcenter = list[6]
		self.downleft = list[7]

	def convertToLine(self):
		#return list of Line objects to the closest right and closest upper point

		lines = list()

		for point in self.neighbors:
			if(point[0] != self.nullpoint):
				
				lines.append(Line(self, point[0], point[1], 32))
		
		return lines

	def filterCandidates(self):

		minDiff = 9999
		bestCandidate = PointNode(0,0)
		for p in self.sameRayCandidates:

			diff = math.fabs(p.y-self.y)

			if diff < minDiff:
				minDiff = diff
				bestCandidate = p

		return bestCandidate
