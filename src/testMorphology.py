import cv2
import numpy as np  
import extractor as ext  
import findLines as fl 
import laserFindPoints as lfp 
import time

cap = cv2.VideoCapture(0)
cap.set(3,240)
cap.set(4,320)
projecting = False

while(True):
	millis = int(round(time.time() * 1000))
	ret, img = cap.read()

	
	thresh,grayscale = lfp.threshImage(img)
	kernel = np.ones((4,4), np.uint8)
	kernel_open = np.ones((2,2), np.uint8)
	erosion =  cv2.erode(thresh, kernel, 1)
	opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel_open)
	dilation = cv2.dilate(opening, kernel, 1)

	connectivity = 4
	output = cv2.connectedComponentsWithStats(dilation, connectivity, cv2.CV_16U)
	num_labels = output[0]
	centroids = output[3]
	#print(num_labels)

	points = np.zeros((thresh.shape[0], thresh.shape[1], 1), np.uint8)

	for i in centroids:
		#print(i[1], i[0])
		points.itemset((np.int(i[1]), np.int(i[0]), 0), 255)
	


	#pointsList, draft = fl.getPoints(dilation, thresh.shape[1], thresh.shape[0])

	


	#centroids = sorted(centroids, key = lambda point: point[1], reverse = False)
	#pointsList = sorted(pointsList, key = lambda point: point.y, reverse = False)


	#print(num_labels, len(pointsList))
	cv2.imshow("img", img)
	cv2.imshow("grayscale", grayscale)
	cv2.imshow("thresh", thresh)
	cv2.imshow("erosion", erosion)
	cv2.imshow("opening", opening)
	cv2.imshow("points", points)
	cv2.imshow("dilation", dilation)
	#cv2.imshow("draft", draft)

	millisnew = int(round(time.time() * 1000))
	#print(millisnew-millis)

	k = cv2.waitKey(1)
	if(k == 113):
		#cv2.imwrite("bfsslow.jpg", thresh)
		#print(centroids, pointsList)
		break


