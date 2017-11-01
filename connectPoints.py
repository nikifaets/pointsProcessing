import cv2
import numpy as np 
import math
from Point import Point
from Line import Line
import heapq

#the connection of the points happens here - input is an image with the extracted points - output is a list of lines

def sort(array):
    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0].y
        for x in array:
            if x.y < pivot:
                less.append(x)
            if x.y == pivot:
                equal.append(x)
            if x.y > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


def dist(a, b):

	return math.sqrt(math.pow(a.x-b.x, 2) + math.pow(a.y-b.y, 2))

def findNeighbours(point, list):

	best = []
	#bestDist = 9999
	#heapq.heappush(best, (999, PointNode(0,0)))
	for i in range(0, len(list)):
		neigh = list[i] 
		if(neigh != point):
			currDist = dist(point,neigh)

			heapq.heappush(best, (currDist, i))
		
	best.sort()			
	resTemp = best[:8]
	res = [list[i[1]] for i in resTemp]
	if(len(res) < 8):
		print("ooopa")
	'''for i in resTemp:
		print(i[0])
	cv2.waitKey()'''
	return res

def makeConnection(point, list):

	pointsByY = sorted(list, key = lambda point: point.y, reverse = False)
	pointsByX = sorted(list, key = lambda point: point.x, reverse = False)

	
	

	#search the four points to the right for minimal y difference
	bestXmatch = point
	bestYdiff = 999
	for i in range (0, 4):
		currDiff = math.fabs(point.y - pointsByX[i].y)
		if(currDiff < bestYdiff):
			bestYdiff = currDiff
			bestXmatch = pointsByX[i]

	point.right = bestXmatch
	bestXmatch.left = point

	#search the four points above for minimal x difference
	bestYmatch = point
	bestXdiff = 999
	for i in range (0, 4):
		currDiff = math.fabs(point.x - pointsByY[i].x)
		if(currDiff < bestXdiff):
			bestXdiff = currDiff
			bestYmatch = pointsByY[i]

	point.upcenter = bestYmatch
	bestXmatch.left = point



def connect(list):

	for i in range(0, len(list)):

		sortedNeighbours = findNeighbours(list[i], list)
		makeConnection(list[i], sortedNeighbours)
		

		

def matchByY(points):

	for i in range(0, len(points)):
		
		point = points[i]
		searchRange = 5
		if(i<searchRange):
			begin = 0
		else:
			begin = i-searchRange

		if(i+searchRange >= len(points)):
			end = len(points)-1
		else:
			end = i+searchRange

		bestDist = 99999
		nullPoint = Point(0,0)
		bestPoint = nullPoint
		bestYdiff = -1

		for j in range(begin, end):

			if (j != i and points[j].x > point.x):

				currPoint = points[j]
				currDist = dist(point, currPoint)
				better = False
				currDiff = math.fabs(currPoint.y - point.y)

				if(currDiff < bestYdiff):
					better = True

				if(better):
					bestYdiff = math.fabs(point.y - currPoint.y)
					bestDist = currDist
					bestPoint = currPoint
		if(bestPoint != nullPoint):
			point.right = bestPoint
			bestPoint.left = point
	


def matchByX(points):

	for i in range(0, len(points)):
		
		point = points[i]
		searchRange = 5
		if(i<searchRange):
			begin = 0
		else:
			begin = i-searchRange

		if(i+searchRange >= len(points)):
			end = len(points)-1
		else:
			end = i+searchRange

		bestDist = 99999
		nullPoint = Point(0,0)
		bestPoint = nullPoint
		bestXdiff = -1

		for j in range(begin, end):

			if (j != i and points[j].y > point.y):

				currPoint = points[j]
				currDist = dist(point, currPoint)
				better = False
				currDiff = math.fabs(point.x - currPoint.x)

				if(currDiff < bestXdiff):
					better = True

				if(better):
					bestXdiff = math.fabs(currDiff)
					bestDist = currDist
					bestPoint = currPoint

		#if(bestPoint != nullPoint):
		#	point.upcenter = bestPoint
		#	bestPoint.downcenter = point
	



