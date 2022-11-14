import pygame
from random import randint
import random

class Enemy3(pygame.sprite.Sprite):
    def __init__(self, pos,screen_width,screen_height, player_pos):
        super().__init__()
        self.screen_width, self.screen_height = screen_width , screen_height
        #player
        self.player_pos = player_pos

        vec = pygame.math.Vector2
  
        fire_front1 = pygame.image.load('graphics/sprites/Skeleton/front1.png').convert_alpha()
        fire_front2 = pygame.image.load('graphics/sprites/Skeleton/front2.png').convert_alpha()
        fire_front3 = pygame.image.load('graphics/sprites/Skeleton/front3.png').convert_alpha()
        fire_front4 = pygame.image.load('graphics/sprites/Skeleton/front4.png').convert_alpha()
        fire_front1 = pygame.transform.scale(fire_front1, (50, 50))
        fire_front2 = pygame.transform.scale(fire_front2, (50, 50))
        fire_front3 = pygame.transform.scale(fire_front3, (50, 50))
        fire_front4 = pygame.transform.scale(fire_front4, (50, 50))
        self.fire_front = [fire_front1, fire_front2, fire_front3, fire_front4]

        fire_back1 = pygame.image.load('graphics/sprites/Skeleton/back1.png').convert_alpha()
        fire_back2 = pygame.image.load('graphics/sprites/Skeleton/back2.png').convert_alpha()
        fire_back3 = pygame.image.load('graphics/sprites/Skeleton/back3.png').convert_alpha()
        fire_back4 = pygame.image.load('graphics/sprites/Skeleton/back4.png').convert_alpha()
        fire_back1 = pygame.transform.scale(fire_back1, (50, 50))
        fire_back2 = pygame.transform.scale(fire_back2, (50, 50))
        fire_back3 = pygame.transform.scale(fire_back3, (50, 50))
        fire_back4 = pygame.transform.scale(fire_back4, (50, 50))
        self.fire_back = [fire_back1, fire_back2, fire_back3, fire_back4]

        fire_left1 = pygame.image.load('graphics/sprites/Skeleton/left1.png').convert_alpha()
        fire_left2 = pygame.image.load('graphics/sprites/Skeleton/left2.png').convert_alpha()
        fire_left3 = pygame.image.load('graphics/sprites/Skeleton/left3.png').convert_alpha()
        fire_left4 = pygame.image.load('graphics/sprites/Skeleton/left4.png').convert_alpha()
        fire_left1 = pygame.transform.scale(fire_left1, (50, 50))
        fire_left2 = pygame.transform.scale(fire_left2, (50, 50))
        fire_left3 = pygame.transform.scale(fire_left3, (50, 50))
        fire_left4 = pygame.transform.scale(fire_left4, (50, 50))
        self.fire_left = [fire_left1, fire_left2, fire_left3, fire_left4]

        fire_right1 = pygame.image.load('graphics/sprites/Skeleton/right1.png').convert_alpha()
        fire_right2 = pygame.image.load('graphics/sprites/Skeleton/right2.png').convert_alpha()
        fire_right3 = pygame.image.load('graphics/sprites/Skeleton/right3.png').convert_alpha()
        fire_right4 = pygame.image.load('graphics/sprites/Skeleton/right4.png').convert_alpha()
        fire_right1 = pygame.transform.scale(fire_right1, (50, 50))
        fire_right2 = pygame.transform.scale(fire_right2, (50, 50))
        fire_right3 = pygame.transform.scale(fire_right3, (50, 50))
        fire_right4 = pygame.transform.scale(fire_right4, (50, 50))
        self.fire_right = [fire_right1, fire_right2, fire_right3, fire_right4]

        self.frame_index = 0
        random
        self.image = self.fire_front[self.frame_index]
        self.rect = self.image.get_rect(center=(pos))

        self.enemy_speed = 1
        self.vel = vec(0, 0)

    def front_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.fire_front[int(self.frame_index)]

    def back_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.fire_back[int(self.frame_index)]   
    
    def left_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.fire_left[int(self.frame_index)]  

    def right_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.fire_right[int(self.frame_index)]
    
    def idle_animation(self):
        if not self.running_x and not self.running_y:
            self.image = self.fire_front[0]

    def running_animation(self):
        if self.rect.x > self.player_pos.x:
            self.left_animation()             
            
        elif self.rect.x < self.player_pos.x:
            self.right_animation()

        elif self.rect.x == self.player_pos.x:
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