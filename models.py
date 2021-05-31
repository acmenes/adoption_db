'''Models for Pet Adoption'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

### CLASSES ###

class Pet(db.Model):
    '''Pet'''

    __tablename__ = "pets"

    id = db.Column(db.Integer, 
                    primary_key=True)

    name = db.Column(db.String(20), 
                    nullable=False)
    
    species = db.Column(db.String(25), 
                        nullable=False)

    photo_url = db.Column(db.String(1000))

    age = db.Column(db.Integer, nullable=False)

    notes = db.Column(db.String(10000), nullable=True)

    # how would you handle available? as an bool?

    available = db.Column(db.Boolean, default=True)

def connect_db(app):
    '''Connect the db to our app'''

    db.app = app
    db.init_app(app)