from abc import ABCMeta, abstractmethod

from user import User


class SenderInterface(metaclass=ABCMeta):
    """
    Interface to send messages. Each implementation should represent a new communication medium.
    """
    @abstractmethod
    def send(self, recipient_info: User, message: str):
        pass


class EmailSender(SenderInterface):
    """
    This class provides the shell for an email oriented implementation of the SenderInterface. The actual logic of
    sending emails is not implemented, instead a message suggesting the email is being sent is presented.
    """
    def __init__(self, *args, **kwargs):
        ...

    def send(self, recipient_info: User, message: str) -> None:
        """
        Sends the email message to a provided recipient.

        :param recipient_info: A user instance containing all info needed to send the email to the user.
        :param message: the actual email
        """
        print(f"Sending email to {recipient_info.username} at address {recipient_info.email}: {message}")
    # implement email sending logic here


class SMSSender(SenderInterface):
    """
    This class provides the shell for an sms oriented implementation of the SenderInterface. The actual logic of
    sending messages via sms is not implemented, instead a message suggesting the sms is being sent is presented.
    """
    def __init__(self, *args, **kwargs):
        ...

    def send(self, recipient_info: User, message: str) -> None:
        """
        Sends the sms message to a provided recipient.

        :param recipient_info: A user instance containing all info needed to send the sms to the user.
        :param message: the actual sms
        """
        print(f"Sending SMS to {recipient_info.phone_number}: {message}")
    # implement SMS sending logic here

# other sender implementations can be added similarly
