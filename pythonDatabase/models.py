from flask import Flask
from flasl_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Flight(db.Model):
    __tablename__ = "flight"
    id = db.Column(db.Integer, primary_key=True)
    origin = db.Column(db.String, nullable=Flase)
    destination = db.Column(db.String, nullable=Flase)
    duration = db.Column(db.Integer, nullable=Flase)


class Passenger(db.Model):
    __tablename__="passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=Flase)
    flight_id = db.Column(dn.Integer, db.ForeignKey("flights.id"), nullable=Flase)
    