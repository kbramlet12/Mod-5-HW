#===============================================================================
#Program Name: First Turtle
# Your Name: Keegan Bramlet
# Date: Novemeber 6, 2022
# Program Purpose: Create a polygon using Turtle given specifications
#===============================================================================
import turtle
wn = turtle.Screen()
wn.bgcolor(input("What is the fill color of your Polygon? "))

polly = turtle.Turtle()
polly.color(input("What is the Line color of your Polygon? "))
polly.pensize(5)

number_of_angles = int(input("How many sides does your polygon have? "))
side_length = int(input("How long is each side? "))
n = number_of_angles
angle = 360 / n

for i in range(0, n):
        polly.forward(side_length)
        polly.left(angle)

wn.exitonclick()

 
