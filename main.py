import cv2
import numpy as np 
import time
import laserFindPoints as cpt
import findLines as fl

cap = cv2.VideoCapture(0)
cap.set(3,320)
cap.set(4,240)
while(True):

	ret, img = cap.read()
	thresh, grayscale = cpt.threshImage(img)
	points, connectedPoints = fl.createGrid(thresh)
	#points = fl.createGrid(thresh)
	cv2.imshow("img", img)
	cv2.imshow("thresh", thresh)
	cv2.imshow("grayscale", grayscale)

	cv2.imshow("points", points)
	cv2.imshow("connected", connectedPoints)
	if cv2.waitKey(1) & 0xFF == ord('q'):
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