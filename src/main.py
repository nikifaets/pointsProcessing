import cv2
import numpy as np 
import time
import laserFindPoints as cpt
import findLines as fl
import transformToPoints as tr
from calibration import calibrator
import pattern as pt

cap = cv2.VideoCapture(0)
cap.set(3,240)
cap.set(4,320)
projecting = False
s = 115
a = 97
q = 113
c = 99
b = 98
pat = pt.Pattern()
while(True):
	ret, img = cap.read()
	cv2.imshow("img", img)
	if projecting:
	
		thresh, grayscale = cpt.threshImage(img)
		#points, pointsList = fl.createGrid(thresh)
		#lines, currMatrix = tr.transform(pointsList, points, pat)
		#points = fl.createGrid(thresh)
		cv2.imshow("img", img)
		cv2.imshow("thresh", thresh)
		#cv2.imshow("grayscale", grayscale)

		#cv2.imshow("points", points)
		#cv2.imshow("connected", connectedPoints)
		#cv2.imshow("lines", lines)

		k = cv2.waitKey(1)
		if k == s:

			points, pointsList = fl.createGrid(thresh)
			cl = calibrator()
			cl.calibrate(pointsList)
			pat = pt.Pattern()
			cv2.imwrite("calibrated.jpg", points)

		if k == c:

			print("got C")
			points, pointsList = fl.createGrid(thresh)
			pat.getDepth(pointsList)
			cv2.imwrite("newGrid.jpg", points)

	k = cv2.waitKey(1)
	if k == a:
		print("got A")
		projecting = not projecting

	if k == q:
		break

'''print("TAKING ONE WITH NO LASER")
for i in range(0,35):
	if(i%5 == 0):
		print(5-i/5)
	ret,img2 = cap.read()
	cv2.imshow("img", img2)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

	time.sleep(0.02)
ret,img2 = cap.read()

print("TAKING ONE WITH LASER")

for i in range(0,35):
	if(i%5 == 0):
		print(5-i/5)
	ret,img1 = cap.read()
	cv2.imshow("img", img1)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	time.sleep(0.02)
ret,img1 = cap.read()

img = cv2.subtract(img1,img2)

thresh, grayscale = cpt.threshImage(img)
points, connectedPoints = fl.createGrid(thresh)

cv2.imshow("thresh", thresh)
cv2.imshow("grayscale", grayscale)

cv2.imshow("points", points)
cv2.imshow("connected", connectedPoints)
cv2.waitKey()'''