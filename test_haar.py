import cv2
import numpy as np 

casc = cv2.CascadeClassifier("haar_new_s20/cascade.xml")

cap = cv2.VideoCapture(0)
'''path = "annotations/scaled/2017-11-09-214806.jpg"
img = cv2.imread(path)
points = casc.detectMultiScale(img)

for(x, y, h, w) in points:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("img", img)
cv2.waitKey()'''


#img = cv2.cvtColor()

while(True):

	ret, img = cap.read()
	points = casc.detectMultiScale(img)

	for(x, y, h, w) in points:
		cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

	cv2.imshow("img", img)
	k = cv2.waitKey(1)
	if k == ord('q'):
		break


