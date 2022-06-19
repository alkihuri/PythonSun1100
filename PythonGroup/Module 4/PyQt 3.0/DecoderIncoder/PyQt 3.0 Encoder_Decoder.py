from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QLineEdit
import sys
 

class View(QMainWindow):  

    def __init__(self,newController): 
        super(View,self).__init__()     
        self.controller = newController                       
        self.setGeometry(300,200,300,250)                                        
        self.setWindowTitle("Caesar Cipher") 
        self.word           = self.CreateInputField("Word:",    25,25) 
        self.resultField    = self.CreateInputField("Result:",  25,75)
        self.encryptBtn     = self.CreateButton("Encrypt",      25,125,self.EncryptHandler)
        self.decryptBtn     = self.CreateButton("Decrypt",      25,175,self.DecryptHandler) 

    def EncryptHandler(self):
        self.controller.SetWordToEncrypt(self.word.text())
        self.controller.DoCrypt()

    def DecryptHandler(self):
        self.controller.SetWordToDecrypt(self.word.text())
        self.controller.DoDecrypt()
       
    def CreateLabel(self,text,x,y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x,y)
        return newLabel

    def CreateInputField(self,label,x,y):
        offsetForInputField = 50
        self.CreateLabel(label,x,y)
        line = QLineEdit(self)
        line.move(x+offsetForInputField, y)
        line.resize(200, 32)
        return line

    def CreateButton(self,text,x,y,fun):
        newButton = QtWidgets.QPushButton(self)
        newButton.setText(text)
        newButton.resize(250, 32)
        newButton.move(x,y)
        newButton.clicked.connect(fun)
        newButton.clicked.connect(self.UpdateUI)
        return newButton
    
    def UpdateUI(self):
        self.resultField.setText(myController.GetResult())


class Model():

    def __init__(self,key):
        self.key = key

    def Encrypt(self,word):
        wLength = len(word)
        ecnrypted = ""
        listWord = list(word) 
        for i in range(wLength):
            eachCharacter = word[i]
            eachCharacterInt = int(ord(word[i]))
            encryptedCahracter = (eachCharacterInt - self.key) % 255  
            ecnrypted += chr(encryptedCahracter)
        return ecnrypted

    def Decrypt(self,word):
        wLength = len(word)
        decrypted = ""
        listWord = list(word) 
        for i in range(wLength):
            eachCharacter = word[i]
            eachCharacterInt = int(ord(word[i]))
            decryptedCahracter = (eachCharacterInt + self.key) % 255  
            decrypted += chr(decryptedCahracter)
        return decrypted

class Controller():

    def __init__(self,newModel):
        self.model = newModel

    def SetWordToDecrypt(self,word):
        self.wordToDecrypt = word

    def SetWordToEncrypt(self,word):
        self.wordToEncrypt = word

    def DoCrypt(self):
        self.encryptedword = self.model.Encrypt(self.wordToEncrypt)
        self.result = self.encryptedword

    def DoDecrypt(self):
        self.decryptedword = self.model.Decrypt(self.wordToDecrypt)
        self.result = self.decryptedword

    def GetResult(self):
        return self.result



app = QApplication(sys.argv) 
key = 5
myModel = Model(key)
myController = Controller(myModel)
myView = View(myController) 
myView.show()
sys.exit(app.exec_())