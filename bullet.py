import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, player_wasd):
        super().__init__()
        
        self.player_wasd = player_wasd

        bullet = pygame.image.load("graphics/sprites/player/player_front1.png")
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