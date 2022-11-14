import pygame
import sys
from gamerun import Gamerun

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

gamerun = Gamerun(screen, screen_width, screen_height)
font = pygame.font.Font('graphics/font/PressStart2P-vaV7.ttf', 20)
music = pygame.mixer.music.load("graphics/music/bg.mp3")
pygame.mixer.music.play(-1)

game_status = 1
prev_player_score = 0
new_player_score = 0

scores = []
rankscores = []
show = 0

def display_text(text, size, color, pos, screen):
    font = pygame.font.Font('graphics/font/PressStart2P-vaV7.ttf', size)
    text_surf = font.render(f'{text}', False, color)
    text_rect = text_surf.get_rect(center=pos)
    screen.blit(text_surf, text_rect)

def draw_text_rank(text, color, size, screen, pos):
    font = pygame.font.Font('graphics/font/PressStart2P-vaV7.ttf', size)
    textobj = font.render(text, False, color)
    textrect = textobj.get_rect(midleft = pos)
    screen.blit(textobj, textrect)

def ranking():
    global scores, rankscores, show
    if show != 1:
        scores = []
        rankscores = []
        with open('score.txt') as file:
            for line in file:
                name, score = line.split(',')
                score = int(score)
                scores.append((name, score))
            scores.sort(key=lambda s: s[1])
            scores.reverse()
            for num in range(0, 5):
                rankscores.insert(num,scores[num])
            file.flush()
            show = 1

def display_rank():
    ranking()
    space = 0
    for i in range(0, 5):
        draw_text_rank(f'{rankscores[i][0]}', ('black'), 20, screen, (screen_width / 2 - 250, 230 + space))
        space += 50

    space = 0
    for i in range(0, 5):
        draw_text_rank(f'{rankscores[i][1]}', ('black'), 20, screen, (screen_width / 2 + 200, 230 + space))
        space += 50

def menu():
    while True:
        global game_status

        screen.fill("white")

        display_text('Cha Lam Chop Ngap Kun', 50, 'black',
                     (screen_width/2, screen_height/2 - 130), screen)

        display_text('65010731 Patsakorn Thong-un', 25, 'black',
                     (screen_width/2, screen_height/2 - 20), screen)

        game_button = pygame.Rect(
            (screen_width/2 - 75, screen_height/2 + 70), (150, 60))
        pygame.draw.rect(screen, ('black'), game_button)
        display_text('play', 30, 'white', (screen_width /
                     2, screen_height/2 + 100), screen)

        rank_button = pygame.Rect(
            (screen_width/2 - 75, screen_height/2 + 170), (150, 60))
        pygame.draw.rect(screen, ('black'), rank_button)
        display_text('rank', 30, 'white', (screen_width /
                     2, screen_height/2 + 200), screen)

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
        global game_status, new_player_score, prev_player_score

        new_player_score = gamerun.score
        if new_player_score >= prev_player_score:
            prev_player_score = new_player_score

        if game_status == 1:
            gamerun.run()
            game_status = gamerun.game_status
        elif game_status == 0:
            gameover()

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
        menu_button = pygame.Rect(
            (screen_width - 250, screen_height/2 + 200), (150, 60))
        pygame.draw.rect(screen, ('black'), menu_button)
        display_text('back', 30, 'white', (screen_width -
                     175, screen_height/2 + 200 + 30), screen)

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

        display_rank()

        pygame.display.update()
        clock.tick(60)


def gameover():
    user_ip = ''
    text_box = pygame.Rect((screen_width/2 - 350/2, screen_height/2 - 20), (350, 50))
    active = False
    while True:
        global game_status, gamerun

        gamerun = Gamerun(screen, screen_width, screen_height)

        game_status = 1

        screen.fill("white")

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
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
                if menu_button.collidepoint((mx, my)):
                    file = open('score.txt', 'a')
                    file.write(f'{user_ip}, {prev_player_score}\n')
                    file.flush()
                    file.close()
                    menu()
            
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip = user_ip[:-1]
                    else:
                        user_ip += event.unicode
                        if surf.get_width() > text_box.w - 20:
                            user_ip = user_ip[:-1]
        
        display_text('GAMEOVER', 40, ('red'), (screen_width / 2, 70), screen)

        display_text(f'SCORE : {prev_player_score}', 20,('black'), (screen_width/2, 180), screen)

        display_text('TYPE YOUR NAME', 20,('black'), (screen_width/2, 300), screen)

        if active:
            color = pygame.Color('black')
        else:
            color = pygame.Color('grey')

        pygame.draw.rect(screen, color, text_box)
        surf = font.render(user_ip, True, 'white')
        screen.blit(surf, (text_box.x + 5, text_box.y + 20))
            
        pygame.display.update()
        clock.tick(60)


menu()
