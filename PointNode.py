from Point import Point

class PointNode(Point):

	def __init__(self, x,y):
		super().__init__(x,y)

		nullpoint = Point(self.x, self.y)

		self.upleft = nullpoint
		self.upcenter = nullpoint
		self.upright = nullpoint
		self.right = nullpoint
		self.left = nullpoint
		self.downright = nullpoint
		self.downcenter = nullpoint
		self.downleft = nullpoint

	def setConnections(self,list):
		self.upleft = list[0]
		self.upcenter = list[1]
		self.upright = list[2]
		self.right = list[3]
		self.left = list[4]
		self.downright = list[5]
		self.downcenter = list[6]
		self.downleft = list[7]
		