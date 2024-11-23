from game_stats import GameStats
import json

class Language:
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.stats = GameStats(self)

    def language(self, is_ukr = False):
            if not self.stats.game_active:
                if is_ukr:
                      self.ln_list = ["Грати", "Налаштування", "Мова", "Повернутися", "Вихід"]
                else:
                      self.ln_list = ["Play", "Settings", "Language", "Back", "Exit"]