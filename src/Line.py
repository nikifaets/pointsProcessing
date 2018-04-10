from PointNode import PointNode
import cv2

class Line:


	def __init__(self, pointsList):
		self.pointsList = pointsList
		self.avg_y = self.mid_y()
		self.pointsList.sort(key = lambda point:point.x, reverse=False)
		self.length = len(self.pointsList)

	def draw(self, img):
		
		for i in range(0,len(self.pointsList)-1):
			x1 = self.pointsList[i].x
			y1 = self.pointsList[i].y
			x2 = self.pointsList[i+1].x
			y2 = self.pointsList[i+1].y
			cv2.line(img, (x1,y1), (x2,y2), 255, 1)

	def mid_y(self):

		sum = 0
		for point in self.pointsList:
			sum += point.y
		num = len(self.pointsList)

		if num <= 0:
			return 0

		return sum/num

	def getPoints(self):

		return self.pointsList

	def sort(self):

		self.pointsList.sort(key = lambda point:point.x, reverse=False)






	
