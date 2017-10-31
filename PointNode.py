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
