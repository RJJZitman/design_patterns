from user import User
from message_sender import SenderInterface


class UserManager:
    """
    Manages the registered users and allows to contact them via a provided SenderInterface implementation.
    """
    def __init__(self):
        self._users: dict[str, User] = {}

    def add_user(self, user: User) -> None:
        """
        Add a user to the registry.

        :param user: the User representation of the user you want to add to the registry,
        """
        self._users[user.username] = user

    def remove_user(self, user: User) -> None:
        """
        Permanently removes a user to the registry.

        :param user: the User representation of the user you want to remove from the registery,
        """
        del self._users[user.username]

    @property
    def usernames(self) -> list[str]:
        """
        Provides a list of the usernames of all registered users.
        """
        return list(self._users)

    def get_users(self) -> dict[str, User]:
        """
        A mapping of the registered User object and their usernames.
        """
        return self._users

    def send_message_to_all_users(self, sender: SenderInterface, message: str) -> None:
        """
        Sends a message to all users separately via the injection SenderInterface implementation.

        :param sender: the SenderInterface implementation
        :param message: the message to send to all users in the registry
        """
        for user in self._users.values():
            sender.send(recipient_info=user, message=message)
