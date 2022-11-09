import pygame
from random import randint, choice
from player import Player
from enemy import Enemy

class Gamerun():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        #player
        player_sprite = Player(self.screen_width, self.screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        self.score = 0
        self.life = 10
        
        # enemy
        self.enemy_sprite = Enemy((choice([0, self.screen_width]), randint(0, self.screen_height)),self.screen_width, self.screen_height, self.player.sprite.rect)
        self.enemy = pygame.sprite.Group(self.enemy_sprite)
        self.enemy_adding_time = randint(200, 300)

    def enemy_move(self):
        for enemy in self.enemy:
            if enemy.rect.x > self.player.sprite.rect.x:
                # if enemy.rect.y >=  self.player.sprite.rect.y:
                enemy.rect.x -= 1
            elif enemy.rect.x < self.player.sprite.rect.x:
                enemy.rect.x += 1
                
            if enemy.rect.y > self.player.sprite.rect.y:
                enemy.rect.y -= 1
            elif enemy.rect.y < self.player.sprite.rect.y:
                enemy.rect.y += 1
    def add_enemy(self):
        self.enemy_adding_time -= 1
        if self.enemy_adding_time <= 0:
            self.enemy.add(Enemy((choice([0, self.screen_width]), randint(0, self.screen_height)),self.screen_width, self.screen_height, self.player.sprite.rect))
            self.enemy.add(Enemy((randint(0, self.screen_width), choice([0, self.screen_height])),self.screen_width, self.screen_height, self.player.sprite.rect))
            self.enemy_adding_time = randint(200,300)
            # self.get_enemy_adding_time_new()
            # self.enemy_adding_time_new  = randint(80, 180)
            # self.enemy_adding_time = self.enemy_adding_time_new

    def collision(self):
        if self.enemy:
            for enemy in self.enemy:
                if pygame.sprite.spritecollide(enemy, self.player, False):
                    enemy.kill()
                    self.life -= 1
        
        if self.player.sprite.bullet:
            for bullet in self.player.sprite.bullet:
                if pygame.sprite.spritecollide(bullet, self.enemy, True):
                    bullet.kill()
                    self.score += 1

    def run(self):
        self.screen.fill("white")

        self.player.draw(self.screen)
        self.player.update()
        self.player.sprite.bullet.draw(self.screen)

        self.add_enemy()
        self.enemy.draw(self.screen)
        self.enemy.update()
        self.enemy_move()

        self.collision()