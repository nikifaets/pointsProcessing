import os
import cv2
import numpy as np
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
    f.write("/home/nikifaets/code/poinsProcessing/negative_samples/pics/"+image+"\n")    
