import os 

currentFilePath     = os.path.dirname(__file__)             # получаем располежение текущей папки
imageFilePath = currentFilePath + "/image.jpg"              # прикрепляем путь к изоюражкнию
oroginalImage = open(imageFilePath, 'rb')                   # читаем изобржаение побитового типа 10101010101010
image = oroginalImage.read()                                 # здесь будет хранится зашифрованное изображение
 
encodedImageBytes = []

for eachByte in image:
    encodedImageBytes.append(int(eachByte))

for  i in range(len(encodedImageBytes)):
    encodedImageBytes[i] = 255 - encodedImageBytes[i]

encodedImageFilePath = currentFilePath + "/encodedimage.jpg"  # прикрепляем путь к зашифрованому
encodedImageTosave = open(encodedImageFilePath,'wb')
encodedImageTosave.write(bytes(encodedImageBytes))