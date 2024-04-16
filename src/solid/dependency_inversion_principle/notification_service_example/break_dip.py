class EmailService:
    def send_email(self, recipient, message):
        pass


class NotificationService:
    def __init__(self):
        self.email_service = EmailService()

    def send_notification(self, recipient, message):
        try:
            self.email_service.send_email(recipient, message)
        except Exception as e:
            print(f"Error sending notification to '{recipient}': {str(e)}")

# violates dip by directly coupling the high-level NotificationService class to the concrete low-level EmailService
# class, instead of depending on abstractions.
