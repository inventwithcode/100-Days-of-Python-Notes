from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(15)
def move_backward():
    tim.backward(15)
def rotate_clockwise():
    tim.right(10)
def rotate_anticlockwise():
    tim.left(10)
def clear_screen():
    tim.reset()

screen.listen()

# NOTE function names are used without parenthesis
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "d", fun = rotate_clockwise)
screen.onkey(key = "a", fun = rotate_anticlockwise)
screen.onkey(key = "c", fun = clear_screen)

screen.exitonclick()