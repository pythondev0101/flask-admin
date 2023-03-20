from typing import Collection
from ez2erp import MONGO



class EventRepository(object):
    
    # _collection: Collection = MONGO.db.core_events
    
    @staticmethod
    def create(model: any):
        pass
        # data = {
        #     'message': "A new {} was created".format(model.get_code()),
        #     'object_id': model.get_object_id(),
        #     'model': type(model).__name__,
        #     'type': 'created',
        #     'data': model.get_data()
        # }
        # return _collection.insert_one(data)
