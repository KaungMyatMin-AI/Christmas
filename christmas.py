from turtle import *
from shape import *
from random import randint
import time

speed(7)
turtle.title("Merry Christmas")
window = turtle.Screen()
window.bgcolor("#D4D4D4")
y = -100
width = 240

#Moon
draw_circle(turtle, "white", 249, 255, 45)
draw_circle(turtle, "#D4D4D4", 229, 255, 47)

#Snowman
draw_circle(turtle, "#F5F5F5", 200, -210, 56)
draw_circle(turtle, "#F5F5F5", 200, -110, 32)
draw_circle(turtle, "black", 210, -74, 4)
draw_circle(turtle, "black", 180, -74, 4)

#Snowwomen
draw_circle(turtle, "#F5F5F5", 290, -210, 46)
draw_circle(turtle, "#F5F5F5", 290, -130, 27)
draw_circle(turtle, "black", 297, -96, 3)
draw_circle(turtle, "black", 276, -96, 3)

#Tree
draw_rectangle(turtle, "brown", -15, y - 40, 30, 40)
while width > 20:
    width = width - randint(20,30)
    height = randint(15, 35)
    x = 0 - width / 2
    draw_rectangle(turtle, "green", x, y, width, height)
    y = y + height
draw_star(turtle, "yellow", 4, y, 20)

#Test
penup()
color("red")
goto(-175, -205)
write("Merry Christmas", move=True, font=("Comic Sans MS", 29, "bold"))

#Stars
draw_star(turtle, "white",-130,200,8)
draw_star(turtle, "white",-120,185,7)
draw_star(turtle, "white",-160,170,5)
draw_star(turtle, "white",-150,130,6)
draw_star(turtle, "white",-88,150,10)

time.sleep(9)
hideturtle()
