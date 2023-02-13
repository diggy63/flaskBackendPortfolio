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
    dateAndTime = request.json["dateAndTime"]
    guests = request.json['guests']
    body = request.json['body']
    email = request.json['email']
    newReservation = Reservation(name=name,number=number,dateAndTime=dateAndTime,guests=guests,body=body, email=email)
    db.session.add(newReservation)
    db.session.commit()
    return "createing"