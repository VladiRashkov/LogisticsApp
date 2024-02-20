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
        return f' {self._first_name}, \n {self._last_name}, \n {self._username}, \n {self._email}'
            