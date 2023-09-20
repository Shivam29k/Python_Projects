from flask import Flask
import random
app = Flask(__name__)


num = random.randint(0,9)

@app.route('/')
def guess_no():
    return f"<b><h1>Guess a number between 0 and 9 ----{num}----</h1></b>"\
           '<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif ></img>'

@app.route('/<int:number>')
def check(number):
    if number == num:
        return  "<b><h1 style='color: green;'>You found me</h1></b>"\
                '<img src=https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif></img>'
    elif number > num:
        return  "<b><h1 style='color: blue;'>too high, try again!</h1></b>"\
                '<img src=https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif></img>'
    elif number < num:
        return  "<b><h1 style='color: red;'>too low, try again</h1></b>"\
                '<img src=https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif></img>'





if __name__=='__main__':
    # Run the app in debug mode to auto reload the app
    app.run(debug=True)