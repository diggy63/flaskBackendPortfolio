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

def getOne(id):
    reservation = Reservation.query.get(id)
    if reservation:
        return reservation.serialize()
    else:
        return jsonify({'action':'couldnt find'})

def createReservation():
    name = request.json["name"]
    number = request.json["number"]
    date = request.json["date"]
    guests = request.json['guests']
    body = request.json['body']
    email = request.json['email']
    time = request.json["time"]

    newReservation = Reservation(time=time,name=name,number=number,date=date,guests=guests,body=body, email=email)
    db.session.add(newReservation)
    db.session.commit()
    return {"msg":"reservation created"}

def deleteReservation(id):
    reservation = Reservation.query.get(id)
    if reservation:
        db.session.delete(reservation)
        db.session.commit()
        return jsonify({'action':'delte successful'})
    else:
        return jsonify({'action':'delte unsuccessful'})