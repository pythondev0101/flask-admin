""" ADMIN MODELS"""
from app import db


class Admin(object):
    """ Ito yung mga functions sa dropdown ng model sa admin page sidebar (eg. Create new, View all)
    """
    __amfunctions__ = [{}]
    
    """ Ito yung icon sa admin page (eg. pe-7s-users).
    Refer sa dashboardpack.com sa mga available icons
    """
    __amicon__ = ""
    
    @property
    def __amname__(self):
        """ Ito yung parang code nya(eg. auth) for authentication.
        Ito yung reference mo sa model sa mga code mo wag yung description
        Ex. if model.__amcode__ = 'auth': 
        """
        raise NotImplementedError('Must implement admin-model name')

    @property
    def __amdescription__(self):
        """ Ito ung visible sa admin page(eg. Authentication)
        """
        raise NotImplementedError('Must implement admin-model description')


class AdminOptions(db.Model):
    __tablename__ = 'admin_options'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('auth_user.id'))
    header_color = db.Column(db.String(64))
    sidebar_color = db.Column(db.String(64))
