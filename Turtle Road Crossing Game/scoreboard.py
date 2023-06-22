from turtle import Turtle
ALIGNMENT = "left"
FONT = ("courier",20, "normal") 
GAME_OVER_FONT = ("courier",30, "normal") 

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()

        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280, 270)
        self.clear()
        self.write(f"Level : {self.level}", align = ALIGNMENT, font=FONT)
    
    def level_inc(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", align = ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = "center", font=GAME_OVER_FONT)

