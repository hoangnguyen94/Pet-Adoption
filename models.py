
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

GENERIC_IMAGE = "https://cdn2.vectorstock.com/i/1000x1000/56/61/paw-print-vector-20655661.jpg"

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet"""
    __tablename__ = "pets"

    id = db.Column(db.INTEGER, primary_key=True,
                    autoincrement=True)
    name = db.Column(db.TEXT, nullable=True)
    species = db.Column(db.TEXT, nullable=True)
    photo_url = db.Column(db.TEXT)
    age = db.Column(db.INTEGER)
    notes = db.Column(db.TEXT)
    available = db.Column(db.BOOLEAN, default=True)

    def image_url(self):
        """Return image for pet or empty image"""
        return self.photo_url or GENERIC_IMAGE