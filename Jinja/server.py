from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)


@app.route('/')
def home():
    random_num = random.randint(1,10)
    year = datetime.date.today().year
    return render_template('index.html', num = random_num, year = year)

@app.route('/guess/<name>')
def guess(name):
    request = requests.get(url='https://api.genderize.io', params={'name':name})
    gender = request.json()['gender']
    request = requests.get(url='https://api.agify.io', params={'name':name})
    age = request.json()['age']
    return render_template('guess.html', name = name, gender = gender, age = age)

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    request = requests.get(url='https://api.npoint.io/7b5973f8bcea520e146b')
    blogs = request.json()
    return render_template('blog.html', blogs = blogs)
if __name__ == '__main__':

    app.run(debug=True)