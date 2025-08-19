from datetime import datetime
import uuid


class Post:

    def __init__(self, content, author):
        self.__post_id = str(uuid.uuid4())
        self.__author = author
        self.__content = content
        self.__timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.__like_count = 0
        self.__view_count = 0


    def get_post_id(self):
        return self.__post_id


    def get_author(self):
        return self.__author


    def get_content(self):
        self.__view_count += 1
        return self.__content


    def get_timestamp(self):
        return self.__timestamp


    def like_post(self):
        self.__like_count += 1


    def get_likes(self):
        return self.__like_count


    def get_views(self):
        return self.__view_count


    def __str__(self):
        return (f"Post by @{self.__author.username} at {self.__timestamp}:\n"
                f"{self.__content}\n"
                f"❤️ {self.__like_count} | 👁️ {self.__view_count}")

    def __repr__(self):
        return (f"Post(post_id='{self.__post_id}', author='{self.__author.username}', "
                f"likes={self.__like_count}, views={self.__view_count})")
