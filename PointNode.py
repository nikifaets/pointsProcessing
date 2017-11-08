from Point import Point

class PointNode(Point):

	def __init__(self, x,y):
		super().__init__(x,y)

		nullpoint = Point(self.x, self.y)
		invalidDistance = 999;

		self.upleft = (nullpoint,invalidDistance)
		self.upcenter = (nullpoint,invalidDistance)
		self.upright = (nullpoint,invalidDistance)
		self.right = (nullpoint,invalidDistance)
		self.left = (nullpoint,invalidDistance)
		self.downright = (nullpoint,invalidDistance)
		self.downcenter = (nullpoint,invalidDistance)
		self.downleft = (nullpoint,invalidDistance)

	def setConnections(self,list):
		self.upleft = list[0]
		self.upcenter = list[1]
		self.upright = list[2]
		self.right = list[3]
		self.left = list[4]
		self.downright = list[5]
		self.downcenter = list[6]
		self.downleft = list[7]
		