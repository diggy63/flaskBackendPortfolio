from extensions import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    number = db.Column(db.String(1000))
    date = db.Column(db.String(1000))
    guests = db.Column(db.String(1000))
    time = db.Column(db.String(1000))
    email = db.Column(db.String(1000))
    body = db.Column(db.String(1000))

    
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
            "number": self.number,
            "date": self.date,
            "guests": self.guests,
            "body":self.body,
            "email": self.email,
            "time": self.time
        }