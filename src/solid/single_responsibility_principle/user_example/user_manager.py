from user import User
from message_sender import SenderInterface


class UserManager:
    def __init__(self):
        self._users: dict[str, User] = {}

    def add_user(self, user: User):
        self._users[user.username] = user

    def remove_user(self, user: User):
        del self._users[user.username]

    @property
    def usernames(self):
        return list(self._users)

    def get_users(self):
        return self._users

    def send_message_to_all_users(self, sender: SenderInterface, message: str):
        for user in self._users.values():
            sender.send(recipient_info=user, message=message)
