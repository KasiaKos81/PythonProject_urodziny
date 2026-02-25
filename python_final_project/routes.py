from flask import Blueprint, render_template,request
from db import db
from model import Flights

my_blueprint = Blueprint("my_blueprint", __name__)

@my_blueprint.route("/v1/flights", methods=["GET", "POST"])
def index():
    flights =db.session.query(Flights).all()
    return render_template("main.html", flights=flights)

@my_blueprint.route("/v1/flights/search", methods=["GET", "POST"])
def flights_search():
    searched_flights = []
    print(request.method)

    if request.method == "POST":
        departure_iata = request.form.get("departure_iata")

        if departure_iata:
            searched_flights = Flights.query.filter_by(departure_iata=departure_iata).all()

    return render_template("search.html", flights=searched_flights)