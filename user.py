from datetime import datetime
import uuid


class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.creation_time = User.creation_time()
        self.user_id = User.unique_id()

    def creation_time():
        current_datetime = datetime.now()
        formatted_time = current_datetime.strftime("%Y/%m/%d %H:%M:%S")
        return formatted_time

    def unique_id():
        user_id = str(uuid.uuid4())
        return user_id
