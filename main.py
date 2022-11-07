import pygame, sys
from gamerun import Gamerun

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

gamerun = Gamerun(screen, screen_width, screen_height)

def menu():
    while True:
        screen.fill("pink")

        game_button = pygame.Rect((screen_width/2 - 50, screen_height/2), (100, 50))
        pygame.draw.rect(screen, ('black'), game_button)

        rank_button = pygame.Rect((screen_width/2 - 50, screen_height/2 + 70), (100, 50))
        pygame.draw.rect(screen, ('black'), rank_button)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if game_button.collidepoint((mx, my)):
                    game()
                if rank_button.collidepoint((mx, my)):
                    rank()
                
        pygame.display.update()
        clock.tick(60)

def game():
    while True:
        gamerun.run()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)


def rank():
    while True:
        screen.fill("black")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(60)

def gameover():
    pass


menu()