from flask import Flask, render_template, globals, request
import requests
from dotenv import load_dotenv
import smtplib
from email.message import EmailMessage
import os
load_dotenv()

MY_EMAIL = os.getenv('my_email')
PASSWORD = os.getenv("password")

app = Flask(__name__)

def send_mail(data):

    msg = EmailMessage()
    msg = EmailMessage()
    msg["From"] = MY_EMAIL
    msg["To"] = MY_EMAIL
    msg["Subject"] = "Contact Email Submission"
    msg.set_content(f"Name : {data['name']} \nEmail : {data['email']} \nPhone_no : {data['phone_no']} \nMessage : {data['message']}")
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.send_message(msg)

@app.before_request
def before_request():
    request = requests.get('https://api.npoint.io/7180eb83e8f0da2a3769')
    globals.g.data = request.json()


@app.route('/')
def home():
    data = globals.g.data
    return render_template('index.html', blogs = data)

@app.route('/contact', methods=['GET','POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        for i in range(100):
            send_mail(data)
            print("Message Successfully sent : ", i)
        return "<h1>Message Successfully sent</h1>"
    else:
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