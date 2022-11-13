import pygame
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.wasd = 's'
        self.bullet_type = 0

        # music 
        self.shoot = pygame.mixer.Sound("graphics/music/shoot.mp3")
        self.shoot.set_volume(0.3)

        front1 = pygame.image.load("graphics/sprites/player/player_front1.png")
        front2 = pygame.image.load("graphics/sprites/player/player_front2.png")
        front3 = pygame.image.load("graphics/sprites/player/player_front3.png")
        front4 = pygame.image.load("graphics/sprites/player/player_front4.png")
        front1 = pygame.transform.scale(front1, (50, 50))
        front2 = pygame.transform.scale(front2, (50, 50))
        front3 = pygame.transform.scale(front3, (50, 50))
        front4 = pygame.transform.scale(front4, (50, 50))
        self.front = [front1, front2, front3, front4]

        back1 = pygame.image.load("graphics/sprites/player/player_back1.png")
        back2 = pygame.image.load("graphics/sprites/player/player_back2.png")
        back3 = pygame.image.load("graphics/sprites/player/player_back3.png")
        back4 = pygame.image.load("graphics/sprites/player/player_back4.png")
        back1 = pygame.transform.scale(back1, (50, 50))
        back2 = pygame.transform.scale(back2, (50, 50))
        back3 = pygame.transform.scale(back3, (50, 50))
        back4 = pygame.transform.scale(back4, (50, 50))
        self.back = [back1, back2, back3, back4]

        right1 = pygame.image.load("graphics/sprites/player/player_right1.png")
        right2 = pygame.image.load("graphics/sprites/player/player_right2.png")
        right3 = pygame.image.load("graphics/sprites/player/player_right3.png")
        right4 = pygame.image.load("graphics/sprites/player/player_right4.png")
        right1 = pygame.transform.scale(right1, (50, 50))
        right2 = pygame.transform.scale(right2, (50, 50))
        right3 = pygame.transform.scale(right3, (50, 50))
        right4 = pygame.transform.scale(right4, (50, 50))
        self.right = [right1, right2, right3, right4]

        self.frame_index = 0
        self.image = self.front[self.frame_index]
        self.rect = self.image.get_rect(center = (self.screen_width/2, self.screen_height/2))

        self.direction = pygame.math.Vector2()

        #player status
        self.running_x = False
        self.running_y = False

        self.facing_right = False

        self.speed = 5

        #bullet
        self.bullet = pygame.sprite.Group() 
        self.bullet_adding_time = 10       
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.left_right_animation()
            self.direction.x = -1
            self.facing_right = False
            self.running_x = True
            self.wasd = 'a'
        elif keys[pygame.K_d]:
            self.left_right_animation()
            self.direction.x = 1
            self.facing_right = True
            self.running_x = True
            self.wasd = 'd'
        else:
            self.direction.x = 0
            self.running_x = False
        
        if keys[pygame.K_w]:
            self.back_animation()
            self.direction.y = -1
            self.running_y = True
            self.wasd = 'w'
        elif keys[pygame.K_s]:
            self.front_animation()
            self.direction.y = 1
            self.running_y = True
            self.wasd = 's'
        else:
            self.direction.y = 0
            self.running_y = False

    def moving(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        if self.running_x:
            self.rect.x += self.direction.x * self.speed
        if self.running_y:
            self.rect.y += self.direction.y * self.speed
    
    def idle_animation(self):
        if not self.running_x and not self.running_y:
            if self.wasd == 'w':
                self.back_animation()
            elif self.wasd == 'a':
                self.left_right_animation()
            elif self.wasd == 's' :
                self.front_animation()
            elif self.wasd == 'd' :
                self.left_right_animation()
    
    def front_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.front[int(self.frame_index)]

    def back_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.back[int(self.frame_index)]   
    
    def left_right_animation(self):
        self.frame_index += 0.1
        if self.frame_index >= 4:
            self.frame_index = 0
        self.image = self.right[int(self.frame_index)]  

        if not self.facing_right:
            self.image = pygame.transform.flip(self.image, True, False)
    
    def constraint(self):
        if self.rect.left <= 50:
            self.rect.left = 50
        elif self.rect.right >= self.screen_width - 50:
            self.rect.right = self.screen_width - 50
        
        if self.rect.top <= 50:
            self.rect.top = 50
        elif self.rect.bottom >= self.screen_height - 50:
            self.rect.bottom = self.screen_height - 50
    
    def shooting(self):
        self.bullet_adding_time -= 1
        if self.bullet_adding_time == 0:
            self.bullet.add(Bullet((self.rect.center), self.wasd, self.bullet_type))
            pygame.mixer.Sound.play(self.shoot)
            
            if self.bullet_type == 0:
                self.bullet_adding_time = 50
            elif self.bullet_type == 1:
                self.bullet_adding_time = 30
            elif self.bullet_type == 2:
                self.bullet_adding_time = 20
            elif self.bullet_type == 3:
                self.bullet_adding_time = 15
            elif self.bullet_type == 4:
                self.bullet_adding_time = 10
            elif self.bullet_type == 5:
                self.bullet_adding_time = 5

    def update(self):
        self.get_input()
        self.moving()
        self.idle_animation()
        self.constraint()
        self.shooting()

        self.bullet.update()
        
