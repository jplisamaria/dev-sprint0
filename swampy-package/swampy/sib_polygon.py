# Polygon excercise from Week 0

# Name: Lisa-Maria Mehta


from TurtleWorld import * 	
import math	
world = TurtleWorld()			
bob = Turtle()				


#	-------------------
#	Function: square ()
#	------------------- 
def square (turtle):
	"""Draws a square with a length of 150."""
	for i in range(4):
		fd (turtle, 150)
		lt (turtle)


#	------------------------------
#	Function: generalized_square()
#	------------------------------ 
def generalized_square (turtle, n):
	"""Draws a square with length n."""
	for i in range(4):
		fd (turtle, n)
		lt (turtle)


# 	-------------------
#	Function: polygon()
#	-------------------
def polygon (turtle, n, length):
	"""Draws a polygon with
	n: number of sides
	length: length of each side"""
	turn_angle = 360/n
	for i in range (n):
		fd (turtle, length)
		lt (turtle, turn_angle)


#	-------------------
# 	Function: circle ()
#	-------------------
def circle (turtle, r):
	"""Draws a circle with radius r, using 360 sides"""
	n = 360
	segment_length = 2*math.pi*r/360
	polygon (turtle, n, segment_length) 


#	---------------
#	Function: arc()
#	---------------
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

	
#	-----------------------------------
#	Very general function: poly_draw ()
#	-----------------------------------
def poly_draw (turtle, n, length, angle):
	"""Draws a figure with connected segment and equal angles
	n: number of n_segments
	length: length of n_segments
	angle: angle of turtle direction change between segments"""
	for i in range (n):
		fd (turtle, length)
		lt (turtle, angle)


#	-----------------------
#	Function: new_polygon() 
#	-----------------------
def new_polygon(turtle, n, length):
	"""Draws a polygon using poly_draw()
	n: number of sides
	length: length of each side"""
	angle = 360/n 			# correct angle to draw polygon
	poly_draw (turtle, n, length, angle)


#	---------------------
#	Function: new_cicle()
#	---------------------
def new_circle (turtle, r):
	"""Draws a circle of radius r using 360 line segments.
	Calls poly_draw()."""
	n = 360					
	segment_length = 2*math.pi*r/360
	turn_angle = 1 	
	poly_draw (turtle, n, segment_length, turn_angle)


#	-------------------
#	Function: new_arc()
#	-------------------
def new_arc(turtle, r, arc_angle):
	"""Draws an arc with given radius and arc angle
	using the same number of line segments as the angle
	measurement in degrees.  Calls on poly_draw()."""
	n_sides = arc_angle				
	segment_length = 2*math.pi*r/360
	turn_angle = 1
	poly_draw (turtle, n_sides, segment_length, turn_angle)


#	********************************************************************
#	--------------------------------------------------------------------
#	The following set of functions move the turtle before or after
#	calling the circle and arc functions.  The ready_to_draw() functions 
#	draw radius lines and position the turtle for drawing the figures. 
#	The return_to_origin() function return the turtle to the origin
#	and to it's starting angle.
#	--------------------------------------------------------------------
#	
def ready_to_draw_circle (turtle,r):
	"""Draws radius and positions turtle to draw circle."""
	turtle.delay =0.01
	bk (turtle, radius)			# draws radius
	rt (turtle)					# positions turtle facing down

def ready_to_draw_arc (turtle, r, angle):
	"""Draws radius and positions turtle to draw arc."""
	turtle.delay = 0.1
	rt (turtle, angle)			# turns turtle to starting angle
	bk (turtle, r)				# draws radius
	rt (turtle)					# positions turtle facing down

def return_to_origin (turtle, r):
	"""Draws radius back towards origin and positions
	turtle for new instructions."""
	lt (turtle)					# points turtle towards origin
	fd (turtle, r)				# moves turtle to origin
#	
#	********************************************************************



# ******************
# ** Main Program **
# ******************
length = 75
sides = 8
radius = 100
theta = 60

square (bob)
world.clear()

generalized_square (bob, length)
world.clear()

polygon (bob, sides, length)
world.clear()

ready_to_draw_circle(bob, radius)				
circle(bob, radius)
return_to_origin(bob, radius)
world.clear()

ready_to_draw_arc (bob, radius, theta)
arc (bob, radius, theta)	
return_to_origin(bob, radius)
world.clear()

new_polygon (bob, sides, length)
world.clear()

ready_to_draw_circle(bob, radius)				
new_circle(bob, radius)
return_to_origin(bob, radius)
world.clear()

ready_to_draw_arc (bob, radius, theta)
new_arc (bob, radius, theta)	
return_to_origin(bob, radius)

print "Radius = ", radius
print "Circumference =", 2*math.pi*radius

wait_for_user()					
