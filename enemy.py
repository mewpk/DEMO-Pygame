import pygame
from random import randint
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos,screen_width,screen_height, player_pos):
        super().__init__()
        self.screen_width, self.screen_height = screen_width , screen_height
        #player
        self.player_pos = player_pos

        vec = pygame.math.Vector2
        dragongold_down1 = pygame.image.load('graphics/sprites/enemy/dragon_down1.png').convert_alpha()
        dragongold_down2 = pygame.image.load('graphics/sprites/enemy/dragon_down2.png').convert_alpha()
        dragongold_down3 = pygame.image.load('graphics/sprites/enemy/dragon_down3.png').convert_alpha()
        dragongold_down4 = pygame.image.load('graphics/sprites/enemy/dragon_down4.png').convert_alpha()
        dragongold_down1 = pygame.transform.scale(dragongold_down1, (50, 50))
        dragongold_down2 = pygame.transform.scale(dragongold_down2, (50, 50))
        dragongold_down3 = pygame.transform.scale(dragongold_down3, (50, 50))
        dragongold_down4 = pygame.transform.scale(dragongold_down4, (50, 50))
        self.dragongold_down = [dragongold_down1, dragongold_down2, dragongold_down3, dragongold_down4]

        dragongold_up1 = pygame.image.load('graphics/sprites/enemy/dragon_up1.png').convert_alpha()
        dragongold_up2 = pygame.image.load('graphics/sprites/enemy/dragon_up2.png').convert_alpha()
        dragongold_up3 = pygame.image.load('graphics/sprites/enemy/dragon_up3.png').convert_alpha()
        dragongold_up4 = pygame.image.load('graphics/sprites/enemy/dragon_up4.png').convert_alpha()
        dragongold_up1 = pygame.transform.scale(dragongold_up1, (50, 50))
        dragongold_up2 = pygame.transform.scale(dragongold_up2, (50, 50))
        dragongold_up3 = pygame.transform.scale(dragongold_up3, (50, 50))
        dragongold_up4 = pygame.transform.scale(dragongold_up4, (50, 50))
        self.dragongold_up = [dragongold_up1, dragongold_up2, dragongold_up3, dragongold_up4]

        dragongold_left1 = pygame.image.load('graphics/sprites/enemy/dragon_left1.png').convert_alpha()
        dragongold_left2 = pygame.image.load('graphics/sprites/enemy/dragon_left2.png').convert_alpha()
        dragongold_left3 = pygame.image.load('graphics/sprites/enemy/dragon_left3.png').convert_alpha()
        dragongold_left4 = pygame.image.load('graphics/sprites/enemy/dragon_left4.png').convert_alpha()
        dragongold_left1 = pygame.transform.scale(dragongold_left1, (50, 50))
        dragongold_left2 = pygame.transform.scale(dragongold_left2, (50, 50))
        dragongold_left3 = pygame.transform.scale(dragongold_left3, (50, 50))
        dragongold_left4 = pygame.transform.scale(dragongold_left4, (50, 50))
        self.dragongold_left = [dragongold_left1, dragongold_left2, dragongold_left3, dragongold_left4]

        dragongold_right1 = pygame.image.load('graphics/sprites/enemy/dragon_right1.png').convert_alpha()
        dragongold_right2 = pygame.image.load('graphics/sprites/enemy/dragon_right2.png').convert_alpha()
        dragongold_right3 = pygame.image.load('graphics/sprites/enemy/dragon_right3.png').convert_alpha()
        dragongold_right4 = pygame.image.load('graphics/sprites/enemy/dragon_right4.png').convert_alpha()
        dragongold_right1 = pygame.transform.scale(dragongold_right1, (50, 50))
        dragongold_right2 = pygame.transform.scale(dragongold_right2, (50, 50))
        dragongold_right3 = pygame.transform.scale(dragongold_right3, (50, 50))
        dragongold_right4 = pygame.transform.scale(dragongold_right4, (50, 50))
        self.dragongold_right = [dragongold_right1, dragongold_right2, dragongold_right3, dragongold_right4]

        self.frame_index = 0
        random
        self.image = self.dragongold_down[self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.enemy_speed = 1
        self.vel = vec(0, 0)

    def front_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.dragongold_down[int(self.frame_index)]

    def back_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.dragongold_up[int(self.frame_index)]   
    
    def left_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.dragongold_left[int(self.frame_index)]  

    def right_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.dragongold_right[int(self.frame_index)]
    
    def idle_animation(self):
        if not self.running_x and not self.running_y:
            self.image = self.dragongold_down[0]

    def running_animation(self):
        if self.rect.x > self.player_pos.x:
            self.left_animation()             
            
        elif self.rect.x < self.player_pos.x:
            self.right_animation()

        elif self.rect.x == self.player_pos.x and self.rect.y < self.player_pos.y:
            self.front_animation()
        
        elif self.rect.x == self.player_pos.x and self.rect.y > self.player_pos.y:
            self.back_animation()
        elif self.rect.y == self.player_pos.y :
            self.front_animation()
    
    def moving(self):
        pass

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
        self.running_animation()
        self.moving()
        self.constraint()