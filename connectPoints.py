import cv2
import numpy as np 
import math
from Point import Point
from Line import Line
from PointNode import PointNode
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
		return -1
	'''for i in resTemp:
		print(i[0])
	cv2.waitKey()'''
	return res

def angleBetweenLines(p1, p2, origin):

	d1 = 0
	alpha1 = 0

	if p1.x == origin.x:
		d = p1.x
	else:
		tg = -(p1.y-origin.y)/(p1.x-origin.x)
		alpha1 = math.atan(tg)
		d = p1.x*math.cos(alpha1) + p1.y*math.sin(alpha1)

	d2 = 0
	alpha2 = 0

	if p2.x == origin.x:
		d = p2.x
	else:
		tg = -(p2.y-origin.y)/(p2.x-origin.x)
		alpha2 = math.atan(tg)
		d2 = p2.x*math.cos(alpha2) + p2.y*math.sin(alpha2)

	return math.degrees(alpha1-alpha2)

def makeConnection(point, list):

	pointsByY = sorted(list, key = lambda point: point.y, reverse = False)
	pointsByX = sorted(list, key = lambda point: point.x, reverse = False)

	#we are looking for the closest 2 points, which lie together on the same line as the current point
	closest = list[0]
	best = PointNode(point.x,point.y)
	second = PointNode(point.x,point.y)
	secondBest = PointNode(point.x, point.y)
	bestf = False
	secondf = False
	secondBestf = False
	#print("PPOOIINNTT: ", point.x, point.y)
	for curr in list:
		point.write(curr,32)
		'''if curr != closest:

			
			print("curr: ", curr.x, curr.y)
			print("dist: ", dist(point,curr))
			print("angle between curr, point and closest: ", angleBetweenLines(curr, closest, point))
			if math.fabs(angleBetweenLines(curr,closest,point)) <=30 and not bestf:
				best = curr
				bestf = True

			if math.fabs(math.fabs(angleBetweenLines(curr, closest, point))-90)<=15:
				second = curr
				secondf = True

			if math.fabs(angleBetweenLines(curr, second, point)) <=20 and secondf:
				secondBest = curr
				break

	 
	if secondBest == Point(0,0) or second == Point(0,0) or best == Point(0,0):
		print("kur ")

	#point.upcenter = (closest,32)
	point.write(closest,32)
	#closest.write(point,32)
	#point.write(best,32)
	#best.write(point,32)
	#closest.downcenter = (point,32)
	#point.right = (best,32)
	#best.left = (point,32)

	#point.write(second,32)
	#point.write(secondBest, 32)
	#second.write(point,32)
	#secondBest.write(point,32)
	#point.downcenter = (second,32)
	#second.upcenter = (point,32)
	#point.left = (secondBest,32)
	#secondBest.right = (point,32)'''



def connect(list):

	for i in range(0, len(list)):

		sortedNeighbours = findNeighbours(list[i], list)
		if sortedNeighbours == -1:
			return -1
		makeConnection(list[i], sortedNeighbours)
		


