from pygame import  *
import os 

def GetImage(nameToSet, sizeXtoSet,sizeYtoSet):
    currentFilePath     = os.path.dirname(__file__)
    resourcesDir        = os.path.join(currentFilePath,'Resources')
    imagesDir           = os.path.join(resourcesDir,'Images')  
    backgroundImagePath = os.path.join(imagesDir,nameToSet)
    backgroundImage     = image.load(backgroundImagePath)
    backgroundImage     = transform.scale(backgroundImage, (sizeXtoSet,sizeYtoSet))
    return backgroundImage

def WindowSetUp(width, height):
    window  = display.set_mode((width,height))
    display.set_caption("PythonTue_1700")
    backgroundImage = GetImage("hero.png",width,height) 
    window.blit(backgroundImage,(0,0))  
    display.update()


gameIsOn = True
while gameIsOn:
    time.delay(50)
    WindowSetUp(500,700)   
    for eachEvent in event.get(): 
        if eachEvent.type == KEYDOWN:  
            if eachEvent.key == K_SPACE:
                gameIsOn = False