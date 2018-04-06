import cv2
import numpy as np

def selectROI(img):
	
	h,w,channels = img.shape

	gray = rgb2gray(img)
	gray = cv2.add(gray, -180)	
	ret,g = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	kernel = np.ones((15,15), np.uint8)
	g = cv2.dilate(g, kernel, 1)

	b = np.zeros((h,w),np.uint8)
	r = np.zeros((h,w),np.uint8)
	np.copyto(b,g)
	np.copyto(r,g)

	#r = np.zeros((h,w,1),np.uint8)

	res = cv2.merge((b,g,r))


	return res



def rgb2gray(img):

	b,g,r = cv2.split(img)
	
	return g

def getROI(img):

	binary = selectROI(img)


	g = cv2.split(binary)[2]

	connectivity = 4
	
	output = cv2.connectedComponentsWithStats(g, connectivity, cv2.CV_32S)
	num_labels = output[0]
	stats = output[2]

	rois = list()
	for i in range(1, num_labels):

		x,y,w,h,area = stats[i]
		#print("y ", y, "x ", x, "w ", w, "h ", h)
		roi = img[y:y+h,x:x+w]
		cv2.rectangle(img, (x,y),(x+w,y+h), (0,0,255), 1)
		rois.append((roi, (x,y)))

	return rois, g



