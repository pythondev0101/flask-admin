from ez2erp.db.models import BaseModel
from ez2erp.db.fields import TextField



class Post(BaseModel):
    ez2collection = 'social_posts'
    ez2name = 'post'
    
    title = TextField()
