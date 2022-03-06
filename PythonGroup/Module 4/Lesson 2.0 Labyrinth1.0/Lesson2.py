from pygame import  * 
from sys    import  * 
from random import  * 
import os 

class Character(pygame.sprite):
    power = 0 
    name = 0
    def __init__(self,name,power,sprite):
        Spawn(self,spite)


    def Spawn(self,sprite):
        image = GetImage(sprite,20,20)
        window.blit(image ,(0,0)) 



def GetImage(name, x, y):
    current_path            = os.path.dirname(__file__)  
    resource_path           = os.path.join(current_path, 'Resources')  
    image_path              = os.path.join(resource_path, 'Images') 
    backgroundimagepath     = os.path.join(image_path,name)
    background = image.load(backgroundimagepath)
    background = transform.scale(background, (x, y))
    return background    

def DrawWindow(setX,setY):
    window = display.set_mode((700, 500))
    display.set_caption("First Project") 
    background = GetImage("background.png",700, 500)
    window.blit(background ,(0,0)) 
    player = Character("Hero",0,"hero.png")
    display.update()  