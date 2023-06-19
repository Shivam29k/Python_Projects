from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food

    if snake.head.distance(food) < 18:
        scoreboard.increase_score()
        snake.extend()
        # print((snake.segments[-1].position()))
        food.refresh()    
    
    if snake.head.xcor() < -282 or snake.head.xcor() > 282 or snake.head.ycor() < -282 or snake.head.ycor() > 282:
        game_is_on = False
        scoreboard.game_over()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            # print("Touch hua")
            game_is_on = False
            scoreboard.game_over()
    

screen.exitonclick()