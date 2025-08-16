from datetime import datetime
import uuid


class User:
    def __init__(self, username, name, email):
        self.user_id = User.unique_id()
        self.username = username
        self.name = name
        self.email = email
        self.creation_time = User.creation_time()

    def creation_time():
        current_datetime = datetime.now()
        formatted_time = current_datetime.strftime("%Y/%m/%d %H:%M:%S")
        return formatted_time

    def unique_id():
        user_id = str(uuid.uuid4())
        return user_id

    def __str__(self):
        return f"""
User ID: {self.user_id}
Username: {self.username}
Name: {self.name}
Email: {self.email}
Creation Time: {self.creation_time}
"""
