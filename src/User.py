class User(ndb.Model):
    
    id = ndb.IntegerProperty()
    name = ndb.StringProperty()
    email = ndb.StringProperty()