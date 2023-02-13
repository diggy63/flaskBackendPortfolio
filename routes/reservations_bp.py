from flask import render_template, redirect, url_for, request, abort, jsonify, Blueprint

from controllers.ReservationsController import getAll, createReservation


reservations_bp = Blueprint('reservations_bp', __name__)

reservations_bp.route('/getall', methods=['GET'])(getAll)
reservations_bp.route('/create', methods=['POST'])(createReservation)
