class User:
    """
    A class to construct representations of user for a certain platform.
    """
    def __init__(self, username: str, email: str, phone_number: str):
        self._username = username
        self._email = email
        self._phone_number = phone_number

    @property
    def username(self) -> str:
        """
        A property for the username of the user.

        :return: the user's username
        """
        return self._username

    @property
    def email(self) -> str:
        """
        A property for the email address of the user.

        :return: the user's email address
        """
        return self._email

    @property
    def phone_number(self) -> str:
        """
        A property for the phone number of the user.

        :return: the user's phone number
        """
        return self._phone_number
