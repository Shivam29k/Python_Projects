from flask import Flask, render_template, globals
import requests

app = Flask(__name__)

@app.before_request
def before_request():
    request = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    globals.g.data = request.json()


@app.route('/')
def home():
    data = globals.g.data
    return render_template("index.html", content = data)

@app.route('/post/<int:id>')
def post(id):
    data = globals.g.data[id-1]
    return render_template('post.html', post = data)

if __name__ == "__main__":
    app.run(debug=True)
