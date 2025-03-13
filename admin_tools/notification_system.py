class NotificationSystem:
    """Отправка уведомлений пользователям."""
    
    def send_sms(self, phone: str, message: str) -> None:
        """Отправляет SMS.
        
        Args:
            phone (str): Номер телефона.
            message (str): Текст сообщения.
        """
        print(f"SMS to {phone}: {message}")

    def send_email(self, email: str, subject: str, body: str) -> None:
        """Отправляет email.
        
        Args:
            email (str): Адрес электронной почты.
            subject (str): Тема письма.
            body (str): Текст письма.
        """
        print(f"Email to {email}:\nSubject: {subject}\nBody: {body}")