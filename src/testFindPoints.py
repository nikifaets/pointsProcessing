from findLines import getPoints
import cv2
import numpy as np  

img = cv2.imread("demo/test.jpg", 0)
height,width = img.shape
draft = np.zeros((height,width), np.uint8)
pointsList = list()
pointsList, draft = getPoints(img,draft,width,height)
cv2.imshow("draft", draft)
cv2.imshow("img", img)
cv2.waitKey()