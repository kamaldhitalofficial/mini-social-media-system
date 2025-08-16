from datetime import datetime

class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        self.creation_time = User.creation_time()

    def creation_time():
        current_datetime = datetime.now()
        formatted_time = current_datetime.strftime("%Y/%m/%d %H:%M:%S")
        return formatted_time
