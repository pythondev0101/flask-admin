import sys
from datetime import datetime
from bson import ObjectId
from pymongo.collection import Collection
from copy import deepcopy, copy
from ez2erp import MONGO



class Query:
    def __init__(self, model):
        self.model = model
        self.collection: Collection = getattr(MONGO.db, self.model.ez2collection)


    def all(self, columns=None):
        query = list(self.collection.find({}))
        # print("query:", query)
        # print(self.model)
        
        if columns is None: # TODO
            # raise Exception("Query.all() development in-progress")
            result = []
            
            for doc in query:
                # print("doc:", doc
                # blueprint = getattr(sys.modules[self.model.__module__], self.model.__name__)
                # print(blueprint)
                # # blueprint = globals()[self.model.__name__]
                # obj = blueprint(doc)
                # print("id:", hex(id(obj)))
                result.append(self.model(doc))
            return result
        
        result = []
        for doc in query:
            row = []
            obj = self.model(doc)

            for col in columns:
                row.append(getattr(obj, col.field_name))
            result.append(row)
        return result
    
    
    def count(self, search={}):
        query = self.collection.count_documents(search)
        return query


    def find_one(self, search):
        query = self.collection.find_one(search)
        if query is None:
            return None
        return self.model(query)


    def insert_one(self, data):
        data['created_at'] = datetime.utcnow()
        query = self.collection.insert_one(data)
        id = query.inserted_id
        return self.retrieve(id)


    def retrieve(self, id):
        query = self.collection.find_one({'_id': ObjectId(id)})
        return self.model(query)
        