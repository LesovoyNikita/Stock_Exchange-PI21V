from passlib.hash import pbkdf2_sha256

class UserManager:
    """Регистрация и аутентификация пользователей."""
    
    def __init__(self):
        """Инициализирует пустой словарь пользователей."""
        self.users = {}

    def register_user(self, email: str, password: str) -> None:
        """Регистрирует нового пользователя.
        
        Args:
            email (str): Email пользователя.
            password (str): Пароль в открытом виде.
        """
        hashed_password = pbkdf2_sha256.hash(password)
        self.users[email] = hashed_password

    def verify_user(self, email: str, password: str) -> bool:
        """Проверяет пароль пользователя.
        
        Args:
            email (str): Email пользователя.
            password (str): Пароль для проверки.
            
        Returns:
            bool: True, если пароль верен.
        """
        return pbkdf2_sha256.verify(password, self.users.get(email, ""))