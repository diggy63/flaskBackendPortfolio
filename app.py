from flask import Flask, jsonify
from flask_cors import CORS
from sqlalchemy import text
from flask_login import UserMixin
from flask_migrate import Migrate
from flask_jwt_extended import create_access_token,get_jwt,get_jwt_identity, unset_jwt_cookies, jwt_required, JWTManager


# retreaving db from exntions
from extensions import db


# create the app and configureing it
app = Flask(__name__)
CORS(app)
app.config.from_object('config')
db.init_app(app)
jwt = JWTManager(app)



#importing routes
from routes.auth_bp import auth_bp
from routes.user_bp import user_bp
from routes.reservations_bp import reservations_bp
from routes.emailReader_bp import emailReader_bp
# registering routes using blueprint
app.register_blueprint(auth_bp,url_prefix='/api/auth')
app.register_blueprint(user_bp,url_prefix='/api/users')
app.register_blueprint(reservations_bp,url_prefix='/api/reservations')
app.register_blueprint(emailReader_bp,url_prefix='/api/emailReader')

# simple code to make make sure the data base is connected
with app.app_context():
    try:
        connection = db.engine.connect()
        connection.execute(text("SELECT 1"))
        print("The database is connected")
        connection.close()
    except Exception as e:
        print("The database is not connected. Error: ", e)




if __name__ == "__main__":
    app.run()