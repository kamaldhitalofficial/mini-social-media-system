import re


class Validation:
    def __init__(email):
        self.email = email


    def is_valid_email(email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, email):
            return email
        else:
            raise ValueError("Incorrect format for email!!!")
