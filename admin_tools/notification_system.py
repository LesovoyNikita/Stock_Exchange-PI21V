class NotificationSystem:
    def send_sms(self, phone: str, message: str):
        print(f"SMS to {phone}: {message}")

    def send_email(self, email: str, subject: str, body: str):
        print(f"Email to {email}:\nSubject: {subject}\nBody: {body}")