import os
import csv
from flask import Flask, render_template, request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("FLIGHTAPP_DB_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    with open("flights.csv") as file:
        data = csv.reader(file)
        for code, origin, destination, capacity, duration in data:
            flight = Flight(
                code=code,
                origin=origin,
                destination=destination,
                capacity=capacity,
                duration=duration,
            )
            db.session.add(flight)
            print(
                f"Added flight {code} from {origin} to {destination}lasting {duration} minutes"
            )
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        main()
