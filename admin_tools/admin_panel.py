class AdminPanel:
    """Панель администратора для анализа статистики."""
    
    def __init__(self):
        """Инициализирует тестовые данные статистики."""
        self.stats = {
            "active_users": 1500,
            "daily_volume": 100000.0
        }

    def get_stats(self) -> dict:
        """Возвращает текущую статистику.
        
        Returns:
            dict: Статистика платформы.
        """
        return self.stats