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
	for i in range(4):
		fd (turtle, 150)
		lt (turtle)


#   ------------------------------
#	Function: generalized_square()
#	------------------------------ 
def generalized_square (turtle, n):
	for i in range(4):
		fd (turtle, n)
		lt (turtle)


# 	-------------------
#	Function: polygon()
#	-------------------
def polygon (turtle, n_sides, n_length):
	for i in range (n_sides):
		fd (turtle, n_length)
		lt (turtle, 360/n_sides)


#	-------------------
# 	Function: circle ()
#	-------------------
def circle (turtle, r):
	polygon (turtle, 360, 2*math.pi*r/360) 


#	---------------
#	Function: arc()
#	---------------
def arc (turtle, r, angle):
	for i in range (angle):
		fd (turtle, 2*math.pi*r/360)
		lt (turtle, 1)

	
#	-----------------------------------
#	Very general function: go_turtle ()
#	-----------------------------------
def go_turtle (turtle, n_segments, l_segment, direction_change):
	for i in range (n_segments):
		fd (turtle, l_segment)
		lt (turtle, direction_change)


#	-----------------------
#	Function: new_polygon() 
#	-----------------------
def new_polygon(turtle, n_sides, length):
	go_turtle (turtle, n_sides, length, 360/n_sides)


#	---------------------
#	Function: new_cicle()
#	---------------------
def new_circle (turtle, r):
	go_turtle (turtle, 360, 2*math.pi*r/360, 1)


#	-------------------
#	Function: new_arc()
#	-------------------
def new_arc(turtle, r, angle):
	go_turtle (turtle, angle, 2*math.pi*r/360, 1)



# ******************
# ** Main Program **
# ******************
length = 30
sides = 3
radius = 100
theta = 5

square (bob)
world.clear()

generalized_square (bob, length)
world.clear()

polygon (bob, sides, length)
world.clear()

bk (bob, radius)			# draws radius
rt (bob)				# positions bob facing down
circle(bob, radius)
lt (bob)				# points bob towards origin
fd (bob, radius) 			# moves bob to origin
world.clear()

rt (bob, theta)		# turns bob to starting theta
bk (bob, radius)			# draws radius
rt (bob)				# positions bob facing down
arc (bob, radius, theta)	
lt (bob)				# points bob towards origin
fd (bob, radius)			# moves bob to origin
world.clear()

new_polygon (bob, sides, length)
world.clear()

bk (bob, radius)			# draws radius
rt (bob)				# positions bob facing down
new_circle(bob, radius)
lt (bob)				# points bob towards origin
fd (bob, radius) 			# moves bob to origin
world.clear()

rt (bob, theta)		# turns bob to starting theta
bk (bob, radius)			# draws radius
rt (bob)				# positions bob facing down
new_arc (bob, radius, theta)	
lt (bob)				# points bob towards origin
fd (bob, radius)			# moves bob to origin
world.clear()



print "Radius = ", radius
print "Circumference =", 2*math.pi*radius


wait_for_user()					
