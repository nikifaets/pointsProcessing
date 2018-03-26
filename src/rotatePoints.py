import math

def rotatePoints(pointsList, center, deg):

	cx = center.x
	cy = center.y

	for p in pointsList:

		px = p.x
		py = p.y
		dist = math.sqrt((px-cx)*(px-cx) + (py-cy)*(py-cy))


		alpha = math.deg(asin(py/dist))
		angle_new = rad(alpha+deg)
		y_rot = sin(angle_new)/dist
		x_rot = cos(angle_new)/dist

		p.x = int(x_rot)
		p.y = int(y_rot)

