from datetime import datetime
import uuid


class User:
    _usernames = set()

    def __init__(self, username, name, email, bio, profile_picture_url):
        if username in User._usernames:
            raise ValueError(f"Username '{username}' is already taken.")
        else:
            self.username = username
        self.user_id = User.unique_id()
        self.name = name
        self.email = email
        self.creation_time = User.creation_time()
        self.bio = bio
        self.profile_picture_url = profile_picture_url

        User._usernames.add(username)

    def creation_time():
        current_datetime = datetime.now()
        formatted_time = current_datetime.strftime("%Y/%m/%d %H:%M:%S")
        return formatted_time

    def unique_id():
        user_id = str(uuid.uuid4())
        return user_id

    def update_profile(self, username=None, name=None, email=None, bio=None, profile_picture_url=None):
        if username and username != self.username:
            if username in User._usernames:
                raise ValueError(f"Username '{username}' is already taken.")
            User._usernames.remove(self.username)
            User._usernames.add(username)
            self.username = username

        if name:
            self.name = name
        if email:
            self.email = email
        if bio:
            self.bio = bio
        if profile_picture_url:
            self.profile_picture_url = profile_picture_url


    def get_profile_info(self):
        return f"""
User ID: {self.user_id}
Username: {self.username}
Name: {self.name}
Email: {self.email}
Bio: {self.bio}
Profile Picture URL: {self.profile_picture_url}
Account Created: {self.creation_time}
"""


    def __str__(self):
        return self.get_profile_info()
