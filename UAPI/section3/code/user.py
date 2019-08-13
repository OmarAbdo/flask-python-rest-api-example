class User:
    #id is a python keyword so you need to use _id or anything else
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password