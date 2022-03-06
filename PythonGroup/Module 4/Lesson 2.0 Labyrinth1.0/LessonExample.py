from pygame import * 
import pygame 
from os import path

img_dir = path.join(path.dirname(__file__), 'img') 
WIDTH = 480
HEIGHT = 600
FPS = 15  
# Создаем игру и окно
pygame.init() 
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robolab Python Workshop!")
clock = pygame.time.Clock()