import cv2
import numpy as np


img1 = cv2.imread("/home/nikifaets/code/laser/laser5.jpg")
img = cv2.resize(img1, (0,0), fx=0.1, fy=0.1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,100,200,apertureSize = 3)

#cv2.imshow("cannyEdge", edges)
#cv2.waitKey()

lines = cv2.HoughLines(edges,1,np.pi/180,1)
print(len(lines))
for rho,theta in lines[0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imshow("canny", edges)
cv2.imshow("img", img)
cv2.waitKey()