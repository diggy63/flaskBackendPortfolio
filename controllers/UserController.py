from flask import request, jsonify
from flask import request

from extensions import db

from models.Test import Test

def getUser():
    result = []
    newT = Test.query.all()
    for test in newT:
        result.append(test.serialize())

    return result

def createUser():
    newName = request.json['name']
    print(newName)
    newT = Test(name=newName)
    db.session.add(newT)
    db.session.commit()
    return "creating"