from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API")
TOKEN = os.getenv("Token")
URL = 'https://api.themoviedb.org/3/search/movie'

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

##CREATE DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy()
db.init_app(app)


##CREATE TABLE
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

class EditForm(FlaskForm):
    rating = StringField("Your rating out of 10", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done", validators=[DataRequired()])

class AddMovie(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    search = SubmitField("Done")

# ------------------------------------------------- for creating table ----------------------------------------------------
# with app.app_context():
#     db.create_all()

## After adding the new_movie the code needs to be commented out/deleted.
## So you are not trying to add the same movie twice. The db will reject non-unique movie titles.
# new_movie = Movie(
#     title="Avatar The Way of Water",
#     year=2022,
#     description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
#     rating=7.3,
#     ranking=9,
#     review="I liked the water.",
#     img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
# )
# with app.app_context():
#     db.session.add(new_movie)
#     db.session.commit()
# ---------------------------------------------------------------------------------------------------------------------------



@app.route("/", methods=['GET', 'POST'])
def home():
    data = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = data.scalars().all()

    i=0
    for movie in movies:
        print(movie.rating)
        movie.ranking = len(movies)-i
        i+=1
    db.session.commit()
    # print(movies.all())

    return render_template("index.html", movies=movies)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    movie = db.get_or_404(Movie, movie_id)
    if request.method == "GET":
        # print(id, "---> ", movie.title)
        return render_template('edit.html', movie=movie, form = form)
    else :
        # if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddMovie()
    if form.validate_on_submit():
        title = form.title.data
        params = {
            'query': title,
            'include_adult':True,
            "page":1,
            "language": 'en-US'
        }
        headers = {
            "accept": "application/json",
            "Authorization": TOKEN,
        }
        response = requests.get(url=URL, headers=headers, params=params)
        movies = response.json()['results']
        return render_template('select.html', movies=movies)

    return render_template('add.html', form=form)

@app.route('/addindb')
def addindb():
    movieid = request.args.get('movieid')
    url = f"https://api.themoviedb.org/3/movie/{movieid}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": TOKEN,
    }
    params = {
        # "page":1,
        "language": 'en-US'
    }
    response = requests.get(url=url, headers=headers).json()
    new_movie = Movie(
        title=response['title'],
        year=int(response['release_date'][:4]),
        description=response['overview'],
        rating= None,
        ranking= None,
        review=None,
        img_url=f"https://image.tmdb.org/t/p/w220_and_h330_face{response['poster_path']}"
    )
    print(new_movie)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for('edit', id=new_movie.id))



if __name__ == '__main__':
    # make debug=False whlie adding to the database from main.py directly coz if debug is true then it will keep on executing the add to databse command everytime it reloads which it keeps doing every moment
    # app.run(debug=False)
    app.run(debug=True)