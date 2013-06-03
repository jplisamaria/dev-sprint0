# Flower excercise (4.2) from Week 0

# Name:Lisa-Maria Mehta


import math
from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

def arc (turtle, r, arc_angle):
	"""Draws an arc with given radius and arc angle
	using the same number of line segments as the angle
	measurement in degrees"""
	n_sides = arc_angle				
	segment_length = 2*math.pi*r/360
	turn_angle = 1
	for i in range (n_sides):
		fd (turtle, segment_length)
		lt (turtle, turn_angle)

def petal (turtle, r, arc_angle):
	"""Draws a petal by drawing an arc of radius r, then 
	drawing a mirror-image arc back to the beginning or the 
	first arc, and turns to its original position."""
	turn_angle = 180 - arc_angle

	arc (turtle,r, arc_angle)
	lt (bob, turn_angle)
	arc (turtle, r, arc_angle)
	lt (bob, turn_angle)

def flower (turtle, r, n, angle):
	"""Draws a flower by drawing n petals (made of arcs of 
	radius r and angle arc_angle)
	n: number of petals
	r: radius of petal arc
	angle = angle of petal arc"""
	for i in range (n):
		arc_angle = angle
		turn_angle = 360/n  	# angle turtle turns between petals 

		petal (turtle, r, arc_angle)
		lt (turtle, turn_angle)

def move_turtle (turtle, n):
	"""Moves turtle for starting position for drawing flower.
	n: number of steps"""
	pu (bob)
	fd (bob, n)
	pd (bob)


# ******************
# ** Main Porgram **
# ******************

bob.delay = 0.001

#	------------
#	First Flower
#	------------
radius = 500
arc_theta = 10
n_petals = 30

move_turtle (bob, -100)
flower (bob, radius, n_petals, arc_theta)

#	-------------
#	Second Flower
#	-------------
radius = 70
arc_theta = 72
n_petals = 5

move_turtle (bob, 200)
flower (bob, radius, n_petals, arc_theta)

#	------------
#	Third Flower
#	------------
radius = 40	
arc_theta = 115			
n_petals = 18

move_turtle (bob, 200)
flower (bob, radius, n_petals, arc_theta)

#	----------------------
#	Get bob out of the way
#	----------------------
pu (bob)
bk (bob, 150)
rt (bob)
fd (bob, 100)


wait_for_user()					

