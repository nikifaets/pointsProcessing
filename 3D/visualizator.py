import cv2
import numpy as np 
import os
from pathlib import Path
import sys
import canvas

path = Path(os.getcwd()).parent
path = str(path)+"/src"
sys.path.append(path)

import roiSelector as rs 
import findLines as fs 
import rotatePoints as rp
from PointNode import PointNode
import getDepth as gd

cal = cv2.imread("calibrated_1.jpg", 0)
new = cv2.imread("sixPoint.jpg", 0)
h,w = cal.shape
foundPoints_cal = np.zeros(cal.shape, np.uint8)
foundPoints_new = np.zeros(cal.shape, np.uint8)

ret, cal = cv2.threshold(cal, 100,255, cv2.THRESH_BINARY)
ret, new = cv2.threshold(new, 100,255, cv2.THRESH_BINARY)

pointsList_cal = fs.getPoints(cal, cal.shape[1], cal.shape[0])
pointsList_new = fs.getPoints(new, new.shape[1], new.shape[0])

for p in pointsList_cal:
	cv2.circle(foundPoints_cal, (int(p.x), int(p.y)), 3, 200, -1)

for p in pointsList_new:
	cv2.circle(foundPoints_new, (int(p.x), int(p.y)), 3, 200, -1)

mid = PointNode(cal.shape[1]/2, cal.shape[0]/2)
deg = -40


pairs = gd.getPointsPairs(pointsList_cal, pointsList_new, 30)
print(pairs, "sdf")

for pair in pairs:

	print(len(pair))
	print(pair)
	p_n, line = pair

	print(p_n)
	for p_c in line:

		cv2.line(foundPoints_cal, (int(p_n.x), int(p_n.y)), (int(p_c.x), int(p_c.y)), 200, 2)




#cv2.imshow("cal", cal_lines)
#cv2.imshow("new", new_lines)
cv2.imshow("found_c", foundPoints_cal)
cv2.imshow("found_n", foundPoints_new)
cv2.waitKey()
#canvas.createScene(pointsList_n)
 
