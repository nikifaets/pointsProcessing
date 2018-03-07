import cv2
import numpy as np 

casc = cv2.CascadeClassifier("haar_2/cascade.xml")

path = "annotations/scaled/laser19.jpg"
img = cv2.imread(path)
#img = cv2.cvtColor()
points = casc.detectMultiScale(img)

for(x, y, h, w) in points:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow("img", img)
cv2.waitKey()

