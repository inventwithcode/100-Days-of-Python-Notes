from turtle import Turtle, Screen
from os import system as console

timmy = Turtle()
my_screen = Screen()


timmy.shape("turtle")
timmy.color("black", "DarkGreen")
my_screen.bgcolor("DarkGrey")
timmy.speed(1)
timmy.width(5)
print(timmy.position())
# timmy movements
timmy.forward(100)
print(timmy.position())

# Program exits on click
my_screen.exitonclick()
console('clear')