import cv2
import numpy as np 
from pathlib import Path  
import os

path = Path(os.getcwd())
path = str(path.parent)
casc = cv2.CascadeClassifier(path+"/hog_s10/cascade.xml")

points = list()

def test_camera():

	cap = cv2.VideoCapture(0)

	while(True):

		

		ret, img = cap.read()
		detected = np.zeros((480,640,1), np.uint8)
		
		img = cv2.blur(img,(3,3) )

		if not tracking:
			points = casc.detectMultiScale(img)

			for(x, y, h, w) in points:
				cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
				detected[int(y+h/2)][int(x+w/2)] = 255


		cv2.imshow("points", detected)
		cv2.imshow("img", img)
		k = cv2.waitKey(1)

		if k == ord('q'):
			break

def test_pic():

	print(os.getcwd())
	img =  cv2.imread(os.getcwd()+"/sample60.jpg",0)
	detected = np.zeros((img.shape[0], img.shape[1],0))

	if img is not None:

		points = casc.detectMultiScale(img)

		for(x, y, h, w) in points:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
			detected[int(y+h/2)][int(x+w/2)] = 255


		cv2.imshow("points", detected)
		cv2.imshow("img", img)


test_pic()



