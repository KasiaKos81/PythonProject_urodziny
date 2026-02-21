from flask import Blueprint, render_template
from db import db
from model import Flights


my_blueprint = Blueprint("my_blueprint", __name__)

base_url = "https://api.aviationstack.com"

@my_blueprint.route("/v1/flights", methods=["GET", "POST"])
def index():
    flights =db.session.query(Flights).all()
    return render_template("main.html", flights=flights)



