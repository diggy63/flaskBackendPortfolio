from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_login import UserMixin
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)
app.config.from_object('config')
db = SQLAlchemy(app)


migrate = Migrate(app, db)


with app.app_context():
    try:
        connection = db.engine.connect()
        connection.execute(text("SELECT 1"))
        print("The database is connected")
        connection.close()
    except Exception as e:
        print("The database is not connected. Error: ", e)



class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
        }

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/api")
def api():
    return jsonify({"message": "Found Api"})

@app.route("/gettest")
def get_test():
    test = Test.query.all()
    sent = test[0].serialize()
    return sent


if __name__ == "__main__":
    app.run()