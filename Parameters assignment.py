#Derrick Hernandez
#9/20/2024

#Init
import turtle
import random
derrick = turtle.Turtle()
turtle.colormode(255)
#Functions
def drawTriangle(size,color):
    for i in range(3):
        derrick.forward(size)
        derrick.left(120)
        derrick.pencolor(color,random.randint(0,255),random.randint(0,255))
def polygon(sides,size,color,width):
    for i in range(sides):
        derrick.forward(size)
        derrick.left(360/sides)
        derrick.pencolor(color,random.randint(0,255),random.randint(0,255))
        derrick.width(width)
#Main
for i in range(random.randint(1,2137)):
    polygon(random.randint(3,10),random.randint(1,300),random.randint(0,255),random.randint(1,30))

