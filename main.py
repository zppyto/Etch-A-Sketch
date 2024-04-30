import turtle

#Create Screen
screen = turtle.Screen()

#Set Screen Properties
screen.title('OOP Demo!')
screen.bgcolor("#90EE90")

#Create turtle
timmy = turtle.Turtle()
timmy.shape("arrow")
timmy.color("red")
timmy.pendown()

def move_forward():
    timmy.setheading(0)
    timmy.forward(10)

def move_backwards():
    timmy.setheading(180)
    timmy.forward(10)

def move_upwards():
    timmy.setheading(90)
    timmy.forward(10)

def move_downwards():
    timmy.setheading(270)
    timmy.forward(10)
    

screen.onkey(fun=move_forward, key="s")
screen.onkey(fun=move_backwards, key="a")
screen.onkey(fun=move_upwards, key="w")
screen.onkey(fun=move_downwards, key="x")

#Start listening
screen.listen()

#Exit on click
turtle.exitonclick()
