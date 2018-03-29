import cv2
import numpy as np


# this algorithm extracts the points from the picture - outputs a new picture where only the points are to be seen


#folderPath = "laser/"
#img  =cv2.imread(folderPath + "laser18.jpg")


#img= cv2.resize(img, None, fx = 0.55, fy = 0.55)
def increase_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    lim = 255 - value
    v[v > lim] = 255
    v[v <= lim] += value

    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img

def threshImage(img):

	
	height,width,channels = img.shape
			
	grayscale = np.zeros((height,width, 1), np.uint8)

	'''for i in range(0, height):
		for j in range(0, width):'''

	for i in np.nditer(img):
		

			h = int(i/height)
			w = i%height
			b,g,r = img[h,w]
	
			grayscale.itemset((h,w,0),(int(g)+int(b)+int(r))/3)
	
	grayscale = cv2.add(grayscale, np.array([-220.0]))
	#print(grayscale[0][0])


	#thresh1 = thresh(grayscale)
	#thresh1 = grayscale
	thresh1 = threshNormal(grayscale, 20)

	kernel = np.ones((1,1), np.uint8)
	thresh1 = cv2.erode(thresh1, kernel, 1)	
		
	return (thresh1,grayscale)
