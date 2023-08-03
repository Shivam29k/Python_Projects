from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    request = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    data = request.json()
    return render_template("index.html", content = data)

@app.route('/post/<id>')
def post(id):
    request = requests.get(url='https://api.npoint.io/c790b4d5cab58020d391')
    data = request.json()[int(id)-1]
    return render_template('post.html', post = data)

if __name__ == "__main__":
    app.run(debug=True)
