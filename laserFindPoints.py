import cv2
import numpy as np
from extractor import thresh

# this algorithm extracts the points from the picture - outputs a new picture where only the points are to be seen


#folderPath = "laser/"
#img  =cv2.imread(folderPath + "laser18.jpg")


#img= cv2.resize(img, None, fx = 0.55, fy = 0.55)


def threshImage(img):

	height,width,channels = img.shape
			
	grayscale = np.zeros((height,width, 1), np.uint8)

	#edged = np.zeros((height,width, 3), np.uint8)
	#np.copyto(grayscale, img)
	#np.copyto(edged, img)
	for i in range(0, height):
		for j in range(0, width):
			
			b,g,r = img[i,j]
			'''mid = b/3+g/3+r/3
			if g>0.5*mid and b<0.5*mid and r<0.5*mid:
				grayscale.itemset((i,j,0),255)
			else: 
				grayscale.itemset((i,j,0),0)  '''
			
			grayscale.itemset((i,j,0),g)


	thresh1 = thresh(grayscale)
	#canny = cv2.Canny(thresh1, 150,250)
		
		#cv2.imshow("edge"+str(im), edged)
	return (thresh1,grayscale)
	#cv2.imwrite("edged19.jpg", thresh1)


"""
for i in range(0, len(img)):
	img[i] = cv2.resize(img[i], None, fx=0.5, fy=0.5)
	cv2.imshow("resizing", img[i])

cv2.imshow("kur", img[0])
cv2.waitKey()
"""