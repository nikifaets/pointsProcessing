import cv2
import numpy as np 
import laserFindPoints as cpt
import findLines as fl
from calibration import calibrator


def getDepth(pointsList, pointsList1):

	coords = list()
	readp = open("pars.txt","r")
	L = float(readp.readline())
	d = float(readp.readline())
	kx = float(readp.readline())
	ky = float(readp.readline())
	prop = float(readp.readline())
	readp.close()

	print("lengths ", len(pointsList), len(pointsList1))
	if len(pointsList) == len(pointsList1):

		for i in range(len(pointsList)):

			
			calP = pointsList[i]
			newP = pointsList1[i]

			kx = prop*newP.x
			ky  = prop*newP.y

			print("CALCULATING DEPTH FOR CAL POINT ", calP.x, calP.y, "AND NEW POINT ", newP.x, newP.y)
			print("L = ", L, "kx = ", kx, "d = ",d)

			

			X0 = calP.X
			Y0 = calP.Y
			Z0 = calP.Z
			#print(X0, Y0, Z0)
			#print(type(X0))
			X = X0*(d/(X0+L*kx))
			Y = Y0*(d/(X0+L*kx))
			Z = L*(d/(X0+L*kx))
			Z1 = d/(d-L*prop*(calP.x - newP.x))
			

			newP.setCalibratedCoords((X, Y, Z))
			coords.append((X,Y,Z))

	writeVertices("3D_1.obj", coords)

def writeVertices( file, coords):

		f = open(file, "w+")
		for point in coords:
			x,y,z = point
			vert = "v "+str(x) + " " + str(y) + " " + str(z) + "\n"
			f.write(vert)

calPath = "test/testCal4.jpg"
newPath = "test/testNew4.jpg"

'''cap = cv2.VideoCapture(1)
cap.set(3,240)
cap.set(4,320)

a = 97
b = 98
c = 99
d = 100
while(True):

	ret, img = cap.read()
	cv2.imshow("img", img)

	k = cv2.waitKey(1)

	if k == a:
		cv2.imwrite(calPath, img)

	if k == b:
		cv2.imwrite(newPath, img)

	if k == d:
		break'''
		

cal = cv2.imread(calPath, 1)
new = cv2.imread(newPath,1)
thresh, grayscale = cpt.threshImage(cal)
points, pointsList = fl.createGrid(thresh)
thresh1, grayscale1 = cpt.threshImage(new)
points1, pointsList1 = fl.createGrid(thresh1)

cv2.imshow("thresh", thresh)
cv2.imshow("grayscale", grayscale)
cv2.imshow("points", points)
cv2.imshow("newthresh", thresh1)
cv2.imshow("grayscalenew", grayscale1)
cv2.imshow("newpoints", points1)

sortedCal = sorted(pointsList, key = lambda point: point.y, reverse = False)
sortedNew = sorted(pointsList1, key = lambda point: point.y, reverse = False)

longer = max(len(sortedNew), len(sortedCal))

for i in range(0, longer):
	
	if len(sortedCal) > i:
		print(sortedCal[i].y, sortedCal[i].x, end = " ")

	if len(sortedNew) > i:
		print(sortedNew[i].y, sortedNew[i].x, end = "")
		sortedNew[i].x = 160-sortedNew[i].x
		sortedNew[i].y = 120-sortedNew[i].y

	print("")

print("----------------------------------------------------")

print(len(sortedCal), len(sortedNew))

cal = calibrator()
print(type(cal))
cal.calibrate(sortedCal)
getDepth(pointsList, pointsList1)

for i in pointsList:
	print(i.X, i.Y, i.Z)

print("----------------------------------------------------")

for i in pointsList1:
	print(i.X, i.Y, i.Z)

cv2.waitKey()