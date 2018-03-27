import math
from PointNode import PointNode

def transfrom_degrees(angle, point):

	if point.x<0 and point.y > 0:
		angle = 180-angle

	if point.x<0 and point.y < 0:
		angle = 180+math.fabs(angle)

	if point.x>0 and point.y<0:
		angle+=360

	return angle
	
def rotatePoints(pointsList, center, deg):

	cx = center.x
	cy = center.y

	for p in pointsList:

		px = p.x-cx
		py = p.y-cy
		dist = math.sqrt(px*px + py*py)

		
		alpha = math.degrees(math.asin(py/dist))
		alpha = transfrom_degrees(alpha, PointNode(px,py))

		angle_new = math.radians(alpha+deg)

		y_rot = math.sin(angle_new)*dist+cy
		x_rot = math.cos(angle_new)*dist+cx

		p.x = int(x_rot)
		p.y = int(y_rot)
	
