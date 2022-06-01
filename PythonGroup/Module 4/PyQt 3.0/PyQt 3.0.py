import os 

currentFilePath     = os.path.dirname(__file__)                 # получаем располежение текущей папки
imageFilePath = currentFilePath + "/image.jpg"                  # прикрепляем путь к изоюражкнию
oroginalImage = open(imageFilePath, 'rb')                       # читаем изобржаение побитового типа  255 22 100 22 такая фигня (если что загугли)
image = oroginalImage.read()                                    # здесь будет хранится зашифрованное изображение
 
encodedImageBytes = []                                          # создаем массив где будем харинть побитовое значение для зашифрованного изобрадения

for eachByte in image:                                          # биты это не число поэтому всякую фигну как с числам  тут не сделаешь 
    encodedImageBytes.append(int(eachByte))                     # поэтому переводим в int тоесть в число

for  i in range(len(encodedImageBytes)):
    encodedImageBytes[i] = 255 - encodedImageBytes[i]           # магия! тут мы тупо зеркалим как каждый бит .... был 0 стал 255, был 255 стал 0

encodedImageFilePath = currentFilePath + "/encodedimage.jpg"    # прикрепляем путь к зашифрованому
encodedImageTosave = open(encodedImageFilePath,'wb')            # открываем поток для записи 
encodedImageTosave.write(bytes(encodedImageBytes))              # пишесм в файл 