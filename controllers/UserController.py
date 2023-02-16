from flask import request, jsonify
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity

from extensions import db

from models.User import User

@jwt_required()
def getUser():
    print("in get")
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    user = user.serialize()
    print(user)
    return jsonify(user)

