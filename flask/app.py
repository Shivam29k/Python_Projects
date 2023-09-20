from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
# db = SQLAlchemy(app)

# class ToDo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime, default = datetime.utcnow)

#     def __repr__(self) -> str:
#         return f'{self.sno} - {self.title}'

# @app.cli.command()
# def init_db():
#     with app.app_context():
#         db.create_all()
#         print('Database initialized')

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
           "<p> this is paragraph.</p>"\
           "<img src='https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif'/>"\
           "<img src='https://img.freepik.com/free-vector/cute-cat-with-love-sign-hand-cartoon-illustration-animal-nature-concept-isolated-flat-cartoon-style_138676-3419.jpg?w=740&t=st=1690478790~exp=1690479390~hmac=18c606222a5e86c0492d50df8027be93e9826482d406a16f2f30b14c5ea69db4'/>"


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper
def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bye')
@make_bold
@make_emphasis
@make_underline
def bye():
    return "bye"

@app.route('/template_file')
def template():
    return render_template('index.html')


@app.route('/products')
def products():
    return 'this is the products page'

@app.route('/username/<name>/<int:number>')
def greet(name, number):
    return f"Hello {name}, you are {number} years old."

if __name__=='__main__':
    # Run the app in debug mode to auto reload the app
    app.run(debug=True)