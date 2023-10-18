from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy()
db.init_app(app)

# Flask login
login_manager = LoginManager()
login_manager.init_app(app)
# ------> user loader callback function for flask login
@login_manager.user_loader
def load_user(user_id):
    # return User.query.get(int(user_id))
    # OR
    return db.get_or_404(User, user_id)

# ------------------------------------------------------------------------------------------------------#
# CREATE TABLE IN DB
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


    # below methods are not required if we use UserMixin, they are set by default in UserMixin
    # create these methods when you need to customize the UserMixin class (for example, if you want to verify the otp before login)
    # def is_active(self):
    #     return True

    # def get_id(self):
    #     return str(self.id)

    # def is_anonymous(self):
    #     return False

    # def is_authenticated(self):
    #     return True
# ------------------------------------------------------------------------------------------------------#

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get Form Fields
        new_user = User(
            email = request.form['email'],
            name = request.form['name'],
            password = generate_password_hash(request.form['password'], method='pbkdf2:sha256', salt_length=8)
        )
        try:
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            flash('You have successfully registered!', 'success')
            return redirect(url_for('secrets'))
        except IntegrityError:
            db.session.rollback()
            flash('Email address already exists. Please choose a different email address.', 'error')
    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # user = User.query.filter_by(email=email).first()
        # OR
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()
        # Check if user actually exists
        # Take the user supplied password, hash it, and compare it to the hashed password in database
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('secrets'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
            return redirect(url_for('login'))
    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html",logged_in=current_user.is_authenticated)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static', path='files/cheat_sheet.pdf')

if __name__ == "__main__":
    app.run(debug=True, port=5004)
