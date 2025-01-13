#Derrick Hernandez
#Digital Scene Pt 2
#nightsky() by Joseph Ortega
#umbrela() by Noah Killoren
#draw_all_trees() by Sadie L
#init
import turtle
sadie=turtle.Turtle()

#function
def drawTree(size,color,x,y):
    sadie.begin_fill()
    sadie.penup()
    sadie.goto(x,y)
    sadie.pendown()
    sadie.color(color)

    for i in range (3):
        sadie.forward(size)
        sadie.left(120)
    sadie.end_fill()
def drawStump(color):
    sadie.begin_fill()
    sadie.penup()
    sadie.forward(90)
    sadie.right(90)
    sadie.pendown()
    sadie.forward(60)
    sadie.right(90)
    sadie.forward(20)
    sadie.right(90)
    sadie.forward(60)
    sadie.color(color)
    sadie.end_fill()
def draw_all_trees():
    drawTree(70,"Green",-350,40)
    drawTree(120,"Green",-375,-30)
    drawTree(170,"Green",-400,-100)
#init
turtle=turtle.Turtle()
turtle.dot(9999,"#4ee3ed")
#function
def umbrellaRed(color): #This is the red piece of the umbrella. The 'color' parameter creates the color of the section.
    turtle.color(color)
    turtle.penup()
    turtle.goto(-390,20)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(-180,70)
    turtle.right(130)
    turtle.circle(170,40)
    turtle.right(93)
    turtle.circle(710,10)
    turtle.left(170)
    turtle.penup()#This is setting up to make the orange piece.
    turtle.circle(710,10)
    turtle.pendown()
    turtle.end_fill()

def umbrellaOrange(color): #This is the orange piece of the umbrella. The 'color' parameter creates the color of the section.
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(-215,30)
    turtle.left(97)
    turtle.circle(320,20)
    turtle.left(65)
    turtle.circle(207,25)
    turtle.left(50)
    turtle.circle(170,40)
    turtle.end_fill()
    turtle.left(90)
    turtle.penup()#This is setting up to make the yellow piece.
    turtle.circle(-321,20)
    turtle.pendown()

def umbrellaYellow(color):#This is the yellow piece. The 'color' parameter creates the color of the section.
    turtle.color(color) 
    turtle.begin_fill()
    turtle.circle(696,10)
    turtle.left(100)
    turtle.circle(152,70)
    turtle.left(115)
    turtle.circle(-185,35)
    turtle.end_fill()
    

def stick(): #This function draws the white stick of the umbrella.
    turtle.penup()    
    turtle.goto(-150,-120)
    turtle.right(155)
    turtle.pensize(7)
    turtle.color("white")
    turtle.pendown()
    turtle.forward(220)
    
def umbrella(): #This function puts the elements of the umbrella hood together to draw the umbrella. I finally input the colors of my umbrella here.
    umbrellaRed("#fc9099")
    umbrellaOrange("#ffb675")
    umbrellaYellow("#ffe866")
    stick()
#init
import turtle
import random
pen = turtle.Turtle()
#Functions #Makes the moon and and dark sky background.
#functions
def night():
    pen.dot(10000, "#52497a")
    pen.dot(265, "white")
    pen.dot(260, "#eeecf9")
    pen.penup()
    pen.left(90)
    pen.forward(300)
    pen.pendown()
    pen.right(90)
    pen.color("white")
    pen.speed(100000)

#Makes a single star in the background
def stars():
    pen.begin_fill()
    for i in range(5):
        pen.left(72)
        pen.forward(5)
        pen.right(144)
        pen.forward(5)
    pen.end_fill()

#Puts both previous functions together, and makes the star function make a lot of stars in a limited range location. Customizable amount of stars.

def nightsky(numberofstars):
    night()
    for i in range(numberofstars):
        pen.penup()
        pen.goto(random.randint(-430,430),random.randint(150,400))
        pen.pendown()
        stars()

#Main
nightsky(40)
#The amount of stars can be changed through the use of the nightsky() parameter.
umbrella()
draw_all_trees()
drawStump("Brown")
