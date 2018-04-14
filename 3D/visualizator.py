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

cal = cv2.imread("calibrated.jpg", 0)
new = cv2.imread("point26.jpg", 0)
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


pairs = gd.getPointsPairs(pointsList_cal, pointsList_new, 3)

points3d_c = list()
points3d_n = list()

for pair in pairs:

	p_n, line = pair
	for p_c in line:

		pc, pn = gd.calculateDepth(p_c, p_n)
		points3d_c.append(pc)
		points3d_n.append(pn)
		cv2.line(foundPoints_cal, (int(p_n.x), int(p_n.y)), (int(p_c.x), int(p_c.y)), 200, 1)
		cv2.circle(foundPoints_cal, (int(p_n.x), int(p_n.y)), 7, 200, -1)



#cv2.imshow("cal", cal_lines)
#cv2.imshow("new", new_lines)
cv2.imshow("found_c", foundPoints_cal)
cv2.imshow("found_n", foundPoints_new)
cv2.imshow("cal", cal)
cv2.waitKey()
canvas.createScene(points3d_n)
gd.writeVertices("calibrated.obj", points3d_c)
gd.writeVertices("model.obj", points3d_n)
 
