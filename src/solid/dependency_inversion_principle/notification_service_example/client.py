from services import NotificationService


class NotificationServiceClient:
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def send_notification(self, recipient, message):
        try:
            self.notification_service.send_notification(recipient, message)
        except Exception as e:
            print(f"Error sending notification to '{recipient}': {str(e)}")
