from datetime import datetime
from typing import Collection



# _collection: Collection = MONGO.db.core_events


class NotificationRepository(object):
    @staticmethod
    def create(model: any):
        data = {
            'message': "A new {} was created".format(model.get_code()),
            'object_id': model.get_object_id(),
            'model': type(model).__name__,
            'type': 'created',
            'data': model.get_data(),
            'date_created': datetime.utcnow(),
            'timezone': 'Asia/Manila'
        }
        
        return _collection.insert_one(data)
