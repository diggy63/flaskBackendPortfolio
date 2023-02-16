from flask import render_template, redirect, url_for, request, abort, jsonify, Blueprint

from controllers.ReservationsController import getAll, createReservation, deleteReservation, getOne


reservations_bp = Blueprint('reservations_bp', __name__)

reservations_bp.route('/getall', methods=['GET'])(getAll)
reservations_bp.route('/get/<int:id>', methods=['GET'])(getOne)
reservations_bp.route('/create', methods=['POST'])(createReservation)
reservations_bp.route('/delete/<int:id>', methods=['DELETE'])(deleteReservation)

