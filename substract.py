import cv2
import numpy as np  

cap = cv2.VideoCapture(-1)
cap.set(3,640)
cap.set(4,480)
cap.set(16, -2)
print(cap.get(16))
global img1
global img2
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #print(ret)

    

    # Display the resulting frame
    cv2.imshow('frame',frame)
    k = cv2.waitKey(30)
    if k == 115:
    	img1 = frame
    if k == 97:
    	img2 = frame
    if k ==113:
    	break
# When everything done, release the capture
cap.release()

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
sub = cv2.subtract(img2, img1)
cv2.imshow("subtracted", sub)
cv2.waitKey()
#cv2.imwrite("laser/laser38.jpg",sub)
cv2.destroyAllWindows()