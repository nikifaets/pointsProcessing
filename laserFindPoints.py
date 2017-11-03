import cv2
import numpy as np

# this algorithm extracts the points from the picture - outputs a new picture where only the points are to be seen

folderPath = "laser/"
img  = [cv2.imread(folderPath + "laser4.jpg"), cv2.imread(folderPath + "laser5.jpg"), cv2.imread(folderPath + "laser32.jpg")]

for i in range(2, len(img)):
	img[i] = cv2.resize(img[i], None, fx = 0.35, fy = 0.35)

for im in range(2, len(img)):

	cv2.imshow("col" + str(im), img[im])

	height,width,channels = img[im].shape
		
	grayscale = np.zeros((height,width, 3), np.uint8)
	edged = np.zeros((height,width, 3), np.uint8)
	np.copyto(grayscale, img[im])
	np.copyto(edged, img[im])
	for i in range(0, height):
		for j in range(0, width):
			b,g,r = img[im][i,j]
			grayscale[i,j] = g,g,g    
			cv2.imshow(str(im), grayscale)
			mid = int(g)+int(b)+int(r)
			if(g - mid/3 > 15):
				edged[i,j] = 255

			else:
				edged[i,j] = 0


	ret,thresh1 = cv2.threshold(grayscale,50,255,cv2.THRESH_BINARY)
	canny = cv2.Canny(thresh1, 150,250)
	
	#cv2.imshow("edge"+str(im), edged)
	cv2.imshow("thresh", thresh1)
	cv2.imshow("canny" + str(im), canny)
	cv2.imwrite("edged12.jpg", thresh1)
	cv2.waitKey()

"""
for i in range(0, len(img)):
	img[i] = cv2.resize(img[i], None, fx=0.5, fy=0.5)
	cv2.imshow("resizing", img[i])

cv2.imshow("kur", img[0])
cv2.waitKey()
"""