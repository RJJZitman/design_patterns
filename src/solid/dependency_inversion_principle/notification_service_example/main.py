from client import NotificationServiceClient
from services import EmailService, SMSService, PushNotificationService


if __name__ == "__main__":
    email_service = EmailService()
    sms_service = SMSService()
    push_notification_service = PushNotificationService()

    client_email = NotificationServiceClient(email_service)
    client_sms = NotificationServiceClient(sms_service)
    client_push_notification = NotificationServiceClient(push_notification_service)

    client_email.send_notification("user@example.com", "Hello via email!")
    client_sms.send_notification("123456789", "Hello via SMS!")
    client_push_notification.send_notification("user", "Hello via push notification!")
