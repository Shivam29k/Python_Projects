from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",22, "normal") 
GAME_OVER_FONT = ("courier",30, "normal") 
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt", "r") as f:
            data = f.readlines() 
        self.highscore = data[0] 
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score : {self.highscore}", align = ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0,0)
        self.write(f"GAME OVER", align = ALIGNMENT, font=GAME_OVER_FONT)
        if int(self.score)>int(self.highscore):
            self.highscore = self.score
            with open("data.txt", "w") as f:
                f.write(str(self.highscore))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.highscore}", align = "center", font= FONT )