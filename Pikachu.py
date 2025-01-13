#09-11-12
#Danny Garcia
#Derrick Hernandez
#pikachu

#Inuit
import turtle
d = turtle.Turtle()

#functions
def pikachu():
#head
    for i in range (8):
        d.forward(15)
        d.right(1)
    d.backward(10)
#ear
    d.left(80)
    for i in range (30):
        d.forward(10)
        d.right(1)
    d.right(135)
    for i in range (30):
        d.forward(10)
        d.right(1)
    for i in range (20):
        d.left(1)
        d.backward(10)
#line in ear
    d.right(140)
    for i in range (6):
        d.forward(10)
        d.left(5)
    for i in range (6):
        d.right(5)
        d.backward(10)
    d.left(140)
    for i in range(20):
        d.forward(10)
        d.right(1)
#side of face
    d.left(60)
    for i in range(3):
        d.backward(5)
        d.left(7)
    for i in range(3):
        d.right(7)
        d.forward(5)
    for i in range(3):
        d.forward(10)
        d.right(10)
    d.left(3)
    for i in range(8):
        d.forward(8)
        d.left(1)
    for i in range(10):
        d.forward(6)
        d.left(2)
    for i in range (12):
        d.forward(5)
        d.right(3)
    for i in range (8):
        d.forward(20)
        d.right(10)
#face cheek
    for i in range(6):
        d.left(10)
        d.backward(20)
    d.right(50)
    for i in range(11):
        d.forward(18)
        d.right(20)
#face eye
    d.penup()
    d.right(180)
    d.forward(100)
    d.pendown()
    d.dot(60)
    d.forward(10)
    d.color("#FFFFFF")
    d.dot(35)
#face nose
    d.color("#000000")
    d.left(55)
    d.penup()
    d.forward(125)
    d.pendown()
    d.dot(5)
#face mouth
    d.left(65)
    d.penup()
    d.forward(20)
    d.left(75)
    d.pendown()
    for i in range(10):
        d.forward(5)
        d.left(1)
    for i in range(6):
       d.forward(5)
       d.left(7)
    for i in range(3):
        d.right(7)
        d.backward(5)
    d.right(100)
    for i in range(16):
        d.forward(10)
        d.right(5)
    for i in range(14):
        d.left(5)
        d.backward(10)
    d.right(100)
    for i in range(14):
        d.forward(5)
        d.left(1)
    d.penup()
    d.goto(0,0)
    d.pendown()



#LEFT SIDE
    d.right(4.5)
#head
    for i in range (8):
        d.forward(15)
        d.left(1)
    d.backward(10)
    d.backward(10)
#ear
    d.right(80)
    for i in range (30):
        d.forward(10)
        d.left(1)
    d.left(135)
    for i in range (30):
        d.forward(10)
        d.left(1)
    for i in range (20):
        d.right(1)
        d.backward(10)
#line in ear
    d.left(140)
    for i in range (6):
        d.forward(10)
        d.right(5)
    for i in range (6):
        d.left(5)
        d.backward(10)
    d.right(140)
    for i in range(20):
        d.forward(10)
        d.left(1)
#side of face
    d.right(60)
    for i in range(3):
        d.backward(5)
        d.right(7)
    for i in range(3):
        d.left(7)
        d.forward(5)
    for i in range(3):
        d.forward(10)
        d.left(10)
    d.right(3)
    for i in range(8):
        d.forward(8)
        d.right(1)
    for i in range(10):
        d.forward(6)
        d.right(2)
    for i in range (12):
        d.forward(5)
        d.left(3)
    for i in range (8):
        d.forward(20)
        d.left(10)
#face cheek
    for i in range(6):
        d.right(10)
        d.backward(20)
    d.left(50)
    for i in range(11):
        d.forward(18)
        d.left(20)
#face eye
    d.penup()
    d.left(180)
    d.forward(100)
    d.pendown()
    d.dot(60)
    d.forward(10)
    d.color("#FFFFFF")
    d.dot(35)
#face nose
    d.color("#000000")
    d.right(55)
    d.penup()
    d.forward(125)
    d.pendown()
    d.dot(5)
#face mouth
    d.right(65)
    d.penup()
    d.forward(20)
    d.right(75)
    d.pendown()
    for i in range(10):
        d.forward(5)
        d.right(1)
    for i in range(6):
       d.forward(5)
       d.right(7)
    for i in range(3):
        d.left(7)
        d.backward(5)
    d.left(100)
    for i in range(16):
        d.forward(10)
        d.left(5)
    for i in range(14):
        d.right(5)
        d.backward(10)
    d.left(100)
    for i in range(14):
        d.forward(5)
        d.right(1)
    d.penup()
    d.goto(0,0)
    d.pendown()


#Main
pikachu()



