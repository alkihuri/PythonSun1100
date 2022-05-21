from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

def CreateLabel(text,window,x,y):
    newLabel = QtWidgets.QLabel(window)
    newLabel.setText(text)
    newLabel.move(x,y)
    return newLabel


app = QApplication(sys.argv)
window  = QMainWindow()
window.setGeometry(200,200,300,300)
window.setWindowTitle("Robolab PyQt 1.0")
l = CreateLabel("Hello world!",window,50,50)
window.show()
sys.exit(app.exec_())

