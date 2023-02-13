from flask import render_template, redirect, url_for, request, abort, jsonify, Blueprint

from controllers.UserController import getUser, createUser


user_bp = Blueprint('user_bp', __name__)

user_bp.route('/gettest', methods=['GET'])(getUser)
user_bp.route('/createtest', methods=['POST'])(createUser)
