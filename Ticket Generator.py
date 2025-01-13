#Name:
#Date:

#Initialize
import turtle
import time
t = turtle.Turtle()

#Functions
import turtle
import random
pen = turtle.Turtle()
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
#Draws an admission ticket with a label and customer information inside. This function uses a turtle to draw a ticket with the name of the customer and the price paid for the ticket.
#(string: name) represents the customers name that appears inside the ticket
#(integer: price) represents the price the customer paid that appears inside the ticket
#(string: dayofweek) represents the day of the week that the ticket was purchased
#(integer: y_location) y_location represents the vertical loction of the ticket
def draw_ticket(name, price, dayofweek, y_location):
    umbrella()
    t.goto(-50, y_location)
    t.write("Ticket", font=("Arial", 15), align="right")
    t.pendown()
    for i in range(2):
        t.forward(500)
        t.left(90)
        t.forward(250)
        t.left(90)
    t.penup()
    t.goto(50, y_location +215)
    t.write("Admit One", font=("Arial", 15), align="right")
    t.goto(440, y_location +215)
    t.write(dayofweek, font=("Arial", 15), align="right")
    t.goto(225, y_location +135)
    t.write(name, font=("Arial", 15), align="right")
    t.goto(225, y_location +15)
    t.write(price, font=("Arial", 15), align="right")
def price_check():
    price = 100
    print("Welcome to the Eminem ticket shop!")
    name = input("What is your first and last name?")
    time.sleep(2)
    age = int(input("How old are you?"))
    time.sleep(2)
    day = input("What day of the week are you planning on visting?")
    time.sleep(2)
    coupon = input("Enter a coupon if you have one!")
    if name == "Ben":#Checks if your name is BEN
        price = 1000000
        draw_ticket(str(name),price,str(day),0)
    elif age <= 3:#Checks for little kids
        price = 0
        draw_ticket(str(name),price,str(day),0)
    elif age >=18:#Checks for old people
        price = 100
        draw_ticket(str(name),price,str(day),0)#Checks for teens on a weekday
    elif age >3 and age < 18 and day == "Monday" or day =="monday" or day =="Tuesday"or day =="tuesday"or day =="Wednesday"or day =="wednesday"or day =="Thursday"or day =="thursday"or day =="Friday"or day =="friday":
        if coupon == "FREEFRIDAY" and day == "Friday"or day =="friday":#Checks for coupon
            price = 0
            draw_ticket(str(name),price,str(day),0)
        else:
            price = 50#If invalid coupon
            draw_ticket(str(name),price,str(day),0)
    elif age > 3 and age < 18 and day == "sunday" or day== "Sunday" or day == "Saturday" or day== "saturday":#Teens on a weekend
        if coupon == "SUNDAY10" and day== "sunday" or day== "Sunday":
            price = price - 10
            draw_ticket(str(name),price,str(day),0)
        else:#If invalid coupon
            price = 100
            draw_ticket(str(name),price,str(day),0)
    else:
        print("sorry I dont understand")
        price_check()

#Main
#1.Introduction
#2.Collect the pertinent information
    #name
    #age
    #Day
    #Coupon
#3. Write Algorythm for determining price
price_check()
