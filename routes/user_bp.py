from flask import render_template, redirect, url_for, request, abort, jsonify, Blueprint

from controllers.UserController import getUser


user_bp = Blueprint('user_bp', __name__)

user_bp.route('/get', methods=['GET'])(getUser)

