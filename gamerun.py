import random
import sys
from random import choice, randint

import pygame

from enemy import Enemy
from enemy2 import Enemy2
from enemy3 import Enemy3
from player import Player


def display_text(text, size, color, pos, screen):
    font = pygame.font.Font('graphics/font/PressStart2P-vaV7.ttf', size)
    text_surf = font.render(f'{text}', False, color)
    text_rect = text_surf.get_rect(center=pos)
    screen.blit(text_surf, text_rect)


class Gamerun():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        # bullet
        self.bullet_type = 0

        # player
        player_sprite = Player(self.screen_width, self.screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.life = 10
        self.lifebox = pygame.Surface((20, 20))
        self.lifebox.fill('red')
        self.life_bg = pygame.Surface((200, 20))
        self.life_bg.fill('black')
        self.game_status = 1

        # sound
        self.hit = pygame.mixer.Sound("graphics/music/hit.mp3")
        self.hit.set_volume(2)

        # money
        self.money = 0
        self.score = 0
        self.money_upgrade_bullet = [2000, 3000, 4000, 5000, 10000, "MAX"]
        # self.money_upgrade_bullet = [, 1, 2, 1, 2, 'max']
        self.money_upgrade_bullet_i = 0

        # enemy
        self.enemy_sprite = Enemy((choice([0, self.screen_width]), randint(
            0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect)
        self.enemy = pygame.sprite.Group(self.enemy_sprite)
        self.enemy_adding_time = 150
        self.enemy_kill = 0
        # button
        self.button_money = pygame.Rect(
            (self.screen_width - 160, 80), (100, 40))

    def enemy_move(self):
        for enemy in self.enemy:

            x = choice((0, 1))
            if x == 0:
                if enemy.rect.x > self.player.sprite.rect.x:
                    enemy.rect.x -= 1
                elif enemy.rect.x < self.player.sprite.rect.x:
                    enemy.rect.x += 1
            elif x == 1:
                if enemy.rect.y > self.player.sprite.rect.y:
                    enemy.rect.y -= 1
                elif enemy.rect.y < self.player.sprite.rect.y:
                    enemy.rect.y += 1

    def add_enemy(self):
        self.enemy_adding_time -= 1
        if self.enemy_adding_time <= 0:
            x_or_y = random.randrange(1, 7)
            if x_or_y == 1:
                self.enemy.add(Enemy((choice([0, self.screen_width]), randint(
                    0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
            elif x_or_y == 2:
                self.enemy.add(Enemy((randint(0, self.screen_width), choice(
                    [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
            elif x_or_y == 3:
                self.enemy.add(Enemy2((choice([0, self.screen_width]), randint(
                    0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
            elif x_or_y == 4:
                self.enemy.add(Enemy2((randint(0, self.screen_width), choice(
                    [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
            elif x_or_y == 5:
                self.enemy.add(Enemy3((choice([0, self.screen_width]), randint(
                    0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
            elif x_or_y == 6:
                self.enemy.add(Enemy3((randint(0, self.screen_width), choice(
                    [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
            if self.bullet_type == 5:
                self.enemy_adding_time = 10
                if random.randrange(0, 3) == 0:
                    for i in range(1, 5):
                        x_or_y = random.randrange(1, 7)
                        if x_or_y == 1:
                            self.enemy.add(Enemy((choice([0, self.screen_width]), randint(
                                0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
                        elif x_or_y == 2:
                            self.enemy.add(Enemy((randint(0, self.screen_width), choice(
                                [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
                        elif x_or_y == 3:
                            self.enemy.add(Enemy2((choice([0, self.screen_width]), randint(
                                0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
                        elif x_or_y == 4:
                            self.enemy.add(Enemy2((randint(0, self.screen_width), choice(
                                [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
                        elif x_or_y == 5:
                            self.enemy.add(Enemy3((choice([0, self.screen_width]), randint(
                                0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
                        elif x_or_y == 6:
                            self.enemy.add(Enemy3((randint(0, self.screen_width), choice(
                                [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
            elif self.score >= 100000:
                self.enemy_adding_time = 30
            elif self.score >= 80000:
                self.enemy_adding_time = 40
            elif self.score >= 60000:
                self.enemy_adding_time = 60
            elif self.score >= 40000:
                self.enemy_adding_time = 80
            elif self.score >= 30000:
                self.enemy_adding_time = 90
            elif self.score >= 20000:
                self.enemy_adding_time = 100
            elif self.score >= 10000:
                self.enemy_adding_time = 120
            elif self.score >= 0:
                self.enemy_adding_time = 130

            if random.randrange(0, 5) == 0:
                for i in range(1, 7):
                    x_or_y = random.randrange(1, 5)
                    if x_or_y == 1:
                        self.enemy.add(Enemy((choice([0, self.screen_width]), randint(
                            0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
                    elif x_or_y == 2:
                        self.enemy.add(Enemy((randint(0, self.screen_width), choice(
                            [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
                    elif x_or_y == 3:
                        self.enemy.add(Enemy2((choice([0, self.screen_width]), randint(
                            0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
                    elif x_or_y == 4:
                        self.enemy.add(Enemy2((randint(0, self.screen_width), choice(
                            [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))
                    elif x_or_y == 5:
                        self.enemy.add(Enemy3((choice([0, self.screen_width]), randint(
                            0, self.screen_height)), self.screen_width, self.screen_height, self.player.sprite.rect))
                    elif x_or_y == 6:
                        self.enemy.add(Enemy3((randint(0, self.screen_width), choice(
                            [0, self.screen_height])), self.screen_width, self.screen_height, self.player.sprite.rect))

    def display_money(self):
        display_text(f'Money :{self.money} $', 20, 'black',
                     (self.screen_width - 200, 50), self.screen)

    def display_score(self):
        display_text(f'Score :{self.score}', 20, 'black',
                     (self.screen_width/2, 50), self.screen)

    def display_hp(self):
        if self.game_status == 1:
            self.screen.blit(self.life_bg, (50, 40))
            for each_life in range(self.life):
                x = 50 + (each_life * (self.lifebox.get_size()[0]))
                self.screen.blit(self.lifebox, (x, 40))

    def collision(self):
        if self.enemy:
            for enemy in self.enemy:
                if pygame.sprite.spritecollide(enemy, self.player, False):
                    enemy.kill()
                    self.life -= 1
                    if self.life <= 0 :
                        self.game_status = 0


        if self.player.sprite.bullet:
            for bullet in self.player.sprite.bullet:
                if pygame.sprite.spritecollide(bullet, self.enemy, True):
                    pygame.mixer.Sound.play(self.hit)
                    bullet.kill()
                    self.money += random.randrange(5, 70) + self.enemy_kill
                    self.score += random.randrange(500, 1000,100)
                    self.enemy_kill += 1

    # button
    def display_button(self):
        pygame.draw.rect(self.screen, ('black'), self.button_money)
        display_text(f'{self.money_upgrade_bullet[self.money_upgrade_bullet_i]}$', 18, 'white', (
            self.screen_width - 110, 100), self.screen)

    def get_mouse_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.button_money.collidepoint((mx, my)):
                    if self.money_upgrade_bullet_i <= 4:
                        if self.money >= self.money_upgrade_bullet[self.money_upgrade_bullet_i]:
                            self.money -= self.money_upgrade_bullet[self.money_upgrade_bullet_i]

                            self.player.sprite.bullet_type += 1
                            if self.player.sprite.bullet_type > 5:
                                self.player.sprite.bullet_type = 5

                            self.money_upgrade_bullet_i += 1
# 20 100 500 1000 5000

    def run(self):
        self.screen.fill("white")

        self.player.draw(self.screen)
        self.player.update()
        self.player.sprite.bullet.draw(self.screen)

        self.add_enemy()
        self.enemy.draw(self.screen)
        self.enemy.update()
        self.enemy_move()

        self.display_money()
        self.display_score()
        self.display_hp()

        self.display_button()
        self.get_mouse_input()

        self.collision()
