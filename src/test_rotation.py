import cv2
import rotatePoints as rp  
import numpy as np
from PointNode import PointNode
import time

def getPoints(img,  width, height):


	pointsList = list()
	draft = np.zeros((height, width,1), np.uint8)
	ret,img = cv2.threshold(img, 100,255, cv2.THRESH_BINARY)

	connectivity = 8
	output = cv2.connectedComponentsWithStats(img, connectivity, cv2.CV_16U)
	num_labels = output[0]
	stats = output[2]

		
	centroids = output[3]
	#print("labels ", num_labels)

	

	for p in range(1, len(centroids)):

		if p>0:

			i = centroids[p]
			draft.itemset((np.int(i[1]), np.int(i[0]), 0), 255)
			pointsList.append(PointNode(i[0], i[1]))

	return pointsList


img = cv2.imread("test/testCal2.jpg", 0)

pointsList = getPoints(img, img.shape[1], img.shape[0])
print(len(pointsList))
rp.rotatePoints(pointsList, PointNode(img.shape[1]/2, img.shape[0]/2), 18)
edited = np.zeros((img.shape[0], img.shape[1],1), np.uint8)

for p in pointsList:

	cv2.circle(edited, (int(p.x), int(p.y)), 5, 200, -1)

cv2.imshow("img", img)
cv2.imshow("edited", edited)
cv2.waitKey()


'''
pointsList = list()
point = PointNode(150,250)
point1 = PointNode(30,50)
pointsList.append(point)
pointsList.append(point1)

while(True):

	img = np.zeros((320,480,1), np.uint8)
	rp.rotatePoints(pointsList, PointNode(img.shape[1]/2, img.shape[0]/2), 5)

	for p in pointsList:

		cv2.circle(img, (p.x, p.y), 4, 200, -1)

	cv2.imshow("img", img)
	time.sleep(0.05)
	k = cv2.waitKey(1)
	if k == ord("q"):
		break

'''
