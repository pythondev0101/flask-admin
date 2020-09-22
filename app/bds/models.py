from app import db
from app.admin.models import Admin
from app.core.models import Base


class Delivery(Base):
    __tablename__ = 'bds_delivery'

    """ COLUMNS """
    date = db.Column(db.DateTime, nullable=True)
    latitude = db.Column(db.String(255), nullable=True)
    longitude = db.Column(db.String(255), nullable=True)
    accuracy = db.Column(db.String(255), nullable=True)
    reference_number = db.Column(db.String(255), nullable=True)
