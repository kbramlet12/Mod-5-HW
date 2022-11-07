#===============================================================================
#Program Name: Second Turtle
# Your Name: Keegan Bramlet
# Date: Novemeber 6, 2022
# Program Purpose: Create the Olympic Ring Design
#===============================================================================
import turtle
wn = turtle.Screen()

olympics = turtle.Turtle()
olympics.pensize(5)
 
olympics.color("blue")
olympics.penup()
olympics.goto(-110, -25)
olympics.pendown()
olympics.circle(45)
 
olympics.color("black")
olympics.penup()
olympics.goto(0, -25)
olympics.pendown()
olympics.circle(45)
 
olympics.color("red")
olympics.penup()
olympics.goto(110, -25)
olympics.pendown()
olympics.circle(45)
 
olympics.color("yellow")
olympics.penup()
olympics.goto(-55, -75)
olympics.pendown()
olympics.circle(45)
 
olympics.color("green")
olympics.penup()
olympics.goto(55, -75)
olympics.pendown()
olympics.circle(45)

wn.exitonclick()
