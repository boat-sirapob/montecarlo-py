#!/usr/local/bin/python3

import random
import math
from matplotlib import pyplot as plt

# plot random points
# check if length from center is greater than radius
# if greater, put in array of squarepoints (or increment count of outside)
# if less, put in array of circlepoints AND squarepoints (or increment count of inside)
# take ratio of points inside the circle and points in the square
# multiply by 4 = pi

xcoords = []
ycoords = []
colors = []

squarepoints = []
circlepoints = []
numsquare = 0
numcircle = 0

radius = 1

target = 100000

for i in range(target):

	x = random.uniform(-radius,radius)
	y = random.uniform(-radius,radius)

	distance = math.sqrt((x)**2 + (y)**2)
	if distance <= radius:
		circlepoints.append((x,y))
		colors.append(1)
	else:
		colors.append(0)
	squarepoints.append((x,y))
	xcoords.append(x)
	ycoords.append(y)
	
	numsquare = len(squarepoints)
	numcircle = len(circlepoints)

	picalc = 4*numcircle/numsquare

	print(picalc)

plt.scatter(xcoords,ycoords, c=colors)
plt.show()
