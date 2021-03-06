# Hello excercise from Week 0

# Name:Lisa-Maria


from TurtleWorld import * 		
world = TurtleWorld()			
bob = Turtle()				



# This is where you put code to move bob

# ****************
# ** Exercise 1 **
# ****************
#	Swampy HELLO
#	------------
world.clear()
bob = Turtle()

#	------------------
# 	Movement Functions
# 	------------------

def fwd_lft (turtle, n):
	fd (turtle, n)
	lt (turtle)

def fwd_rt (turtle, n):
	fd (turtle, n)
	rt (turtle)

def backwd_lft (turtle, n):
	bk (turtle, n)
	lt (turtle)

def backwd_rt (turtle, n):
	bk (turtle, n)
	rt (turtle)

def white_space (turtle, space):
	pu (turtle)
	fwd_lft (turtle, space)

def start (turtle, st_position):
	pu (turtle)
	bk (turtle, st_position)
	lt (turtle)


#	---------------------------
#	Individual Letter Functions
#	---------------------------
def H (turtle, ht, wd):
	pd (turtle)
	fd (turtle, ht)
	backwd_rt (turtle, ht*0.5)
	fwd_lft (turtle, wd)
	fd (turtle, ht*0.5)
	backwd_rt (turtle, ht)

def E (turtle, ht, wd):
	pd (turtle)
	fwd_rt (turtle, ht)
	fd (turtle, wd)
	backwd_rt (turtle, wd)
	fwd_lft (turtle, ht*0.5)
	fd (turtle, wd*0.6)
	backwd_rt (turtle,wd*0.6)
	fwd_lft (turtle, ht*0.5)
	fd (turtle, wd)

def L (turtle, ht, wd):
	fd (bob, ht)
	pd (bob)
	backwd_rt (bob, ht)
	fd (bob, wd)

def boxy_O (turtle, ht, wd):
	pd (bob)
	fwd_rt (bob, ht)
	fwd_rt (bob, wd)
	fwd_rt (bob, ht)
	fd (bob, wd)

# -----------------
# Setting variables
# -----------------
ht = 100
wd = 35
space = 20

# ------------
# Main Program
#-------------
start (bob, 150)
H(bob, ht, wd)
white_space (bob, space)
E(bob, ht, wd)
white_space (bob, space)
L(bob, ht, wd)
white_space (bob, space)
L (bob, ht, wd)
white_space (bob, space)
boxy_O (bob, ht, wd)
pu (bob)
fwd_lft (bob, ht)
fd (bob, wd)




wait_for_user()					
