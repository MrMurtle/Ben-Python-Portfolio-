#Derrick Hernandez
#9/20/2024
#parameters
#A variable (container) that customizes a function(AKA the value inside the parenthesis)

#Init
import turtle
import random
dah = turtle.Turtle()

#Functions
def square(size,color):     #Step 1: Create  the Parameter
    for i in range(4):
        dah.forward(size) #Step 2: Use you parameter inside you function
        dah.left(90)
        dah.color(color)
        dah.begin_fill()
        dah.fillcolor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        dah.end_fill()
#Main
dah.speed(500)
for i in range(random.randint(1,198324791287398127937812983791287)):
    square(random.randint(1,100000),"red") #Step 2: Supply and argument(value) to all of your calls
    dah.speed(random.randint(1,1231231231))
