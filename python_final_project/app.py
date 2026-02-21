from flask import Flask
from routes import my_blueprint
from views import users_blueprint
from db import db
from service import get_api_info
from model import Flights

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db.init_app(app)
app.register_blueprint(my_blueprint)
app.register_blueprint(users_blueprint)

with app.app_context():
    db.create_all()
    flights = Flights.query.all()
    if not flights:
        flights_information = get_api_info()
        for flight in flights_information:
            departure_airport = flight.get("departure", {}).get("airport")
            arrival_airport = flight.get("arrival", {}).get("airport")
            departure_iata = flight.get("departure", {}).get("iata")
            arrival_iata = flight.get("arrival", {}).get("iata")
            airline_name = flight.get("airline", {}).get("name")
            flight_number = flight.get("flight", {}).get("number")


            new_flight = Flights(
                departure_airport=departure_airport,
                arrival_airport=arrival_airport,
                departure_iata=departure_iata,
                arrival_iata=arrival_iata,
                airline_name=airline_name,
                flight_number=flight_number,
        )

            db.session.add(new_flight)
            db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)