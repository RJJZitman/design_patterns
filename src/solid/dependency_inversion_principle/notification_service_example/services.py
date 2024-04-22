from abc import ABCMeta, abstractmethod


class NotificationService(metaclass=ABCMeta):
    """Interface for notification methods"""
    @abstractmethod
    def send_notification(self, recipient: any, message: str):
        pass


class EmailService(NotificationService):
    """Service to send emails"""
    def send_notification(self, recipient: str, message: str):
        # Implementation to send an email
        print(f"Email sent to '{recipient}': {message}")


class SMSService(NotificationService):
    """Service to send SMS messages"""
    def send_notification(self, recipient: str, message: str):
        # Implementation to send an SMS
        print(f"SMS sent to '{recipient}': {message}")


class PushNotificationService(NotificationService):
    """Service to send push notifications"""
    def send_notification(self, recipient: str, message: str):
        # Implementation to send a push notification
        print(f"Push notification sent to '{recipient}': {message}")
