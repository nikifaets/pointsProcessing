import cv2
import numpy as np

folderPath = "test/"
img  =cv2.imread(folderPath + "testCal.jpg")

img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
cv2.imshow("grayscale", cimg)
cv2.waitKey(0)

circles = cv2.HoughCircles(cimg,cv2.HOUGH_GRADIENT,1,2,
                                    param1=50,param2=30,minRadius=0)
print("KUR")
print(type(circles))
print (circles)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
  # draw the outer circle
  cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
  # draw the center of the circle
  cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)

'''height,width,channels = img.shape
    
grayscale = np.zeros((height,width, 1), np.uint8)
original = np.zeros((height,width, 1), np.uint8)


for i in range(0, height):
  for j in range(0, width):
    b,g,r = img[i,j]
    grayscale[i,j] = g   


#img = cv2.GaussianBlur(grayscale, (3,3) ,3)
img = cv2.medianBlur(grayscale, 3)

cv2.imshow("img", img)
cv2.waitKey()
grad = cv2.Canny(grayscale,100,200)
cv2.imshow("gradients", grad)
cv2.waitKey()
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                                    param1=50,param2=30,minRadius=0,maxRadius=0)
print (circles)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
  # draw the outer circle
  cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
  # draw the center of the circle
  cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()'''