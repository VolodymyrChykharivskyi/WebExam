from datetime import datetime
from flask import Flask
from appInit import db
from sqlalchemy.inspection import inspect

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(20), nullable=False)
    car_brand = db.Column(db.String(20), nullable=False)
    technical_condition = db.Column(db.String(20), nullable=False)
    under_way = db.Column(db.String(10), nullable=False)
    price = db.Column(db.String(20), nullable=False)
    date_of_manufacture = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return u"Car({self.license_plate}, {self.car_brand})"
