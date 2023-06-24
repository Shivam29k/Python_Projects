import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data  = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

game_is_on = True
correct_ans = 0

while game_is_on:
    answer_state = screen.textinput(title=f"{correct_ans}/50 states guessed", prompt="Enter the name of state:").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states ]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        screen.bye()
        break
    if answer_state in all_states:
        correct_ans += 1
        guessed_states.append(correct_ans)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        row_data = data[data.state == answer_state]
        t.goto(int(row_data.x), int(row_data.y))
        t.write(f"{answer_state}", align="center", font=('Arial', 8, 'normal'))

screen.exitonclick()