from db import db

class Flights(db.Model):
    __tablename__ = 'flights'
    id = db.Column(db.Integer, primary_key=True)
    departure_airport = db.Column(db.String(100))
    arrival_airport = db.Column(db.String(100))
    departure_iata = db.Column(db.String(100))
    arrival_iata = db.Column(db.String(100))
    airline_name = db.Column(db.String(100))
    flight_number = db.Column(db.String(100))

