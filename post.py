from datetime import datetime
import uuid


class Post:

    def __init__(self, author, content):
        self._post_id = str(uuid.uuid4())
        self.author = author
        self.content = content
        self._timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self._like_count = 0
        self._view_count = 0


        def get_post_id(self):
            return self._post_


        def get_author(self):
            return self._author


        def get_content(self):
            self._view_count += 1
            return self._content


        def get_timestamp(self):
            return self._timestamp


        def like_post(self):
            self._like_count += 1


        def get_likes(self):
            return self.like_count
