from flask import Flask, render_template, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap5

class MyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=30)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=40), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    login = SubmitField('Log In')

'''
https://wtforms.readthedocs.io/en/2.3.x/fields/ ---> Go to the bottom to find other validators which are present in wtf forms
https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields ---> basic fields
'''

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_string"
bootstrap = Bootstrap5(app)  #initializing bootstrap-flask

users = [
    {
    'name' : 'Shivam',
    'email' : 'skumarshivam50@gmail.com',
    'password' : '1234567890'
    },
    {
    'name' : 'Shivam1',
    'email' : 'shivamkg29@gmail.com',
    'password' : '1234567890'
    }
]


@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        for user in users:
            if request.form['email'] == user['email']:
                if request.form['password'] == user['password']:
                    return redirect('/success')
        return redirect('/denied')
    return render_template('login.html', form = form)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/denied')
def denied():
    return render_template('denied.html')

if __name__ == '__main__':
    app.run(debug=True)
