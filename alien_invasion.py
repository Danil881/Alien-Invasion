import sys
from time import sleep
import pygame
import json

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from Language import Language
import image_button
import button_usa
import button_ukr
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvansion:
    """Класс для упраления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = 1366
        self.settings.screen_height = 768
        pygame.display.set_caption("Alien Invasion")

        #Создание экземпляра для хранения игровой статистики.
        #и панели результатов
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        ln = Language(self)
        ln.language(is_ukr = False)
        ln_l = ln.ln_list

        #Создание кнопок.
        self.play_button = button_usa.Button_Play(self, ln_l[0])
        self.settings_button = button_usa.Button_Settings(self, ln_l[1])
        self.settings_language_button = button_usa.Buttons.Language(self, ln_l[2])
        self.settings_button_back = button_usa.Button_Settings.Button_Settings_Back(self, ln_l[3])
        self.settings_button_exit = button_usa.Exit(self, ln_l[4])

        #Создание картинок_кнопок
        self.settings_language_picture_ukr = image_button.Ukraine(self)
        self.settings_language_picture_usa = image_button.English(self)

        Fleets._create_fleet(self)

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                Bullets._update_bullets(self)
                Aliens._update_aliens(self)

            self._update_screen()
      
    def _check_events(self):
        """Обрабатывает нажатие клавиш и события мыши."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     Mouse_Keyboard._check_keydown_events(self, event)
                elif event.type == pygame.KEYUP:
                     Mouse_Keyboard._check_keyup_events(self, event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                      mouse_pos = pygame.mouse.get_pos()
                      self._check_play_button(mouse_pos)

                      #для Настроек
                      mouse_pos_s = pygame.mouse.get_pos()
                      self._check_setting_button(mouse_pos_s)
                      #для Возвращение из настроек
                      mouse_pos_s_b = pygame.mouse.get_pos()
                      self._check_setting_button_back(mouse_pos_s_b)

                      #для Выхода из игры
                      mose_pos_exit = pygame.mouse.get_pos()
                      self._check_settings_button_exit(mose_pos_exit)

                      #Для укр языка
                      mouse_pos_s_l_ukr = pygame.mouse.get_pos()
                      self._check_setting_button_ukr(mouse_pos_s_l_ukr)
                      self.check_language = True
                      #Для англ языка
                      mouse_pos_s_l_usa = pygame.mouse.get_pos()
                      self._check_settings_button_usa(mouse_pos_s_l_usa)
                      self.check_language = False

    def _check_play_button(self, mouse_pos):
          """Запускает новую игру при нажатии кнопки Play."""
          if self.stats.game_active_s == False:
                button_clicked = self.play_button.rect.collidepoint(mouse_pos)
                if button_clicked and not self.stats.game_active:
                       #Сброс игровых настроек.
                       self.settings.initialize_dynamic_settings()

                       #Сброс игровой статистики.
                       self.stats.reset_stats()
                       self.stats.game_active = True
                       self.sb.prep_score()
                       self.sb.prep_level()
                       self.sb.prep_ships()

                       #Очистка списков пришельцев и снарядов.
                       self.aliens.empty()
                       self.bullets.empty()

                       #Создание нового флота и размещение корабля в центре.
                       Fleets._create_fleet(self)
                       self.ship.center_ship()

                       #Указатель мыши скрывается.
                       pygame.mouse.set_visible(False)

    def _check_setting_button(self, mouse_pos_s):
          """Работа с кнопкой Settings"""
          button_clicked_s = self.settings_button.rect.collidepoint(mouse_pos_s)
          if button_clicked_s and not self.stats.game_active:
               self.stats.game_active_s = True
    
    def _check_setting_button_back(self, mouse_pos_s_b):
          """Работа с кнопкой назад в настройках"""
          button_clicked_s_b = self.settings_button_back.rect.collidepoint(mouse_pos_s_b)
          if button_clicked_s_b and not self.stats.game_active:
               self.stats.game_active_s = False

    def _check_setting_button_ukr(self, mouse_pos_s_l_ukr):
          """Изменение языка на украинский"""
          button_clicked_s_l = self.settings_language_picture_ukr.rect.collidepoint(mouse_pos_s_l_ukr)
          if button_clicked_s_l and not self.stats.game_active and self.stats.game_active_s:
                ln = Language(self)
                ln.language(is_ukr = True)
                ln_l = ln.ln_list

                self.play_button = button_ukr.Button_Play(self, ln_l[0])
                self.settings_button = button_ukr.Button_Settings(self, ln_l[1])
                self.settings_language_button = button_ukr.Buttons.Language(self, ln_l[2])
                self.settings_button_back = button_ukr.Button_Settings.Button_Settings_Back(self, ln_l[3])
                self.settings_button_exit = button_ukr.Exit(self, ln_l[4])

    def _check_settings_button_usa(self, mouse_pos_s_l_usa):
          """Изменение языка на английський"""
          button_clicked_s_l = self.settings_language_picture_usa.rect.collidepoint(mouse_pos_s_l_usa)
          if button_clicked_s_l and not self.stats.game_active and self.stats.game_active_s:
                ln = Language(self)
                ln.language(is_ukr = False)
                ln_l = ln.ln_list

                self.play_button = button_usa.Button_Play(self, ln_l[0])
                self.settings_button = button_usa.Button_Settings(self, ln_l[1])
                self.settings_language_button = button_usa.Buttons.Language(self, ln_l[2])
                self.settings_button_back = button_usa.Button_Settings.Button_Settings_Back(self, ln_l[3])
                self.settings_button_exit = button_usa.Exit(self, ln_l[4])

    def _check_settings_button_exit(self, mouse_pos_exit):
         """Работа с кнопкой Exit"""
         button_clicked_exit= self.settings_button_exit.rect.collidepoint(mouse_pos_exit)
         if button_clicked_exit and not self.stats.game_active and not self.stats.game_active_s:
               Save.save_high_score(self)
               sys.exit()

    def _update_screen(self):
         """Обновляет изображение на экране и отображает новый экран."""
         if not self.stats.game_active:
                if self.stats.game_active_s:
                     Settings_s.settings_s(self)
                else:
                     Menu.menu(self)
         else:
               Game.game(self)


class Aliens:
      """Класс для работы с пришельцами"""
      def _create_alien(self, alien_number, row_number):
           """Создание пришельца и размещение его в ряду."""
           #Создание пришельца и розмещение его в ряду.
           alien = Alien(self)
           alien_width, alien_height = alien.rect.size
           alien_width = alien.rect.width
           alien.x = alien_width + 2 * alien_width * alien_number
           alien.rect.x = alien.x
           alien.rect.y = alien.rect.h + alien.rect.h + 2 * alien.rect.height * row_number
           self.aliens.add(alien)

      def _update_aliens(self):
          """Обновляет позиции всех пришельцув во флоте."""
          Fleets._check_fleet_edges(self)
          self.aliens.update()

          if pygame.sprite.spritecollideany(self.ship, self.aliens):
                Damage._ship_hit(self)

          #Проверить, добрались ли пришельцы до ниженго края экрана.
          Aliens._check_aliens_bottom(self)

      def _check_aliens_bottom(self):
          """Проверяет, добрались ли пришельцы до нижнего края экрана."""
          screen_rect = self.screen.get_rect()
          for alien in self.aliens.sprites():
                if alien.rect.bottom >= screen_rect.bottom:
                      #Происходит то же, что при столкновении с кораблем.
                      Damage._ship_hit(self)
                      break
                          
class Fleets:
      """Класс для работы с флотом"""
      def _create_fleet(self):
           """Создание флота вторжения."""
           #Создание пришельца и вычисление количества пришельцев в ряду
           #Интервал между соседними пришельцами равен ширине пришельца.
           alien = Alien(self)
           alien_width, alien_height = alien.rect.size
           available_space_x = self.settings.screen_width - (2 * alien_width)
           number_aliens_x = available_space_x // (2 * alien_width)

           #Определение количества рядов, помещающихся на экране
           ship_height = self.ship.rect.height
           available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
           number_rows = available_space_y // (2 * alien_height)

           #Создание флота вторжения.
           for row_number in range(number_rows):
                for alien_number in range(number_aliens_x):
                    Aliens._create_alien(self, alien_number, row_number)
      
      def _change_fleet_direction(self):
          """Опускает весь флот и меняет направление флота."""
          for alien in self.aliens.sprites(): 
                alien.rect.y += self.settings.fleet_drop_speed
          self.settings.fleet_direction *= -1

      def _check_fleet_edges(self):
          """Реагирует на достижение пришельцем края экрана."""
          for alien in self.aliens.sprites():
                if alien.check_edges():
                    Fleets._change_fleet_direction(self)
                    break
                
class Bullets:
      """Класс для работы с пулями"""
      def _fire_bullet(self):
            """Создание нового снаряда и включение его в группу bullets."""
            if len(self.bullets) < self.settings.bullets_allowed:
             new_bullet = Bullet(self)
             self.bullets.add(new_bullet)
      
      def _update_bullets(self):
           """Обновление позиции снарядов и уничтожение старых снарядов"""
           self.bullets.update()
           
           #Удаление снарядов, вышедших за край экрана.
           for bullet in self.bullets.copy():
                  if bullet.rect.bottom <= 0:
                         self.bullets.remove(bullet)
            
           Damage._check_bullet_alien_collision(self)

class Damage:
      """Класс для обработки урона"""
      def _ship_hit(self):
          """Обрабатывает столкновение корабля с пришельцем."""
          if self.stats.ships_left >0:
                #Уменьшение ships_left и обновление панели счета
                self.stats.ships_left -= 1
                self.sb.prep_ships()

                #Очистка списка пришелцеви снарядов.
                self.aliens.empty()
                self.bullets.empty()

                #Создание нового флота и размещение корабля в центре.
                Fleets._create_fleet(self)
                self.ship.center_ship()

                #Пауза.
                sleep(0.5)
          else:
                self.stats.game_active = False
                pygame.mouse.set_visible(True)

      def _check_bullet_alien_collision(self):
          """Обработка коллизий снрядов с пришельцами."""
          #Удаление снарядов и пришельцев, участвующих в колизиях.
          collisions = pygame.sprite.groupcollide(
                        self.bullets, self.aliens, True, True)
          
          if collisions:
                for aliens in collisions.values():
                      self.stats.score += self.settings.alien_points * len(aliens)
                self.sb.prep_score() 
                self.sb.check_high_score()
           
          if not self.aliens:
                 #Уничтожение существующих снарядов и создание нового флота.
                 self.bullets.empty()
                 Fleets._create_fleet(self)
                 self.settings.increase_speed()

                 #Увиличение уровня.
                 self.stats.level += 1
                 self.sb.prep_level()

class Mouse_Keyboard:
      """Класс для обработки мыши и клавиатуры"""
      def _check_keydown_events(self, event):
         """Реагирует на нажатие клавиш."""
         if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
         elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
         elif event.key == pygame.K_ESCAPE:
               self.stats.game_active = False
               pygame.mouse.set_visible(True)
         elif event.key == pygame.K_SPACE:
                  Bullets._fire_bullet(self)

      def _check_keyup_events(self, event):
         """Реагирует на отпускание клавиш."""
         if event.key == pygame.K_RIGHT:
                          self.ship.moving_right = False
         elif event.key == pygame.K_LEFT:
                          self.ship.moving_left = False

class Menu:
      """Класс для отображения меню"""
      def menu(self):
            self.background_image = pygame.image.load("image/front.bmp")
            self.screen.blit(self.background_image, (0, 0))

            Save.load_high_score(self)
            self.sb.prep_score() 
            self.sb.check_high_score()

            self.sb.show_high_score()
            
            self.play_button.draw_button()
            self.settings_button.draw_button()
            self.settings_button_exit.draw_button()

            pygame.display.flip()

class Settings_s:
      """Класс для отображения настроек"""
      def settings_s(self):
            self.background_image = pygame.image.load("image/front.bmp")
            self.screen.blit(self.background_image, (0, 0))

            self.settings_button_back.draw_button()
            self.settings_language_button.draw_button()

            #Отображает кнопки картинки
            self.settings_language_picture_ukr.draw_button()
            self.settings_language_picture_usa.draw_button()

            pygame.display.flip()

class Game:
      """Класс для отображения игры"""
      def game(self):
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            for bullet in self.bullets.sprites():
                  bullet.draw_bullet()
            self.aliens.draw(self.screen)

            #Вывод информации о счете.
            self.sb.show_score()

            #Отображение после него прорисованого экрана.
            pygame.display.flip()

class Save:
      """Класс для работы с сохранениями"""
      def save_high_score(self):
            """Сохранение рекорда"""
            save_way = "save/save.json"
            try:
                  with open(save_way, "r") as file_s:
                        score = json.load(file_s)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                  score = 0
            
            if self.stats.score > score:
                  with open(save_way, "w") as file:
                        json.dump(self.stats.score, file)

      def load_high_score(self):
            """Загрузка рекорда"""
            try:
                  save_way = "save/save.json"
                  with open(save_way, "r") as file:
                        self.stats.score = json.load(file)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                  return 0

if __name__ == "__main__":
    #Создание экземпляра и запуск игры.
    ai = AlienInvansion()
    ai.run_game()