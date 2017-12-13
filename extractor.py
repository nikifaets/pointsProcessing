import cv2
import numpy as np 

def thresh(img):
	height,width,channels = img.shape
	step = 5
	w = int(width/step)
	h = int(height/step)
	#blur = cv2.GaussianBlur(img,(3,3),1)
	#blur = cv2.medianBlur(img, 3)
	#ret3,th3 = cv2.threshold(img,120,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	th1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY_INV,3,9)
	'''th2 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY_INV,3,9)'''

	'''cv2.imshow("th1", th1)
	cv2.imshow("th2", th2)
	cv2.imshow("th3", th3)
	cv2.imshow("blur", blur)'''

	return th1

'''folderPath = "laser/"
img  =cv2.imread(folderPath + "laser34.jpg")
img = cv2.resize(img, None, fx = 0.35, fy = 0.35)

height,width,channels = img.shape
		
grayscale = np.zeros((height,width, 1), np.uint8)
original = np.zeros((height,width, 1), np.uint8)


for i in range(0, height):
	for j in range(0, width):
		b,g,r = img[i,j]
		grayscale[i,j] = g   

np.copyto(original, grayscale)
roi = thresh(grayscale)
#cv2.imshow("thresh", roi)

median = cv2.medianBlur(roi,3)
gaus = cv2.GaussianBlur(roi, (3,3),2)
cv2.imshow("median", median)
cv2.imshow("original_grayed", original)
cv2.imshow("gaussian", gaus)
#cv2.imshow("original", img)
#cv2.imwrite("edged28.jpg", roi)
cv2.waitKey()'''
