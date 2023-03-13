from mongoengine.connection import connect
from mongoengine.document import Document
from mongoengine.fields import BinaryField, BooleanField, DateTimeField, EmailField, IntField, ListField, StringField
from datetime import datetime
import json


connect("mongo-db")

class User(Document):
    username = StringField(unique=True, required=False)
    email = EmailField(unique=True)
    password = BinaryField(required=False)
    age = IntField()
    bio = StringField(max_length=100)
    categories = ListField()
    admin = BooleanField(default=False)
    registred = BooleanField(default=False)
    date_created = DateTimeField(default=datetime.utcnow)

    def json(self):
        user_dict = {
            'username': self.username,
            'email': self.email
        }


user = User(
    username="TEST"
).save()