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
new = cv2.imread("new_1.jpg", 0)

ret, cal = cv2.threshold(cal, 100,255, cv2.THRESH_BINARY)
ret, new = cv2.threshold(new, 100,255, cv2.THRESH_BINARY)

pointsList_cal = fs.getPoints(cal, cal.shape[1], cal.shape[0])
pointsList_new = fs.getPoints(new, new.shape[1], new.shape[0])


mid = PointNode(cal.shape[1]/2, cal.shape[0]/2)
deg = -13

pointsList_n, pointsList_c, cal, new = gd.getDepth(cal,new,deg)
gd.writeVertices("model.obj", pointsList_n)
gd.writeVertices("calibrated.obj", pointsList_n)


canvas.createScene(pointsList_n)
cv2.imshow("cal", cal)
cv2.imshow("new", new)
cv2.waitKey()
 
