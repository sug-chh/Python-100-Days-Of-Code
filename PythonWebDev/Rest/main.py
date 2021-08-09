from flask import Flask, json, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

##Connect to Database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


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
        # dictionary = {}
        # for column in self.__table__.columns:
        #     dictionary[column.name] = getattr(self, column.name)
        # return dictionary

        return {column.name : getattr(self, column.name) for column in self.__table__.columns}





@app.route("/")
def home():
    return render_template("index.html")


## HTTP GET - Read Record
@app.route("/random")
def random_route():
    all_cafes = db.session.query(Cafe).all()
    random_cafe = random.choice(all_cafes)
    return jsonify(random_cafe.to_dict())


@app.route("/all")
def get_all():
    all_cafe = db.session.query(Cafe).all()
    all_cafe_array = []
    for cafe in all_cafe:
        all_cafe_array.append(cafe.to_dict())
    return jsonify(cafes = all_cafe_array)
        
@app.route('/search')
def search():
    loc = request.args.get('loc')
    filtered_cafe = db.session.query(Cafe).filter_by(location = loc).first()
    if filtered_cafe:
        return jsonify(cafe = filtered_cafe.to_dict())
    else:
        return jsonify(error={'Not found' : "Sorry, we don't have a cafe at that location"})
        
    

@app.route('/update-price/<int:id>', methods = ['PATCH'])
def update_price(id):
    new_price = request.args.get('price')
    get_cafe = db.session.query(Cafe).get(id)

    if get_cafe:
        get_cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(cafe=get_cafe.to_dict()), 200
    else: 
        return jsonify(error = {"error": "Sorry the cafe with that id doesn't exist!"})

@app.route('/report-closed/<int:id>', methods=["Delete"])
def delete(id):
    api_key = request.args.get('api_key')
    if api_key == "api_key123":
        cafe = db.session.query(Cafe).get(id)
        if cafe:
            db.session.delete(cafe)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe from the database."}), 200
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Forbidden": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == "__main__":
    app.run(debug=True)
