import cv2
import numpy as np  

cam = 1
ret = False

while(not ret):

	cap = cv2.VideoCapture(cam)
	ret,img = cap.read()
	img = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV)
	print("trying ", ret)



num = 60
while(True):

	ret, img = cap.read()
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret,img = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)

	if ret:

		cv2.imshow("img", img)

		k = cv2.waitKey(1)
		if k == ord("s"):
			cv2.imwrite("sample" + str(num)+".jpg", img)
			print("IMAGE TAKEN")
			num+=1

		if k == ord("q"):
			break
