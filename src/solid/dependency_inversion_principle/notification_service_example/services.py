from abc import ABCMeta, abstractmethod


class NotificationService(metaclass=ABCMeta):
    @abstractmethod
    def send_notification(self, recipient, message):
        pass


class EmailService(NotificationService):
    def send_notification(self, recipient, message):
        # Implementation to send an email
        print(f"Email sent to '{recipient}': {message}")


class SMSService(NotificationService):
    def send_notification(self, recipient, message):
        # Implementation to send an SMS
        print(f"SMS sent to '{recipient}': {message}")


class PushNotificationService(NotificationService):
    def send_notification(self, recipient, message):
        # Implementation to send a push notification
        print(f"Push notification sent to '{recipient}': {message}")
