import cv2
import numpy as np 


def vote(read):

	lines = list()
	mSpaces = 160
	mStep = 4
	mMin = -20
	mMax = 20

	nSpaces = 32
	nStep = 10
	nMin = -160
	nMax = 160

	arrayW = mSpaces+5
	arrayH = nSpaces+5

	data = np.zeros((arrayW, arrayH))

	for point in range(0, len(read)):

		x,y = read[point]

		for i in range (0, mSpaces):

			m = i/mStep + mMin
			
			n = y/10-m*(x/10)
			print("m,x,y and m for point", x,y,m,n)
			if(n>nMax):
				n = nMax
			if(n<nMin):
				n = nMin

			nBox = int(abs(n-nMin)/nStep)

			data[i,nBox]+=1

	for i in range(0, mSpaces):
		for j in range(0, nSpaces):

			if(data[i][j]>8):
				m = i/mStep + mMin
				print("m: " + str(i) + "/" + str(mStep) + "+" + str(mMin))
				n = j*10+nMin
				lines.append((n,m))
	return lines


readImg = cv2.imread("/home/nikifaets/code/laser/demo3.jpg")
img = cv2.cvtColor(readImg, cv2.COLOR_BGR2GRAY)

count = 0
diameter = 40
radius = 20
height,width = img.shape

points = list()

mem = np.zeros((width,height), np.bool)
print(mem[80][100])

for i in range(0,width):
	for j in range(0,height):

		if(mem[i][j] == False):
			gray = img[j][i]
			if(gray > 200):
				print(i,j)
				count+=1
				recX1 = i
				recY1 = j-radius
				recX2 = i+diameter
				recY2 = j+radius
				x = i/50 
				y = -j/50
				points.append((x,y))
				cv2.rectangle(readImg, (recX1, recY1), (recX2, recY2), 255, 5)
				for w in range(recX1 , recX2):
					for h in range ( recY1, recY2):
						if(w<0):
							w = 0
						if(w>=width):
							w = width-1
						if(h>=height):
							h = height-1

						
						mem[w][h] = True

				#print(i,j)
#print(count)
#print(points)
lines = vote(read = points)

for i in range(0, len(lines)):

	x1 = 0
	x2 = 600

	n,m = lines[i]
	y1 = int(m*x1 + n)
	y2 = int(m*x2 + n)
	cv2.line(readImg, (x1,y1), (x2,y2), (0,0,255), 10)

print(lines)
cv2.imshow("img", img)
cv2.imshow("original", readImg)
cv2.waitKey()



						





  
