import pygame
from player import Player

class Gamerun():
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.screen_width = screen_width
        self.screen_height = screen_height

        #player
        player_sprite = Player(self.screen_width, self.screen_height)
        self.player = pygame.sprite.GroupSingle(player_sprite)
    
    def run(self):
        self.screen.fill("white")

        self.player.draw(self.screen)
        self.player.update()