import turtle
import pandas

screen = turtle.Screen()
screen.title("India State Guess Game")
image = "blank_india_map.gif"
turtle.addshape(image)
turtle.shape(image)

data = pandas.read_csv("state_coordinates.csv")
all_states = data.states.to_list()
guessed_states = []

game_is_on = True
correct_ans = 0
while game_is_on:
    answer_state = screen.textinput(title= f"{correct_ans}/28 States Guessed", prompt="Type the name of state:").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        correct_ans += 1
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(f"{answer_state}", align="center", font=('Arial', 8, 'normal'))
        
dict = {
    "States" : [state for state in all_states if state not in guessed_states]
}
    
print(dict)

screen.exitonclick()