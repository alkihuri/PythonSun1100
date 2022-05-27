from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__ (self):
        super(MyWindow,self).__init__() 
        self.counter = 0 
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Counter")
        self.CreateLabel("0",100,100) 
        self.CreateButton("Click!",100,150,self.CounterFunc)

    def CreateLabel(self,text,x=50,y=50):
        self.newLabel = QtWidgets.QLabel(self)
        self.newLabel.setText(text)
        self.newLabel.move(x,y) 

    def CreateButton(self,text,x,y,fun):
        self.newButton = QtWidgets.QPushButton(self)
        self.newButton.setText(text)
        self.newButton.move(x,y)
        self.newButton.clicked.connect(fun)

    def CounterFunc(self):
        self.counter += 1 
        self.newButton.adjustSize()
        self.newLabel.adjustSize()
        self.newLabel.setText(str(self.counter))
        self.update() 

app = QApplication(sys.argv)
window  = MyWindow() 
window.show()
sys.exit(app.exec_()) 

