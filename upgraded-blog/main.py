from flask import Flask, render_template, globals
import requests

app = Flask(__name__)

@app.before_request
def before_request():
    request = requests.get('https://api.npoint.io/7180eb83e8f0da2a3769')
    globals.g.data = request.json()


@app.route('/')
def home():
    data = globals.g.data
    return render_template('index.html', blogs = data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:id>')
def post(id):
    data = globals.g.data[id-1]
    return render_template('post.html', post = data)

if __name__ == '__main__':
    app.run(debug=True)