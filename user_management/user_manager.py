from passlib.hash import pbkdf2_sha256

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, email: str, password: str):
        hashed_password = pbkdf2_sha256.hash(password)
        self.users[email] = hashed_password

    def verify_user(self, email: str, password: str) -> bool:
        return pbkdf2_sha256.verify(password, self.users.get(email, ""))