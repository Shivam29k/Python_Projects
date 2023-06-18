from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Create and move all of our turtles to their starting positions
start_coordinate = -100
i = 0
all_turtles = []
for _ in colors:
    new_turtle = Turtle(shape="car")
    new_turtle.color(colors[i])
    new_turtle.penup()
    x = -230
    new_turtle.goto(x = -230, y = start_coordinate)
    start_coordinate += 40
    i+=1
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        # make each turtle move a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()