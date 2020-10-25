from app import db
from app.admin.models import Admin
from app.core.models import Base
from datetime import datetime


# class Delivery(Base):
#     __tablename__ = 'bds_delivery'

#     """ COLUMNS """
#     date = db.Column(db.DateTime, nullable=True)
#     latitude = db.Column(db.String(255), nullable=True)
#     longitude = db.Column(db.String(255), nullable=True)
#     accuracy = db.Column(db.String(255), nullable=True)
#     reference_number = db.Column(db.String(255), nullable=True)


class Subscriber(Base, Admin):
    __tablename__ = 'bds_subscribers'
    __amname__ = 'subscriber'
    __amdescription__ = 'Subscribers'
    __amicon__ = 'pe-7s-users'
    __amfunctions__ = []
    __list_view_url__ = 'bp_bds.subscribers'

    """ COLUMNS """
    fname = db.Column(db.String(64), nullable=True)
    lname = db.Column(db.String(64), nullable=True)
    email = db.Column(db.String(64), nullable=True, unique=True)
    address = db.Column(db.String(1000), nullable=True)
    longitude = db.Column(db.String(255),nullable=True)
    latitude = db.Column(db.String(255), nullable=True)
    deliveries = db.relationship('Delivery', cascade='all,delete', backref="subscriber")
    area_id = db.Column(db.Integer, db.ForeignKey('bds_area.id', ondelete="SET NULL"), nullable=True)
    area = db.relationship('Area',backref="subscribers")

    @property
    def url():
        return "bp_bds.subscribers"

class Delivery(Base, Admin):
    __tablename__ = 'bds_delivery'
    __amname__ = 'delivery'
    __amdescription__ = 'Deliveries'
    __amicon__ = 'pe-7s-paper-plane'
    __amfunctions__ = []
    __list_view_url__ = 'bp_bds.deliveries'
    
    """ COLUMNS """
    subscriber_id = db.Column(db.Integer, db.ForeignKey('bds_subscribers.id', ondelete="SET NULL"), nullable=True)
    delivery_date = db.Column(db.DateTime, default=datetime.utcnow,nullable=True)
    date_delivered = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(255), nullable=True)


# area_subscribers = db.Table('bds_area_subscribers',
#     db.Column('subscriber_id', db.Integer, db.ForeignKey('bds_subscribers.id'), primary_key=True),
#     db.Column('area_id', db.Integer, db.ForeignKey('bds_area.id'), primary_key=True)
# )


# area_messengers = db.Table('bds_area_messengers',
#     db.Column('user_id', db.Integer, db.ForeignKey('auth_user.id'), primary_key=True),
#     db.Column('area_id', db.Integer, db.ForeignKey('bds_area.id'), primary_key=True)
# )


class Area(Base, Admin):
    __tablename__ = 'bds_area'
    __amname__ = 'area'
    __amdescription__ = 'Areas'
    __amicon__ = 'pe-7s-flag'
    __amfunctions__ = []
    __list_view_url__ = 'bp_bds.areas'

    """ COLUMNS """
    name = db.Column(db.String(255),nullable=False)
    # code = db.Column(db.String(255),nullable=False)
    description = db.Column(db.String(1000),nullable=True)
    # subscribers = db.relationship('Subscriber', secondary=area_subscribers, lazy='subquery',backref=db.backref('area', lazy=True))
    # messengers = db.relationship('User', secondary=area_messengers, lazy='subquery',backref=db.backref('area', lazy=True))


# class AreaSubscribers(db.Model):
#     __tablename__ = 'bds_area_subscribers'

#     """ COLUMNS """
#     id = db.Column(db.Integer, primary_key=True)
#     area_id = db.Column(db.Integer, db.ForeignKey('bds_area.id',ondelete='CASCADE'))
#     subscriber_id = db.Column(db.Integer, db.ForeignKey('bds_subscribers.id', ondelete="SET NULL"), nullable=True)
#     subscriber = db.relationship('Subscriber', backref="area_subscriber")


# class AreaMessengers(db.Model):
#     __tablename__ = 'bds_area_messengers'

#     """ COLUMNS """
#     id = db.Column(db.Integer, primary_key=True)
#     area_id = db.Column(db.Integer, db.ForeignKey('bds_area.id',ondelete='CASCADE'))
#     user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id', ondelete="SET NULL"), nullable=True)
#     user = db.relationship('User', backref="area_messenger")


class Messenger(db.Model, Admin):
    __abstract__ = True
    __amname__ = 'user'
    __amdescription__ = 'Messengers'
    __amicon__ = 'pe-7s-car'
    __amfunctions__ = []
    __list_view_url__ = 'bp_bds.messengers'
