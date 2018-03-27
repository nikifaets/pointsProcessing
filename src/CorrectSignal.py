import numpy as np  
from PointNode import PointNode

class CorrectSignal:

	

	def __init__(self, imgDimensions, roiSize, bufSize, minCount):

		self.bufCounter = 0
		self.minCount = minCount
		self.bufSize = bufSize

		self.roi_w = roiSize[0]
		self.roi_h = roiSize[1]
		self.img_w = imgDimensions[0]
		self.img_h = imgDimensions[1]
		self.hist_w = int(self.img_w/self.roi_w)
		self.hist_h = int(self.img_h/self.roi_h)

		
		# calculate the number of bins, where the number of points in the current bin is being counted
		# first h of array, then w
		#dimension 0 is number of points in area, dimension 1 is average x coordinate, dimension 2 is average y coordinate

		self.hist_new = np.zeros((self.hist_h+1, self.hist_w+1, 3), np.int32)
		self.hist_orig = np.zeros((self.hist_h+1, self.hist_w+1, 3), np.int32)

		

	def update(self, pointsList):

		if self.bufCounter>=self.bufSize:

			for i in range(0, self.hist_h):
				for j in range(0, self.hist_w):

					
					if self.hist_new[i][j][0] >= self.minCount:

						num = self.hist_new[i][j][0]
						x = self.hist_new[i][j][1]
						y = self.hist_new[i][j][2]

						self.hist_orig[i][j][0] = 1
						self.hist_orig[i][j][1] = int(x/num)
						self.hist_orig[i][j][2] = int(y/num)
						

					else:
						self.hist_orig[i][j][0] = 0
						self.hist_orig[i][j][1] = 0
						self.hist_orig[i][j][2] = 0
						
			self.hist_new = np.copy(self.hist_orig)
			self.bufCounter = 0

		self.createHistogram(pointsList)

	def createHistogram(self, pointsList):


		for p in pointsList:
			x_pos = int(p.x/self.roi_w)
			y_pos = int(p.y/self.roi_h)

			
			#print(p.x, "-> ", x_pos)

			
			self.hist_new[y_pos][x_pos][0] +=1
			self.hist_new[y_pos][x_pos][1] += int(p.x)
			self.hist_new[y_pos][x_pos][2] += int(p.y)


		self.bufCounter+=1

	def getFixedData(self):

		pointsList = list()

		for i in range(0, self.hist_h):
				for j in range(0, self.hist_w):

					if self.hist_orig[i][j][0]>=1:

						x = self.hist_orig[i][j][1]
						y = self.hist_orig[i][j][2]

						pointsList.append(PointNode(x, y))

		return pointsList

	def showHistograms(self):

		print("old")
		print(self.hist_orig)
		print("new")
		print(self.hist_new)


		

