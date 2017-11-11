import cv2
import numpy as np 

def thresh(img):
	height,width,channels = img.shape
	step = 5
	w = int(width/step)
	h = int(height/step)
	#print("img",width,height)
	#print("roi",w,h)
	for i in range(0,step):
		for j in range(0,step):
			#i = height
			#j = width
			x1 = w*j
			y1 = h*i
			x2 = x1+w
			y2 = y1+h
			#print("a(", x1,y1,"), ", "b( ", x2,y2,")") 
			roi = img[y1:y2+1,x1:x2+1]
			roi_h, roi_w, roi_channels = roi.shape
			#print("roi shape", roi_h, roi_w)
			
			max_dens = 0
			mid_dens = 0
			counter = 0
			for he in range(roi_h):
				for wi in range(roi_w):
					g = roi[he,wi]
					mid_dens = mid_dens+int(g)
					#print("mid_dens, j",mid_dens, j)
					counter+=1
					if g > max_dens:
						max_dens = g
			print(mid_dens,counter)
			mid_dens = mid_dens/counter
			print(mid_dens)
			for he in range(roi_h):
				for wi in range(roi_w):
					g = roi[he,wi]
					if g > 2*mid_dens and max_dens>30:
						roi[he][wi] = 250
					else:
						roi[he][wi] = 0

			print(max_dens)
			#cv2.rectangle(roi, (0,0), (roi_w, roi_h), 120, 1)
			#cv2.putText(roi, str(max_dens), (0,roi_h-10), cv2.FONT_HERSHEY_SIMPLEX, fontScale = 0.3, color = 255, thickness = 1)

	return img

folderPath = "laser/"
img  =cv2.imread(folderPath + "laser36.jpg")
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
cv2.imshow("thresh", roi)
cv2.imshow("original_grayed", original)
cv2.imshow("original", img)
#cv2.imwrite("edged19.jpg", thresh1)
cv2.waitKey()
