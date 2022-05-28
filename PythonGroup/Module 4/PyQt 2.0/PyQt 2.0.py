from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel, QLineEdit
import sys


class MyWindow(QMainWindow):
    def __init__ (self):
        super(MyWindow,self).__init__() 
        self.counter = 0 
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Calculator")

        self.aField         = self.CreateInputField("a:",100,25)
        self.bField         = self.CreateInputField("b:",100,50)
        self.resultField    = self.CreateLabel("Result:",50,100)

        self.plusBtn        = self.CreateButton("+",100,150,self.Plus)
        self.minusBtn       = self.CreateButton("-",100,175,self.Minus)
        self.multiplyBtn    = self.CreateButton("*",100,200,self.Multiply)
        self.divideBtn      = self.CreateButton("/",100,225,self.Divide)

        self.a = 0
        self.b = 0 
        self.result = 0 

    def CreateLabel(self,text,x,y):
        newLabel = QtWidgets.QLabel(self)
        newLabel.setText(text)
        newLabel.move(x,y)
        return newLabel
    
    def CreateInputField(self,label,x,y):
        self.CreateLabel(label,x-50,y)
        line = QLineEdit(self) 
        line.move(x, y)
        line.resize(200, 32)
        return line

    def CreateButton(self,text,x,y,fun):
        newButton = QtWidgets.QPushButton(self)
        newButton.setText(text)
        newButton.move(x,y)
        newButton.clicked.connect(fun) 
        return newButton

    def Update(self):
        try:
            self.a =  float(self.aField.text())
        except:
            self.a = 0
        try:
            self.b =  float(self.bField.text())
        except:
            self.b = 0
        self.resultField.setText("Result : " + str(self.result))


    def Plus(self): 
        self.Update()
        self.result =  self.a + self.b
        self.Update()

    def Minus(self): 
        self.Update()
        self.result = self.a - self.b
        self.Update()

    def Multiply(self): 
        self.Update()
        self.result = self.a * self.b
        self.Update()

    def Divide(self): 
        self.Update()
        self.result = self.a / self.b
        self.Update()

app = QApplication(sys.argv)
window  = MyWindow() 
window.show()
sys.exit(app.exec_()) 

