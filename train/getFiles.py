import os
import cv2
import numpy as np

def cut(name):

    save = "/home/nikifaets/code/pointsProcessing/negative_samples/pics"
    img = cv2.imread("/home/nikifaets/code/pointsProcessing/train/cut/neg/"+path, 1)
    roi_h = 35
    roi_w = 35

    h,w,c = img.shape
    print("kur")
    count = 0
    for i in range(0, h, roi_h):
        for j in range(0,w, roi_w):

            print("kur")
            roi = img[i:i+roi_h, j:j+roi_w]
            cv2.imwrite(save+"/model"+path+str(count)+".jpg", roi)
            count+=1


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


path = "/home/nikifaets/code/pointsProcessing/negative_samples/"
path_save = path+"scaled/"

end_h = 640
end_w = 480
files = findfiles(path+"pics")
f = open(path+"negative_samples.txt", "w")

for image in files:
    print(image)
    f.write("/home/nikifaets/code/pointsProcessing/negative_samples/pics/"+image+"\n")    
