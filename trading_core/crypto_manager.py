import os

class CryptoManager:
    @staticmethod
    def generate_wallet() -> str:
        return "0x" + os.urandom(20).hex()