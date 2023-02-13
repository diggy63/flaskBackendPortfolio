from extensions import db

class Test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1000))
    
    def serialize(self):
        return{
            'id': self.id,
            'name': self.name,
        }