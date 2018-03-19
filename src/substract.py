import cv2
import numpy as np  

def bgr2gr(img):

	height,width,channels = img1.shape
	grayscale = np.zeros((height,width,1), np.uint8)
	for i in range(0, height):
		for j in range(0, width):
			b,g,r = img[i,j]
			grayscale[i,j] = g  
	return grayscale


img1 = cv2.imread("doc/cantseepoints1.jpg",1)
img2 = cv2.imread("doc/nopoints1.jpg",1)

img1 = bgr2gr(img1)
img2 = bgr2gr(img2)


cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
sub = cv2.subtract(img1, img2)
cv2.imshow("subtracted", sub)
cv2.imwrite("doc/subtracted.jpg", sub)
cv2.waitKey()
#cv2.imwrite("laser/laser38.jpg",sub)
cv2.destroyAllWindows()