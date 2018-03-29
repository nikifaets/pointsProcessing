import cv2
import numpy as np  

cam = 0
ret = False

while(not ret):

	cap = cv2.VideoCapture(cam)
	ret,img = cap.read()
	print("trying ", ret)



num = 60
while(True):

	ret, img = cap.read()

	if ret:

		cv2.imshow("img", img)

		k = cv2.waitKey(1)
		if k == ord("s"):
			cv2.imwrite("sample" + str(num)+".jpg", img)
			print("IMAGE TAKEN")
			num+=1

		if k == ord("q"):
			break
