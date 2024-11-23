import pygame

from settings import Settings

class Ukraine():
             def __init__(self, ai_game):
                 """Инициализирует атрибуты кнопки."""
                 self.screen = ai_game.screen
                 self.screen_rect = self.screen.get_rect()
                 self.settings = Settings()

                 #Загрузка изображение пришельца и назначение атрибута rect.
                 self.image = pygame.image.load("image/Ukraine.bmp")
                 self.rect = self.image.get_rect()

                 #Задает кординаты флага
                 self.rect.x = self.settings.screen_width / 2 + 160
                 self.rect.y = self.settings.screen_height / 2
                 self.rect_place = (self.rect.x, self.rect.y)
        
             def draw_button(self):
                 #Отображает пустой кнопки и вывод сообщения.
                 self.screen.blit(self.image, self.rect_place)

class English():
             def __init__(self, ai_game):
                 """Инициализирует атрибуты кнопки."""
                 self.screen = ai_game.screen
                 self.screen_rect = self.screen.get_rect()
                 self.settings = Settings()

                 #Загрузка изображение пришельца и назначение атрибута rect.
                 self.image = pygame.image.load("image/USA.bmp")
                 self.rect = self.image.get_rect()

                 #Задает кординаты флага
                 self.rect.x = self.settings.screen_width / 2 - 230
                 self.rect.y = self.settings.screen_height / 2
                 self.rect_place = (self.rect.x, self.rect.y)
        
             def draw_button(self):
                 #Отображает пустой кнопки и вывод сообщения.
                 self.screen.blit(self.image, self.rect_place)