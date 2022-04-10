from pygame import *
-import random 
from os import path


ENEMY = [MiG_35, MiG_31]
MiG_35 = sprite.Group()
for i in range(1,3)

MiG_31 = sprite.Group()
for i in range(1,6)

ENeMY = enemy(self, sprite)

ENEMY.add(ENeMY)

LockedPlanes = [Su-27, Il-76, An-225]
UnlockedPlanes = [ZAZ]




WIDTH = 480
HEIGHT = 600
FPS = 15

# colors set up
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)








# Window creating
pygame.init() 
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shooter Example =)")
clock = pygame.time.Clock()


img_dir = path.join(path.dirname(__file__), 'img') 
# Game sprites
background = pygame.image.load(path.join(img_dir, "field.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "ship.png")).convert()
npc_img = pygame.image.load(path.join(img_dir, "npc.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "bullet.png")).convert()


class Player = Player(pygame.sprite.Sprite):
    score = 0
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def _upgrade_(self, score):
        if score = 50:
            print("You've Upgraded from ZAZ to Su-27")
            UnlockedPlanes.add(LockedPlanes(Su-27))
        else:


     def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(npc_img, (50, 50))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-300, -30)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()


# Загрузка всей игровой графики
background = pygame.image.load(path.join(img_dir, "field.png")).convert()
background_rect = background.get_rect()
player_img = pygame.image.load(path.join(img_dir, "ship.png")).convert()
npc_img = pygame.image.load(path.join(img_dir, "npc.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "bullet.png")).convert()

all_sprites = pygame.sprite.Group()
#Game entities innit
all_sprites = pygame.sprite.Group()  
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
player = Player() 
all_sprites.add(player)

for i in range(2):
    m = Mob()
    all_sprites.add(m)