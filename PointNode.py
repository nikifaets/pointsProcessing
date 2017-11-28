from Point import Point
from Line import Line

class PointNode(Point):

	def __init__(self, x,y):
		super().__init__(x,y)

		self.nullpoint = Point(self.x, self.y)
		invalidDistance = 999;

		self.neighbors = list()

		self.upleft = (self.nullpoint,invalidDistance)
		self.upcenter = (self.nullpoint,invalidDistance)
		self.upright = (self.nullpoint,invalidDistance)
		self.right = (self.nullpoint,invalidDistance)
		self.left = (self.nullpoint,invalidDistance)
		self.downright = (self.nullpoint,invalidDistance)
		self.downcenter = (self.nullpoint,invalidDistance)
		self.downleft = (self.nullpoint,invalidDistance)
		'''self.neighbors.append(self.upleft)
		self.neighbors.append(self.upcenter)
		self.neighbors.append(self.upright)
		self.neighbors.append(self.right)
		self.neighbors.append(self.left)
		self.neighbors.append(self.downright)
		self.neighbors.append(self.downcenter)
		self.neighbors.append(self.downleft)'''



	def write(self, point,dist):
		self.neighbors.append((point,dist))

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
				
				lines.append(Line(self, point[0], point[1]))
		
		return lines