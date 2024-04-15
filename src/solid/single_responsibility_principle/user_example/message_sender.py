from abc import ABCMeta, abstractmethod

from user import User


class SenderInterface(metaclass=ABCMeta):
    @abstractmethod
    def send(self, recipient_info: User, message: str):
        pass


class EmailSender(SenderInterface):
    def __init__(self, *args, **kwargs):
        ...

    def send(self, recipient_info: User, message: str):
        print(f"Sending email to {recipient_info.username} at address {recipient_info.email}: {message}")
    # implement email sending logic here


class SMSSender(SenderInterface):
    def __init__(self, *args, **kwargs):
        ...

    def send(self, recipient_info: User, message: str):
        print(f"Sending SMS to {recipient_info.phone_number}: {message}")
    # implement SMS sending logic here

# other sender implementations can be added similarly
