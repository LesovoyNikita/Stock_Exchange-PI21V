class AdminPanel:
    def __init__(self):
        self.stats = {
            "active_users": 1500,
            "daily_volume": 100000.0
        }

    def get_stats(self) -> dict:
        return self.stats