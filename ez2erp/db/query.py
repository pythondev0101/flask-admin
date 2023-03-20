from bson import ObjectId
from ez2erp import MONGO



class Query:
    def __init__(self, model):
        self.model = model
        self.collection = getattr(MONGO.db, self.model.collection)


    def retrieve(self, id):
        query = self.collection.find_one({'_id': ObjectId(id)})
        return self.model(query)
    
    
    def all(self, columns=None):
        query = list(self.collection.find({}))
        result = []
        for row in query:
            if columns is None:
                result.append(self.model(row))
            else:
                
                result.append([
                    self.model.id,
                    
                ])
        return result
