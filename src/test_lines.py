import findLines as fl 
import cv2
import numpy as np
from calibration import calibrator 
import rotatePoints as rp
from PointNode import PointNode

cal = calibrator()


angle_rot = -39
img = cv2.imread("newGrid.jpg", 0)
h,w = img.shape
detected = np.zeros((h,w,1), np.uint8)
lines_img = np.zeros((h,w,1), np.uint8)


pointsList = fl.getPoints(img, w, h)
rp.rotatePoints(pointsList, PointNode(w/2,h/2), angle_rot)

for p in pointsList:

	cv2.circle(detected, (int(p.x), int(p.y)), 4, 200, -1)

lines = fl.collectLines(pointsList)
lines = fl.fixLines(lines)
for line in lines:
	line.draw(lines_img)


cv2.imshow("lines", lines_img)
cv2.imshow("detected", detected)
cv2.waitKey()
