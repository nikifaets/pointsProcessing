import cv2
import numpy as np 

casc = cv2.CascadeClassifier("src/haar_new_s10/cascade.xml")

cap = cv2.VideoCapture(0)

points = list()


img = cv2.imread("laser/laser34.jpg")
#img = cv2.resize(img,(480,640))

h,w,c = img.shape
detected = np.zeros((h,w,1), np.uint8)

#img = cv2.blur(img,(3,3) )

points = casc.detectMultiScale(img)

for(x, y, h, w) in points:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
	detected[int(y+h/2)][int(x+w/2)] = 255


cv2.imshow("points", detected)
cv2.imshow("img", img)
k = cv2.waitKey(0)


