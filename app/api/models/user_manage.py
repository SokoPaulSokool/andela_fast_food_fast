
class User:
    """creates order"""

    def __init__(self, user_id, user_name, email, password, user_type):
        self.user_id = user_id
        self.user_name = user_name
        self.email = email
        self.password = password
        self.user_type = user_type

    def toJSON(self):
        return {"user_id": self.user_id, "user_name": self.user_name,
                "email": self.email, "password": self.password,
                "user_type": self.user_type
                }
