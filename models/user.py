class User:
    def __init__(self, first_name, last_name, username, email):
        if "@" not in email:
            raise ValueError('Invalid email address')
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self._email = email

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError('Invalid email address')
        self._email = value

    def __str__(self):
        return f' {self.first_name}, \n {self.last_name}, \n {self.username}, \n {self.email}'
            