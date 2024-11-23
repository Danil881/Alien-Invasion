import pygame.font

from settings import Settings

class Button_Play():
    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        #Назначение размеров и свойств кнопок.
        self.width, self.height = 170, 85
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 120)

        #Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.settings.screen_width / 2 - 80
        self.rect.y = self.settings.screen_height / 2
        self.rect_place = (self.rect.x, self.rect.y)

        #Сообщение кнопки создаеться только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect = self.rect_place

    def draw_button(self):
        #Отображает пустой кнопки и вывод сообщения.
        self.screen.blit(self.msg_image, self.msg_image_rect)

class Button_Settings():
    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        #Назначение размеров и свойств кнопок.
        self.width, self.height = 190, 53
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 70)

        #Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.settings.screen_width / 2 - 520
        self.rect.y = self.settings.screen_height / 2 + 20
        self.rect_place = (self.rect.x, self.rect.y)

        #Сообщение кнопки создаеться только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect = self.rect_place
        
    def draw_button(self):
        #Отображает пустой кнопки и вывод сообщения.
        self.screen.blit(self.msg_image, self.msg_image_rect)

    class Button_Settings_Back:
         def __init__(self, ai_game, msg):
             """Инициализирует атрибуты кнопки."""
             self.screen = ai_game.screen
             self.screen_rect = self.screen.get_rect()
             self.settings = Settings()

             #Назначение размеров и свойств кнопок.
             self.width, self.height = 120, 50
             self.button_color = (255, 255, 255)
             self.text_color = (0, 0, 0)
             self.font = pygame.font.SysFont(None, 80)

             #Построение объекта rect кнопки и выравнивание по центру экрана.
             self.rect = pygame.Rect(0, 0, self.width, self.height)
             self.rect.x = self.settings.screen_width / 2 - 550
             self.rect.y = self.settings.screen_height / 2 + 240
             self.rect_place = (self.rect.x, self.rect.y)

             #Сообщение кнопки создаеться только один раз.
             self._prep_msg(msg)

         def _prep_msg(self, msg):
             """Преобразует msg в прямоугольник и выравнивает текст по центру."""
             self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
             self.msg_image_rect = self.msg_image.get_rect()
             self.msg_image_rect = self.rect_place
        
         def draw_button(self):
             #Отображает пустой кнопки и вывод сообщения.
             self.screen.blit(self.msg_image, self.msg_image_rect)

class Buttons:
    class Language:
         def __init__(self, ai_game, msg):
             """Инициализирует атрибуты кнопки."""
             self.screen = ai_game.screen
             self.screen_rect = self.screen.get_rect()
             self.settings = Settings()

             #Назначение размеров и свойств кнопок.
             self.width, self.height = 120, 50
             self.button_color = (255, 255, 255)
             self.text_color = (0, 0, 0)
             self.font = pygame.font.SysFont(None, 60)

             #Построение объекта rect кнопки и выравнивание по центру экрана.
             self.rect = pygame.Rect(0, 0, self.width, self.height)
             self.rect.x = self.settings.screen_width / 2 - 53
             self.rect.y = self.settings.screen_height / 2 - 200
             self.rect_place = (self.rect.x, self.rect.y)

             #Сообщение кнопки создаеться только один раз.
             self._prep_msg(msg)

         def _prep_msg(self, msg):
             """Преобразует msg в прямоугольник и выравнивает текст по центру."""
             self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
             self.msg_image_rect = self.msg_image.get_rect()
             self.msg_image_rect = self.rect_place
        
         def draw_button(self):
             #Отображает пустой кнопки и вывод сообщения.
             self.screen.blit(self.msg_image, self.msg_image_rect)

class Exit:
    def __init__(self, ai_game, msg):
        """Инициализирует атрибуты кнопки."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = Settings()

        #Назначение размеров и свойств кнопок.
        self.width, self.height = 100, 55
        self.button_color = (255, 255, 255)
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 80)

        #Построение объекта rect кнопки и выравнивание по центру экрана.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.x = self.settings.screen_width / 2 + 410
        self.rect.y = self.settings.screen_height / 2 + 10
        self.rect_place = (self.rect.x, self.rect.y)

        #Сообщение кнопки создаеться только один раз.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Преобразует msg в прямоугольник и выравнивает текст по центру."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                     self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect = self.rect_place
        
    def draw_button(self):
             #Отображает пустой кнопки и вывод сообщения.
             self.screen.blit(self.msg_image, self.msg_image_rect)