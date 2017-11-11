from Point import Point				

class Line:

	def __init__(self, a, b, dist):

		self.start = Point(a.x, a.y)
		self.end = Point(b.x, b.y) 
		self.length = dist


	
