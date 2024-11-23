import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invansion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        
        #Параметры экрана
        self.screen_width = 1366
        self.screen_height = 768
        self.bg_color = (0, 0, 0)

        #Параметр меню экрана
        self.mbg_color = (0, 0, 0)
        self.sbg_color = (25, 25, 112)

        #Настройки корабля
        self.ship_limit = 2

        #Параметри снаряда
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 3

        #Настройка пришельцев
        self.fleet_drop_speed = 10

        #Темп ускорения игры
        self.speedup_scale = 1.04
        #Темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed_factor = 0.8
        self.bullet_speed_factor = 0.6
        self.alien_speed_factor = 0.4

        #fleet_direcrion = 1 обозначает движение вправо; a -1 - влево
        self.fleet_direction = 1

        #Подсчет очков
        self.alien_points = 10

    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)