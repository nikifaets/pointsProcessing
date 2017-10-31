import cv2
import numpy as np 
import math
from Point import Point
from Line import Line

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

def connect(pointsByX, pointsByY):
	matchByY(pointsByY)
	matchByX(pointsByX)

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

				if(currDist < bestDist):
					if(bestYdiff == -1 or math.fabs(point.y - currPoint.y) < 1.5*bestYdiff):
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

				if(currDist < bestDist):
					if(bestXdiff == -1 or math.fabs(point.x - currPoint.x) < 1.5*bestXdiff):
						better = True

					if(better):
						bestXdiff = math.fabs(point.x - currPoint.x)
						bestDist = currDist
						bestPoint = currPoint

		if(bestPoint != nullPoint):
			point.upcenter = bestPoint
			bestPoint.downcenter = point
	



