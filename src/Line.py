from PointNode import PointNode
import cv2


class Line:


	def __init__(self, poinstList):
		self.pointsList = pointsList
		self.avg_y = self.mid_y()
		self.pointsList.sort(key = lambda point:point.x, reverse=False)

	def draw(self, img):
		
		for i in range(0,len(self.points)-1):
			x1 = self.points[i].x
			y1 = self.points[i].y
			x2 = self.points[i+1].x
			y2 = self.points[i+1].y
			cv2.line(img, (x1,y1), (x2,y2), 255, 1)

	def mid_y(self):

		sum = 0
		for point in self.points:
			sum += point.y
		num = len(self.points)
		return sum/num



	
