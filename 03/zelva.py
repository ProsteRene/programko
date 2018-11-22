from turtle import forward, left,right, exitonclick,color
from random import choice

colors = ["gold", "red", "blue", "pink", "green","purple"]

for x in range(10000000):
	color(choice(colors))
	forward(x / 100)
	left(10)
	
exitonclick()