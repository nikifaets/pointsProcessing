import cv2
import numpy as np 

casc = cv2.CascadeClassifier("hog_s10/cascade.xml")

cap = cv2.VideoCapture(0)

tracking = False
tracker = list()
points = list()

while(True):

	

	ret, img = cap.read()
	detected = np.zeros((480,640,1), np.uint8)
	
	img = cv2.blur(img,(3,3) )

	if not tracking:
		points = casc.detectMultiScale(img)

		for(x, y, h, w) in points:
			cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
			detected[int(y+h/2)][int(x+w/2)] = 255

	if tracking:

		for tr in tracker:

			ret,sqr = tr.update(img)
			p1 = (int(sqr[0]), int(sqr[1]))
			p2 = (int(sqr[0] + sqr[2]), int(sqr[1] + sqr[3]))
			cv2.rectangle(img, p1, p2, 255, 2,1)

			x = int(sqr[1]+sqr[3]/2)
			y = int(sqr[0]+sqr[2]/2)
			if y < 480 and x < 640:

				detected[y][x] = 255


	cv2.imshow("points", detected)
	cv2.imshow("img", img)
	k = cv2.waitKey(1)

	if k == ord('a') and not tracking:

		tracking = True
		for p in points:

			tr = cv2.TrackerTLD_create()

			tr.init(img, (p[0], p[1], p[2], p[3]))
			tracker.append(tr)

	if k == ord('q'):
		break


