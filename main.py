import pygame
import sys
import os
from random import randint


class Tree(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('graphics/tree.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('graphics/player.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.speed = 1
        self.load_sprites()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
        self.rect.center += self.direction * self.speed



class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

        # camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        # ground
        self.ground_surface = pygame.image.load("graphics/Map.png").convert()
        self.ground_rect = self.ground_surface.get_rect(topleft=(0, 0))

        # zoom
        self.zoom_scale = 4
        self.internal_surf_size = (1280, 720)
        self.internal_surf = pygame.Surface(
            self.internal_surf_size, pygame.SRCALPHA)
        self.internal_rect = self.internal_surf.get_rect(
            center=(self.half_w, self.half_h))
        self.internal_surface_size_vector = pygame.math.Vector2(
            self.internal_surf_size)
        self.internal_offset = pygame.math.Vector2()
        self.internal_offset.x = self.internal_surf_size[0] // 2 - self.half_w
        self.internal_offset.y = self.internal_surf_size[1] // 2 - self.half_h

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):

        self.center_target_camera(player)
        # ground
        ground_offset = self.ground_rect.topleft - self.offset
        self.internal_surf.blit(self.ground_surface, ground_offset)
        # active elements
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.internal_surf.blit(sprite.image, offset_pos)
        scaled_surf = pygame.transform.scale(
            self.internal_surf, self.internal_surface_size_vector * self.zoom_scale)
        scaled_rect = scaled_surf.get_rect(center=(self.half_w, self.half_h))
        self.display_surface.blit(scaled_surf, scaled_rect)


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# setup
camera_group = CameraGroup()
player = Player((300, 200), camera_group)

# loop tree (for enemy)
# for i in range(20):
#     random_x = randint(0,1000)
#     random_y = randint(0,1000)
#     Tree((random_x,random_y),camera_group)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # color screen
    screen.fill("#71ddee")

    camera_group.update()
    camera_group.custom_draw(player)

    pygame.display.update()
    clock.tick(60)
