import cv2
import numpy as np
from extractor import thresh,threshNormal

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

	print("in threshImages")
	height,width,channels = img.shape
			
	grayscale = np.zeros((height,width), np.uint8)
	#print(grayscale[0][0], grayscale[0][1])
	#edged = np.zeros((height,width, 3), np.uint8)
	#np.copyto(grayscale, img)
	#np.copyto(edged, img)
	for i in range(0, height):
		for j in range(0, width):
			
			b,g,r = img[i,j]
			#mid = b/3+g/3+r/3
			'''if g>=r+20 and g>=b+20:
				grayscale.itemset((i,j,0),g)
			else: 
				grayscale.itemset((i,j,0),0) '''
	
<<<<<<< HEAD
			grayscale.itemset((i,j,0),g)
	print(grayscale[0][0])
	print(type(grayscale))
	grayscale = cv2.add(grayscale, np.array([-20.0]))
	print(grayscale[0][0])
	print(type(grayscale))
=======
			grayscale.itemset((i,j),g)
	#print(grayscale[0][0])
	#print(type(grayscale))
	grayscale = cv2.add(grayscale, np.array([.0]))
	#print(grayscale[0][0])
	#print(type(grayscale))
>>>>>>> 368cd359e6caa6c660371930d4c6a6daade392e9

	#thresh1 = threshNormal(grayscale, 50)
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