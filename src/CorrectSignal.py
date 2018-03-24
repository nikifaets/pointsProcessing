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

		print(self.hist_w, self.hist_h)
		# calculate the number of bins, where the number of points in the current bin is being counted
		# first h of array, then w

		self.hist_new = np.zeros((self.hist_h+1, self.hist_w+1), np.uint8)
		self.hist_orig = np.zeros((self.hist_h+1, self.hist_w+1), np.uint8)

		

	def update(self, pointsList):

		if self.bufCounter>=self.bufSize:

			for i in range(0, self.hist_h):
				for j in range(0, self.hist_w):

					print(self.hist_new[1][1])
					if self.hist_new[i][j] >= self.minCount:

						print(i,j, self.hist_w*j, self.hist_h*i)
						self.hist_orig[i][j] = 1
						

					else:
						self.hist_orig[i][j] = 0
						
			self.hist_new = np.copy(self.hist_orig)
			self.bufCounter = 0

		self.createHistogram(pointsList)

	def createHistogram(self, pointsList):


		for p in pointsList:
			x_pos = int(p.x/self.roi_w)
			y_pos = int(p.y/self.roi_h)

			
			#print(p.x, "-> ", x_pos)

			self.hist_new[y_pos][x_pos] +=1

		self.bufCounter+=1

	def getFixedData(self):

		pointsList = list()

		for i in range(0, self.hist_h):
				for j in range(0, self.hist_w):

					if self.hist_orig[i][j]>=1:
						pointsList.append(PointNode(j*self.roi_w, i*self.roi_h))

		return pointsList

	def showHistograms(self):

		print("old")
		print(self.hist_orig)
		print("new")
		print(self.hist_new)


		

