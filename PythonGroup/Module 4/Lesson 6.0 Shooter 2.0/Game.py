print("Robolab Python Pro Course / Shooter template project =) ")


# link for presentation => https://docs.google.com/presentation/d/1UkxfjWFpecW7BD-9ngFL7hs1fSykJnfQynp53x15_i8/edit#slide=id.g122dbdc220d_1_85


# modules import 
import pygame
import random
from os import path
#colors and window size set up
WHITE = (255,255,255)
BLACK = (0,0,0)
WIDTH = 480
HEIGHT = 600
FPS = 15 
# Window creating
pygame.init()
pygame.mixer.init()
window_size = (WIDTH,HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Shooter 2nd lesson")
clock = pygame.time.Clock() 
# Game sprites 
img_dir = path.join(path.dirname(__file__),"img")
background = pygame.load(path.join(img_dir,"field.png")).convert()
background_rect = background.get_rect() 
player_img = pygame.load(path.join(img_dir,"field.png")).convert()
npc_img = pygame.load(path.join(img_dir,"npc.png")).convert()
bullet_img = pygame.load(path.join(img_dir,"bullet.png")).convert()

#player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_size = (50,50)
        self.image = pygame.transform.scale(player_img,player_size)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH /2
        self.rect.bottom = HEIGHT - player_size.x
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keysate = pygame.key.get_pressed()
        if keysate[pygame.K_LEFT]:
            self.speedx = -8 
        if keysate[pygame.K_RIGHT]:
            self.speedx = 8   
        self.rect.x += self.speedx
    #shoot mechanic function


#mob generation system ~ mob (NPC) class

#mob generation system ~ generation

#Game lifecycle
    #fps

    #event handler

        #event to close window

        #shoot [if event.type == pygame.KEYDOWN] [if event.key == pygame.K_SPACE]

    #update of render

    #screen flip


 


 






 

 