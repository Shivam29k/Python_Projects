import turtle
import pandas
from states import states

screen = turtle.Screen()
screen.title("India State Guess Game")
image = "blank_india_map.gif"
turtle.addshape(image)
turtle.shape(image)



X  = []
Y = []

def make_csv(x, y):
    dict = {
        "states" : states,
        "x" : X,
        "y": Y
    }
    df = pandas.DataFrame(dict)
    df.to_csv('state_coordinates.csv')


def get_mouse_click_coor(x, y):
    X.append(x)
    Y.append(y)
    print(f"State Registered")

    if len(X) == 28:
        make_csv(X, Y)
        screen.bye()
    


# screen.listen()
turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()