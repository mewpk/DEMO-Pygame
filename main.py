import pygame, sys
from gamerun import Gamerun

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

gamerun = Gamerun(screen, screen_width, screen_height)
music = pygame.mixer.music.load("graphics/music/bg.mp3")
pygame.mixer.music.play(-1)

def display_text(text, size, color, pos, screen):
    font = pygame.font.Font('graphics/font/PressStart2P-vaV7.ttf', size)
    text_surf = font.render(f'{text}', False, color)
    text_rect = text_surf.get_rect(center = pos)
    screen.blit(text_surf, text_rect)

def menu():
    while True:
        screen.fill("white")

        display_text('Cha Lam Chop Ngap Kun', 50, 'black', (screen_width/2, screen_height/2 - 130), screen)

        display_text('65010731 Patsakorn Thong-un', 25, 'black', (screen_width/2, screen_height/2 - 20), screen)

        game_button = pygame.Rect((screen_width/2 - 75, screen_height/2 + 70), (150, 60))
        pygame.draw.rect(screen, ('black'), game_button)
        display_text('play', 30, 'white', (screen_width/2, screen_height/2 + 100), screen)

        rank_button = pygame.Rect((screen_width/2 - 75, screen_height/2 + 170), (150, 60))
        pygame.draw.rect(screen, ('black'), rank_button)
        display_text('rank', 30, 'white', (screen_width/2, screen_height/2 + 200), screen)


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
        screen.fill("white")
        display_text('Rank', 40, 'black', (screen_width/2, 70), screen)
        menu_button = pygame.Rect((screen_width - 250, screen_height/2 + 200), (150, 60))
        pygame.draw.rect(screen, ('black'), menu_button)
        display_text('back', 30, 'white', (screen_width - 175, screen_height/2 + 200 + 30), screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if menu_button.collidepoint((mx, my)):
                    menu()

        pygame.display.update()
        clock.tick(60)

def gameover():
    pass

menu()