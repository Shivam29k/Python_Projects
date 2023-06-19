from turtle import Turtle, Screen
screen = Screen()
SNAKE_LENGTH = 3
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
       
    def create_snake(self):   
        # length = 3
        for length in range(SNAKE_LENGTH):
            self.add_segment(length,0)
        screen.update()

    def add_segment(self, x,y):
        snake_segment = Turtle("square")
        snake_segment.penup()
        snake_segment.color("white")
        snake_segment.goto(x, y)
        self.segments.append(snake_segment)

    def extend(self):
        x_cor = self.segments[-1].xcor()
        y_cor = self.segments[-1].ycor()
        self.add_segment(x_cor, y_cor)

    def move(self):

        for seg_num in range(len(self.segments)-1,0,-1):

            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].setheading(RIGHT)