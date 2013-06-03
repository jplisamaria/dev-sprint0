# Polygon excercise from Week 0

# Name: Lisa-Maria Mehta


from TurtleWorld import * 	
import math	
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

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
	bk (turtle, r)			# draws radius
	rt (turtle)				# positions turtle facing down
	polygon (turtle, 360, 2*math.pi*r/360) 




# ******************
# ** Main Program **
# ******************
length = 30
sides = 3
radius = 100

#square (bob)
#world.clear()
#generalized_square (bob, length)
#world.clear()
#polygon (bob, sides, length)
#world.clear()
circle(bob, radius)

print "Radius = ", radius
print "Circumference =", 2*math.pi*radius


wait_for_user()					
