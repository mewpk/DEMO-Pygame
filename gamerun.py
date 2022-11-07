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
        
        # enemy
        self.random_x = choice([0, 600])
        self.random_y = randint(30,370)
        enemy_sprite = Enemy((self.random_x, self.random_y),self.screen_width, self.screen_height)
        self.enemy = pygame.sprite.Group(enemy_sprite)
        self.enemy_adding_time = 100

    def enemy_move(self):
        for enemy in self.enemy:
            if enemy.rect.x >= self.player.sprite.rect.x:
                enemy.rect.x -= 1
            if enemy.rect.x < self.player.sprite.rect.x:
                enemy.rect.x += 1
            if enemy.rect.y >= self.player.sprite.rect.y:
                enemy.rect.y -= 1
            if enemy.rect.y < self.player.sprite.rect.y:
                enemy.rect.y += 1
    def add_enemy(self):
        self.enemy_adding_time -= 1
        if self.enemy_adding_time <= 0:
            self.enemy.add(Enemy((choice([-70, 650]), randint(70,300))))
            self.get_enemy_adding_time_new()
            self.enemy_adding_time_new  = randint(80, 180)
            self.enemy_adding_time = self.enemy_adding_time_new
    def run(self):
        self.screen.fill("white")
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        self.player.update()
        self.enemy.update()
        self.enemy_move()