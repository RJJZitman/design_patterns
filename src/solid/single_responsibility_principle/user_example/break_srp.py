class User:
    def __init__(self, username: str, email: str, phone_number: str):
        self.username = username
        self.email = email
        self.phone_number = phone_number

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_phone_number(self):
        return self.phone_number

    # break SRP by using the User class to both create users and contact them
    def send_email(self, message: str):
        print(f"Sending email to {self.username} at address {self.email}: {message}")

    def send_sms(self, message: str):
        print(f"Sending SMS to {self.phone_number}: {message}")

