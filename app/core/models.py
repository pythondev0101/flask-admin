#TODO: create Base,Customer model
from app import db
from datetime import datetime

# MODEL.BASE
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    # TODO server_default=value
    active = db.Column(db.Boolean, nullable=False, default="1")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self):
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        self.active = 1