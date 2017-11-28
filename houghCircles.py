import cv2
import numpy as np


folderPath = "laser/"
img  =cv2.imread(folderPath + "demo.jpg")
img = cv2.resize(img, None, fx = 0.35, fy = 0.35)

height,width,channels = img.shape
    
grayscale = np.zeros((height,width, 1), np.uint8)
original = np.zeros((height,width, 1), np.uint8)


for i in range(0, height):
  for j in range(0, width):
    b,g,r = img[i,j]
    grayscale[i,j] = g   


img = cv2.medianBlur(grayscale,5)
cv2.imshow("img", img)
cv2.waitKey()
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1.2, 5)
print(circles)
#circles = np.uint16(np.around(circles))
for i in circles[0,:]:
  # draw the outer circle
  cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
  # draw the center of the circle
  cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()