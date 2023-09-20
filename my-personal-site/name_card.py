from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('name_card_index.html')

if '__main__' == __name__:
    app.run(debug=True)