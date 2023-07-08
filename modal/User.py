

class User:
    email: str
    password: str
    username: str

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username