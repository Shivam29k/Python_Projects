from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("courier",20, "normal") 
GAME_OVER_FONT = ("courier",30, "normal") 


class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()

        self.player_1 = Screen().textinput(title = "Player Name", prompt="Enter the name of player 1")
        self.player_2 = Screen().textinput(title = "Player Name", prompt="Enter the name of player 2")
        self.win_score = int(Screen().textinput(title = "Winning Score", prompt="At what score you wanna challange eachother ?"))
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.l_score = 0
        self.r_score = 0
        self.write(f"{self.player_1} : {self.l_score}    |    {self.player_2} : {self.r_score}", align = ALIGNMENT, font=FONT)
    

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.write(f"{self.player_1} : {self.l_score}    |    {self.player_2} : {self.r_score}", align = ALIGNMENT, font=FONT)
    def r_point(self):
        self.r_score += 1
        self.clear()
        self.write(f"{self.player_1} : {self.l_score}    |    {self.player_2} : {self.r_score}", align = ALIGNMENT, font=FONT)

    def game_over(self):
        if self.l_score >= self.win_score or self.r_score >= self.win_score:
            self.hideturtle()
            self.goto(0,25)
            self.write(f"GAME OVER", align = ALIGNMENT, font=GAME_OVER_FONT)
            if self.l_score == self.win_score:
                self.goto(0,-50)
                self.write(f"{self.player_1} WINS !!", align = ALIGNMENT, font=FONT)
            else:
                self.goto(0,-50)
                self.write(f"{self.player_2} WINS !!", align = ALIGNMENT, font=FONT)

            return True
