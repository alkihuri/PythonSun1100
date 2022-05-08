from random import randint 
import pygame 
from os import path
pygame.init() 
font = pygame.font.Font(None, 72)

win_width = 800 
win_height = 600
left_bound = win_width / 40            
right_bound = win_width - 8 * left_bound
shift = 0

x_start, y_start = 20, 10

img_file_back =     path.dirname(__file__)+ '/cave.png'
img_file_hero =     path.dirname(__file__)+ '/m1.png'
img_file_enemy =    path.dirname(__file__)+ '/enemy.png' 
img_file_bomb =     path.dirname(__file__)+ '/bomb.png'
img_file_princess = path.dirname(__file__)+ '/princess.png'
FPS = 60


C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0

class FinalSprite(pygame.sprite.Sprite):
  def __init__(self, player_image, player_x, player_y, player_speed):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 120))
    self.speed = player_speed

     
    self.rect = self.image.get_rect()
    self.rect.x = player_x
    self.rect.y = player_y

class Hero(pygame.sprite.Sprite):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha() 
    self.rect.x += self.x_speed
    self.rect = self.image.get_rect()

    def gravitate(self):
        self.y_speed += 0.25
    def jump(self, y):
        if self.stands_on:
            self.y_speed = 
for event in pygame.event.get():
 if event.type == pygame.KEYDOWN:
 if event.key == pygame.K_LEFT:
 robin.x_speed = -5
 elif event.key == pygame.K_RIGHT:
 robin.x_speed = 5
 elif event.key == pygame.K_UP:
 robin.jump(-7)
    