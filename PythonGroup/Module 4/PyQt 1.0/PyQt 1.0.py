#pyqt 1.0 
# https://docs.google.com/presentation/d/1gqyMy49e3D3A0E9ACEwZGh825fAHHC7Q8yT97-nw4Qw/edit?usp=sharing
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
from PyQt5.QtWidgets import widget, widget
app = QApplication([])
sys.exit(app.exec_())
class MyWindow(QMainWindow):
    def CreateLabel(self,text,x=50,y=50):
        self.newLabel = QtWidgets.QLabel(self)
        self.newLabel.SetText
        self.newLabel.Move(50,50)

    def CreateButton(self,text,x,y,fun):
        self.newButton = QtWidgets.QPushButton(self)
        self.newButton.SetText
        self.newButton.Move(50,50)
        self.newButton.clicked.connect(input)

        app = QApplication(sys.argv)
        window  = MyWindow()
        window.show()
        sys.exit(app.exec_())

    def CounterFunc(self):
        self.counter+=1
        self.newLabel.setText(str(self.counter))
    def __init__ (self):
        super(MyWindow,self).__init__()
        self.counter = 0
        self.setGeometry(200,200,300,300)
        self.setWindowTitle("Counter")
        self.CreateLabel(params)
        self.CreateButton(params)
        
