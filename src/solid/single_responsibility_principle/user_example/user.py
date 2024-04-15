class User:
    def __init__(self, username: str, email: str, phone_number: str):
        self._username = username
        self._email = email
        self._phone_number = phone_number

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @property
    def phone_number(self):
        return self._phone_number
