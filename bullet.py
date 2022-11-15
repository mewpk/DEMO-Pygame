import pygame
import math
import random
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, player_wasd, bullet_type):
        super().__init__()
        self.player_wasd = player_wasd
        self.bullet_type = bullet_type
        if self.bullet_type == 0: # 0
            bullet = pygame.image.load("graphics/sprites/bullet/a.png").convert_alpha()
        elif self.bullet_type == 1: # 20
            bullet = pygame.image.load("graphics/sprites/bullet/b.png").convert_alpha()
        elif self.bullet_type == 2: # 100
            bullet = pygame.image.load("graphics/sprites/bullet/c.png").convert_alpha()
        elif self.bullet_type == 3: # 500
            bullet = pygame.image.load("graphics/sprites/bullet/d.png").convert_alpha()
        elif self.bullet_type == 4: # 1000
            bullet = pygame.image.load("graphics/sprites/bullet/e.png").convert_alpha()
        elif self.bullet_type == 5: # 5000
            number = random.randrange(1,9)
            if number == 1 :
                bullet = pygame.image.load("graphics/sprites/bullet/d1.png").convert_alpha()
            elif number == 2:
                bullet = pygame.image.load("graphics/sprites/bullet/d2.png").convert_alpha()
            elif number == 3 :
                bullet = pygame.image.load("graphics/sprites/bullet/d3.png").convert_alpha()
            elif number == 4 :
                bullet = pygame.image.load("graphics/sprites/bullet/d4.png").convert_alpha()
            elif number == 5 :
                bullet = pygame.image.load("graphics/sprites/bullet/d5.png").convert_alpha()
            elif number == 6 :
                bullet = pygame.image.load("graphics/sprites/bullet/d6.png").convert_alpha()
            elif number == 7 :
                bullet = pygame.image.load("graphics/sprites/bullet/d7.png").convert_alpha()
            elif number == 8 :
                bullet = pygame.image.load("graphics/sprites/bullet/d8.png").convert_alpha()
        self.image = bullet
        self.rect = self.image.get_rect(center = pos)
        self.bullet_speed = 10
    def moving(self):
        if self.player_wasd == 'w':
            self.rect.y -= self.bullet_speed
        elif self.player_wasd == 'a':
            self.rect.x -= self.bullet_speed
        elif self.player_wasd == 's':
            self.rect.y += self.bullet_speed
        elif self.player_wasd == 'd':
            self.rect.x += self.bullet_speed
    def constraint(self):
        if self.rect.left <= 0:
            self.kill()
        elif self.rect.right >= self.screen_width:
            self.kill()
        if self.rect.top <= 0:
            self.kill()
        elif self.rect.bottom >= self.screen_height:
            self.kill()
    def update(self):
        self.moving()
        # print(self.bullet_type)