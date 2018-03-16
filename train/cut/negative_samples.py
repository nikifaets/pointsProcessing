import cv2
import numpy as np 
import sys
import os

def findfiles(directory):
    objects = os.listdir(directory)  # find all objects in a dir

    files = []
    for i in objects:  # check if very object in the folder ...
        if isFile(directory + i):  # ... is a file.
            files.append(i)  # if yes, append it.
    return files

def isFile(object):
    try:
        os.listdir(object)  # tries to get the objects inside of this object
        return False  # if it worked, it's a folder
    except Exception:  # if not, it's a file
        return True


path = sys.argv[1]
save = "/home/nikifaets/code/pointsProcessing/negative_samples/pics"
#img = cv2.imread("neg/"+path+".jpg", 1)
roi_h = 100
roi_w = 100

images = findfiles(path)
print(len(images))

for file in images:

	print(file)
	img = cv2.imread(path+"/"+file, 1)
	h,w,c = img.shape
	
	count = 0
	for i in range(0, h, roi_h):
		for j in range(0,w, roi_w):

			
			roi = img[i:i+roi_h, j:j+roi_w]
			cv2.imwrite(save+"/model"+file+str(count)+".jpg", roi)
			count+=1
