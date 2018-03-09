import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
cap.set(3,240)
cap.set(4,320)

casc = cv2.CascadeClassifier("haar_new_s15/cascade.xml")

path = "annotations1/scaled/laser32.jpg"

while(True):

	ret,img = cap.read()
	print(ret)

	#img = cv2.cvtColor()
	points = casc.detectMultiScale(img)

	for(x, y, h, w) in points:
	        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

	cv2.imshow("img", img)
	cv2.waitKey()

