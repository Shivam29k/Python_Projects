from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import random
import json

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy()
db.init_app(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }


# with app.app_context():
#     db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    request = db.session.execute(db.select(Cafe))
    all_cafes = request.scalars().all()
    random_cafe = random.choice(all_cafes)
    cafe = random_cafe.to_dict()
    return jsonify(cafe)

@app.route("/all")
def get_all_cafe():
    # request = db.session.execute(db.select(Cafe))
    # all_cafes = request.scalars().all()
    all_cafes = Cafe.query.all()
    cafes = {"cafes": []}
    for cafe in all_cafes:
        cafes["cafes"].append(cafe.to_dict())
    return jsonify(cafes)

@app.route("/search")
def search():
    location = request.args.get("loc")
    data = Cafe.query.all()
    all_cafes = []
    for cafe in data:
        if location.lower() in cafe.location.lower():
            all_cafes.append(cafe)

    if all_cafes:
        cafes = {"cafes": []}
        for cafe in all_cafes:
            cafes["cafes"].append(cafe.to_dict())
        return jsonify(cafes)
    else:
        return jsonify({"error": {"Not Found": "Sorry, we don't have a cafe at that location."}})


## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.args.to_dict()
    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data["seats"],
        has_toilet=bool(data["has_toilet"]),
        has_wifi=bool(data["has_wifi"]),
        has_sockets=bool(data["has_sockets"]),
        can_take_calls=bool(data["can_take_calls"]),
        coffee_price=data["coffee_price"],
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})

## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_id = cafe_id
    print(cafe_id)
    new_price = request.args.get("new_price")
    cafe = Cafe.query.get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}) , 200
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}) , 404

## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    cafe_id = cafe_id
    API = request.args.get("api-key")
    cafe = Cafe.query.get(cafe_id)
    if API == "TopSecretAPIKey":
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."}) , 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}) , 404
    else:
        return jsonify(error={"Not Found": "Sorry that's not allowed. Make sure you have the correct api-key."}) , 403
if __name__ == '__main__':
    app.run(debug=True)