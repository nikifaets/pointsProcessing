import cv2
import numpy as np 
import laserFindPoints as cpt
import findLines as fl
from calibration import calibrator
from PointNode import PointNode


def getDepth(pointsList_c, pointsList_n):

	coords = list()
	pairs = list()
	readp = open("pars.txt","r")
	L = float(readp.readline())
	d = float(readp.readline())
	kx = float(readp.readline())
	ky = float(readp.readline())
	prop = float(readp.readline())
	readp.close()

	print("lengths ", len(pointsList_c), len(pointsList_n))
	if len(pointsList_n) == len(pointsList_c):

		print("!!!!!!!!!!!1",0)
		pairs = getPairs(pointsList_c, pointsList_n, 0)
		
		

	else:

		print("!!!!!!!!!!!!!!!11,1",1)
		pairs = getPairs(pointsList_c, pointsList_n,1)
		

	for i in pairs:

			
		calP = i[0]
		newP = i[1]

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




def getPairs(pointsList_c, pointsList_n, diff):

	#0 for the same length of lists
	if diff == 0:
		pairs = list()

		for i in range(0, len(pointsList_c)):

			pairs.append((pointsList_c[i], pointsList_n[i]))

		return pairs

	else:

		#find points from each image with the same y coordinate
		pairs = list()
		
		for i in range(0, len(pointsList_c)):

			local_c = list()
			local_n = list()

			p = pointsList_c[i]
			y = p.y
			local_c.append(p)

			if i < len(pointsList_c)-1:
				while(pointsList_c[i+1].y == y):

					i+=1
					local_c.append(pointsList_c[i])

				for j in range(0, len(pointsList_n)):

					p_n = pointsList_n[j]
					if p_n.y == y:
						local_n.append(p_n)

			#------------ compare the collected points with the same y coordinate

			if len(local_c) == len(local_n):

				for pair in range(0, len(local_c)):

					pairs.append((local_c[pair], local_n[pair]))

		return pairs







def writeVertices( file, coords):

		f = open(file, "w+")
		for point in coords:
			x,y,z = point
			vert = "v "+str(x) + " " + str(y) + " " + str(z) + "\n"
			f.write(vert)

calPath = "test/testCal5.jpg"
newPath = "test/testNew5.jpg"


cal = cv2.imread(calPath, 0)
new = cv2.imread(newPath,0)

h_c, w_c = cal.shape
h_n, w_n = new.shape

pointsList_n, new = fl.getPoints(new, w_n, h_n)
pointsList_c, cal = fl.getPoints(cal, w_c, h_c)
cv2.imshow("new_p", new)
cv2.imshow("cal_p", cal)

points_c = np.zeros((h_c, w_c, 1), np.uint8)
points_n = np.zeros((h_c, w_c, 1), np.uint8)
pointsList_c = list()
pointsList_n = list()

counter = 0
for h in range(0, h_c):
	for w in range(0, w_c):
		if cal[h][w] > 100:
			pointsList_c.append(PointNode(w,h))
			points_c[h][w] = 255
			counter+=1

		if new[h][w] > 100:
			pointsList_n.append(PointNode(w,h))
			points_n[h][w] = 255


#cv2.imshow("thresh", thresh)
#cv2.imshow("grayscale", grayscale)

cv2.imshow("points", points_c)
cv2.imshow("cal", cal)
#cv2.imshow("newthresh", thresh1)
#cv2.imshow("grayscalenew", grayscale1)
cv2.imshow("new", new)
cv2.imshow("newpoints", points_n)
cv2.waitKey()

sortedCal = sorted(pointsList_c, key = lambda point: point.y, reverse = False)
sortedNew = sorted(pointsList_n, key = lambda point: point.y, reverse = False)

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
getDepth(pointsList_c, pointsList_n)

for i in pointsList_c:
	print(i.X, i.Y, i.Z)

print("----------------------------------------------------")

for i in pointsList_n:
	print(i.X, i.Y, i.Z)

print(counter)
cv2.waitKey()