from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Initializing DataBase
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


@app.route('/')
def home():
    flag = False
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
        print(len(all_books))
        if len(all_books)==0:
            flag = True
    return render_template('index.html', flag= flag, books=all_books)

@app.route('/delete', methods=['GET'])
def delete():
    if request.method=='GET':
        id = request.args.get('id')
        book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('home'))

@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method=='GET':
        id = request.args.get('id')
        book = db.session.execute(db.select(Book).where(Book.id == id)).one()[0]
        db.session.commit()
        print(book.title)
        return render_template('edit.html', book=book)
    else:
        rating = request.form['Rating']
        id = request.args.get('id')
        with app.app_context():
            book = db.session.execute(db.select(Book).where(Book.id == id)).one()[0]
            book.rating = rating
            db.session.commit()
        return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method=='POST':

        with app.app_context():
            new_book = Book( title=request.form['Title'], author=request.form['Author'], rating=request.form['Rating'])
            db.session.add(new_book)
            db.session.commit()
            print('Book Added: ',new_book)
        return redirect(url_for('home'))
    return render_template('add.html')


if __name__ == "__main__":
    app.run(debug=True)
