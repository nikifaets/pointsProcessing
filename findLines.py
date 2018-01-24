
import cv2
import numpy as np 
import math
from connectPoints import connect 
from connectPoints import sort
from Point import Point
from PointNode import PointNode
import queue

def getPoints(img, draft, width, height):

	
	pointsList = list()
	mem = np.zeros((height, width), np.bool)

	for i in range(0, width):
		for j in range(0, height):

			#print("kur ", img[j][i]>100, mem[j][i] == False)
			if(img[j][i] > 100 and not mem[j,i]):
				
				maxw = (i,j)
				minw = (i,j)
				maxh = (i,j)
				minh = (i,j)
				#search white in the neighbours in a sideXside rectangle
				heap = queue.Queue()
				heap.put((i,j))
				length = 1
				while heap.qsize() > 0:
					curr = heap.get()
					#print("POINT ", curr[1],curr[0], img[j][i])
					side = 4
					for h in range(curr[1]-side, curr[1]+side):
						for w in range(curr[0]-side, curr[0]+side):
							if not (h==j and w==i):
								#print(h,w)
								if w >= width:
									w = width-1
								if w<0:
									w = 0
								if h >= height:
									h = height-1
								if h<0:
									h = 0
								
								#print(h,w)
								if(mem[h][w] == False):
									mem[h][w] = True
									if img[h][w] > 100:
										heap.put((w,h))
										length+=1
										#print("pushed", h, w)
										if h > maxh[1]:
											maxh = (w,h)
										if h < minh[1]:
											minh = (w,h)
										if w > maxw[0]:
											maxw = (w,h)
										if w < minw[0]:
											minw = (w,h)

				midh = int((maxh[1] + minh[1])/2)
				midw = int((maxw[0] + minw[0])/2)
				print(length, midh, midw)

				minSize = 1
				if (maxh[0] != 0 and minh[0] != 9999 and minw[0] != 9999 and maxw[0] != 0) and length>=minSize:
					
					'''draft[maxh[1],maxh[0]]=200
					draft[minh[1],minh[0]]=200
					draft[maxw[1],maxw[0]]=200
					draft[minw[1],minw[0]]=200'''
					print("writing")
					pointsList.append(PointNode(midw,midh))
					draft[midh][midw] = 255
									

	return (pointsList,draft)
# the main file for the moment - the connected lines are processed here
#img = cv2.imread("demo/edged6.jpg", 0)
#img = cv2.imread("laser/demo.jpg", 0)
#width,height = img.shape

def drawLines(lines, width, height):

	connectedLines = np.zeros((height, width), dtype = np.uint8)
	minlen = 999
	maxlen = 0
	counter = 0
	summ = 0
	for i in lines:
		x1 = i.start.x
		y1 = i.start.y

		x2 = i.end.x
		y2 = i.end.y
	

		cv2.line(connectedLines, (y1,x1), (y2,x2), 100, 1)

		#if(i.length==999):
		#	cv2.line(connectedLines, (x1,y1), (x2,y2), 250, 2)
		

	return connectedLines

def collectLines(points):
	lines = list()
	for i in points:
		received = i.convertToLine()
		lines.extend(received)

	return lines

def createGrid(img):
	#cv2.imshow("img", img)

	height,width = img.shape
	

	#points = np.zeros((width,height), np.uint8)
	pointsList = list()
	nodesList = list()
	draft = np.zeros((height,width), np.uint8)

	pointsList,draft = getPoints(img, draft, width, height)

	'''ret = connect(pointsList)
	if ret == -1:
		return (draft, draft,[PointNode(0,0)])
	lines = list()
	lines = collectLines(pointsList)
	showLines = drawLines(lines, width, height)'''

	#return (draft, showLines, pointsList)

	return draft,pointsList


def test(img):
	draft,showLines = createGrid(img)
	cv2.imshow("draft", draft)
	cv2.imshow("showLines", showLines)
	cv2.waitKey()


'''img = cv2.imread("demo/edged24.jpg",0)
test(img)'''