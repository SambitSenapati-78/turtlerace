from turtle import Turtle, Screen
import random

game_not_end = False
screen = Screen()
screen.setup(500, 400)
user_input = screen.textinput("Make your bet", "which turtle will win the race ? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=positions[turtle_index])
    all_turtle.append(new_turtle)


if user_input:
    game_not_end = True
while game_not_end:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            game_not_end = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won. The {winning_color} turtle is the winner of the race. ")
            else:
                print(f"you've lost. The {winning_color} turtle is the winner of the race. ")
        random_length = random.randint(0, 10)
        turtle.forward(random_length)

screen.exitonclick()