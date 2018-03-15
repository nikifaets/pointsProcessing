import cv2
import numpy as np 
import sys

path = sys.argv[1]
save = "/home/nikifaets/code/pointsProcessing/negative_samples/pics"
img = cv2.imread("neg/"+path+".jpg", 1)
roi_h = 70
roi_w = 70

h,w,c = img.shape
print("kur")
count = 0
for i in range(0, h, roi_h):
	for j in range(0,w, roi_w):

		print("kur")
		roi = img[i:i+roi_h, j:j+roi_w]
		cv2.imwrite(save+"/model"+path+str(count)+".jpg", roi)
		count+=1
