from flask import render_template, redirect, url_for, request, abort, jsonify, Blueprint

from controllers.EmailReaderController import getOAuth, readEmails


emailReader_bp = Blueprint('emailReader_bp', __name__)

emailReader_bp.route('/OAuth', methods=['GET'])(getOAuth)
emailReader_bp.route('/Scan', methods=['GET'])(readEmails)
