from flask import request, jsonify
from flask import request

from extensions import db

from models.Reservation import Reservation

def getAll():
    getAll = Reservation.query.all()
    allReservation = []
    for reservation in getAll:
        allReservation.append(reservation.serialize())
    return jsonify(allReservation)

def createReservation():
    name = request.json["name"]
    number = request.json["number"]
    date = request.json["dateAndTime"]
    guests = request.json['guests']
    body = request.json['body']
    email = request.json['email']
    time = request.json["time"]

    newReservation = Reservation(time=time,name=name,number=number,date=date,guests=guests,body=body, email=email)
    db.session.add(newReservation)
    db.session.commit()
    return "createing"