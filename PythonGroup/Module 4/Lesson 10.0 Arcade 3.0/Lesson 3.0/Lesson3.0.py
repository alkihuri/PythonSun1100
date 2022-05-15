# Подключить нужные модули
from random import randint 
import pygame 
from os import path
pygame.init() 
# во время игры пишем надписи размера 72
font = pygame.font.Font(None, 72)

# Глобальные переменные (настройки)
win_width = 800 
win_height = 600
left_bound = win_width / 40             # границы, за которые персонаж не выходит (начинает ехать фон)
right_bound = win_width - 8 * left_bound
shift = 0

x_start, y_start = 20, 10

img_file_back =     path.dirname(__file__)+ '/cave.png'
img_file_hero =     path.dirname(__file__)+ '/m1.png'
img_file_enemy =    path.dirname(__file__)+ '/enemy.png' 
img_file_bomb =     path.dirname(__file__)+ '/bomb.png'
img_file_princess = path.dirname(__file__)+ '/princess.png'
FPS = 60

# цвета:
C_WHITE = (255, 255, 255)
C_DARK = (48, 48, 0)
C_YELLOW = (255, 255, 87)
C_GREEN = (32, 128, 32)
C_RED = (255, 0, 0)
C_BLACK = (0, 0, 0)


# Классы
# класс для цели (стоит и ничего не делает)
class FinalSprite(pygame.sprite.Sprite):
  # конструктор класса
  def __init__(self, player_image, player_x, player_y, player_speed):
      # Вызываем конструктор класса (Sprite):
      pygame.sprite.Sprite.__init__(self)

      # каждый спрайт должен хранить свойство image - изображение
      self.image = pygame.transform.scale(pygame.image.load(player_image), (60, 120))
      self.speed = player_speed

      # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
      
class Hero(pygame.sprite.Sprite):
    def __init__(self, filename, x_speed=0, y_speed=0, x=x_start, y=y_start, width=120, height=120):
        pygame.sprite.Sprite.__init__(self)
        # картинка загружается из файла и умещается в прямоугольник нужных размеров:
        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha() 
                    # используем convert_alpha, нам надо сохранять прозрачность

        # каждый спрайт должен хранить свойство rect - прямоугольник. Это свойство нужно для определения касаний спрайтов. 
        self.rect = self.image.get_rect()
        # ставим персонажа в переданную точку (x, y):
        self.rect.x = x 
        self.rect.y = y
        # создаем свойства, запоминаем переданные значения:
        self.x_speed = x_speed
        self.y_speed = y_speed
        # добавим свойство stands_on - это та платформа, на которой стоит персонаж
        self.stands_on = False # если ни на какой не стоит, то значение - False

    def gravitate(self):
        self.y_speed += 0.25

    def jump(self, y):
        if self.stands_on:
            self.y_speed = y

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        # сначала движение по горизонтали
        self.rect.x += self.x_speed
        # если зашли за стенку, то встанем вплотную к стене
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: # идем направо, правый край персонажа - вплотную к левому краю стены
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) # если коснулись сразу нескольких, то правый край - минимальный из возможных
        elif self.x_speed < 0: # идем налево, ставим левый край персонажа вплотную к правому краю стены
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) # если коснулись нескольких стен, то левый край - максимальный

        # теперь движение по вертикали        
        self.gravitate()
        self.rect.y += self.y_speed
        # если зашли за стенку, то встанем вплотную к стене
        platforms_touched = pygame.sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: # идем вниз
            for p in platforms_touched:
                self.y_speed = 0 
                # Проверяем, какая из платформ снизу самая высокая, выравниваемся по ней, запоминаем её как свою опору:
                if p.rect.top < self.rect.bottom: 
                    self.rect.bottom = p.rect.top
                    self.stands_on = p
        elif self.y_speed < 0: # идем вверх
            self.stands_on = False # пошли наверх, значит, ни на чем уже не стоим!
            for p in platforms_touched:
                self.y_speed = 0  # при столкновении со стеной вертикальная скорость гасится
                self.rect.top = max(self.rect.top, p.rect.bottom) # выравниваем верхний край по нижним краям стенок, на которые наехали


class Wall(pygame.sprite.Sprite):
    def __init__(self, x=20, y=0, width=120, height=120, color=C_GREEN):
        pygame.sprite.Sprite.__init__(self)
        # картинка - новый прямоугольник нужных размеров:
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # создаем свойство rect 
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

class Enemy(pygame.sprite.Sprite): # враг
    def __init__(self, x=20, y=0, filename=img_file_enemy, width=100, height=100):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.transform.scale(pygame.image.load(filename), (width, height)).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y

    def update(self):
        ''' перемещает персонажа, применяя текущую горизонтальную и вертикальную скорость'''
        self.rect.x += randint(-5, 5)
        self.rect.y += randint(-5, 5)

# Запуск игры 
pygame.display.set_caption("ARCADA")
window = pygame.display.set_mode([win_width, win_height])
back = pygame.transform.scale(pygame.image.load(img_file_back).convert(), (win_width, win_height))


# список всех персонажей игры:
all_sprites = pygame.sprite.Sprite.Group()

barriers = pygame.sprite.Group()

enemies = pygame.sprite.Group()

bombs = pygame.sprite.Group()

# create a character, add it to the list of all sprites:
robin = Hero(img_file_hero)
all_sprites.add(robin)

# create walls, add them:
w = Wall(50, 150, 480, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(700, 50, 50, 360)
barriers.add(w)
all_sprites.add(w)
w = Wall(350, 380, 640, 20)
barriers.add(w)
all_sprites.add(w)
w = Wall(-200, 590, 1600, 20)
barriers.add(w)
all_sprites.add(w)


# список препятствий:

en = Enemy(50, 480)
all_sprites.add(en)
enemies.add(en)

en = Enemy(400, 480)
all_sprites.add(en)
enemies.add(en)


bomb = Enemy(550, 520, img_file_bomb, 60, 60)
bombs.add(bomb)

pr = FinalSprite(img_file_princess, win_width + 500, win_height - 150, 0)
all_sprites.add(pr)




# создаем персонажа, добавляем его в список всех спрайтов:

# создаем стены, добавляем их:




# Main game loop:
run = True
finished = False

while run:
   # Event Handling
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           run = False
       elif event.type == pygame.KEYDOWN:
           if event.key == pygame.K_LEFT:
               robin.x_speed = -5
           elif event.key == pygame.K_RIGHT:
               robin.x_speed = 5
           elif event.key == pygame.K_UP:
               robin.jump(-7)

       elif event.type == pygame.KEYUP:
           if event.key == pygame.K_LEFT:
               robin.x_speed = 0
           elif event.key == pygame.K_RIGHT:
               robin.x_speed = 0

     if not finished:
       # Moving Game Objects
       all_sprites.update()

       # beyond checking the rules of the game
       # check touch with bombs:
       pygame.sprite.groupcollide(bombs, all_sprites, True, True)
               # if the bomb touches the sprite, then it is removed from the list of bombs, and the sprite is removed from all_sprites!

       # check the touch of the hero with the enemies:
       if pygame.sprite.spritecollide(robin, enemies, False):
           robin.kill() # the kill method removes the sprite from all groups in which it is listed

       # check screen borders:
       if (
           robin.rect.x > right_bound and robin.x_speed > 0
           or
           robin.rect.x < left_bound and robin.x_speed < 0
       ): # when exiting to the left or right, we transfer the change to the screen shift
           shift -= robin.x_speed 
           # move all the sprites to a common shift (and separately the bombs, they are in another list):
           for s in all_sprites:
               s.rect.x -= robin.x_speed # robin himself is also in this list, so his movement will be visually canceled
           for s in bombs:
               s.rect.x -= robin.x_speed

       # draw the background with a shift
       local_shift = shift % win_width
       window.blit(back, (local_shift, 0))
       if local_shift != 0:
           window.blit(back, (local_shift - win_width, 0))

       # draw all sprites on the screen surface before checking for win/loss
       # if the game ended in this iteration of the loop, then a new background will be drawn on top of the characters
       all_sprites.draw(window) 
       # we draw a group of bombs separately - so a bomb that has left its group will automatically cease to be visible
       bombs.draw(window)

       # check for win and loss:
       if pygame.sprite.collide_rect(robin, pr):
           finished = True
           window.fill(C_BLACK)
           # write text on the screen
           text = font.render("YOU WIN!", 1, C_RED)
           window.blit(text, (250, 250))

       # check for loss:
       if robin not in all_sprites or robin.rect.top > win_height:
           finished = True           
           window.fill(C_BLACK)
           # write text on the screen
           text = font.render("GAME OVER", 1, C_RED)
           window.blit(text, (250, 250))

   pygame.display.update()

   # Pause
   pygame.time.delay(20)