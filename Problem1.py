from turtle import *

squilliam = Turtle()

squilliam.color("dark green")
squilliam.pensize(5)
squilliam.speed(0)
squilliam.shape("turtle")

def drawTriangle():
	for x in range(3):
		squilliam.forward(100)
		squilliam.left(120)

drawTriangle()

mainloop()