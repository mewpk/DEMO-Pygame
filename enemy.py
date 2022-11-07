import pygame
from random import randint

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos,screen_width,screen_height):
        super().__init__()
        self.screen_width, self.screen_height = screen_width , screen_height
        vec = pygame.math.Vector2
        run1 = pygame.image.load('graphics/sprites/enemy/dragon_down1.png').convert_alpha()
        run2 = pygame.image.load('graphics/sprites/enemy/dragon_down2.png').convert_alpha()
        run3 = pygame.image.load('graphics/sprites/enemy/dragon_down3.png').convert_alpha()
        run4 = pygame.image.load('graphics/sprites/enemy/dragon_down4.png').convert_alpha()
        # run5 = pygame.image.load('graphics/sprites/enemy/run/5.png').convert_alpha()
        # run6 = pygame.image.load('graphics/sprites/enemy/run/6.png').convert_alpha()
        # run7 = pygame.image.load('graphics/sprites/enemy/run/7.png').convert_alpha()
        # run8 = pygame.image.load('graphics/sprites/enemy/run/8.png').convert_alpha()
        self.run = [run1, run2, run3, run4]

        self.frame_index = 0
        self.image = self.run[self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.enemy_speed = 1
        self.vel = vec(0, 0)

    def running(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.run):
            self.frame_index = 0
        self.image = self.run[int(self.frame_index)]

    def constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top <= 20:
            self.rect.top = 20
        if self.rect.bottom >= self.screen_height:
            self.rect.bottom = self.screen_height
    
    def update(self):
        self.running()
        self.constraint()