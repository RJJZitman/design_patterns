from services import NotificationService


class NotificationServiceClient:
    """Notification client. Should only have a single instance per NotificationService implementation"""
    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def send_notification(self, recipient: any, message: str):
        """Send the notification through the notification_service"""
        try:
            self.notification_service.send_notification(recipient, message)
        except Exception as e:
            print(f"Error sending notification to '{recipient}': {str(e)}")
