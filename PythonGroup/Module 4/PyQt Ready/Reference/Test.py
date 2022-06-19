from functools import partial
from operator import indexOf
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
from PyQt5.QtGui import * 
import sys
  
class Window(QMainWindow):
    OutputMainNumber = "0"
    OutputSmallText = ""

    StoredDataNumber = []
    StoredDataOperation = []

    finishedOperation = False

    def __init__(self):
        super().__init__()

        self.setFixedSize(250, 315)

        self.setWindowTitle("Calculator")
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        self.OutputMain = QLabel("0", self)
        self.OutputMain.setGeometry(5,5,240,50)
        self.OutputMain.setStyleSheet("border: 2px solid black; border-radius: 5px; background: #ffffff; font: bold 24px Verdana; padding-top: 10px")
        self.OutputMain.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)

        self.OutputSmall = QLabel("0", self)
        self.OutputSmall.setGeometry(5,6,240,20)
        self.OutputSmall.setStyleSheet("font: bold 12px Verdana; padding-right: 8px")
        self.OutputSmall.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignTop)

        #ButtonsSetup
        self.Buttons = {}
        self.Buttons['CE'] = QPushButton("CE", self)
        self.Buttons['CE'].setGeometry(5,60,60,50)
        self.Buttons['CE'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['CE'].clicked.connect(partial(self.ResetCal,True))

        self.Buttons['C'] = QPushButton("C", self)
        self.Buttons['C'].setGeometry(65,60,60,50)
        self.Buttons['C'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['C'].clicked.connect(self.C)

        self.Buttons['Del'] = QPushButton("Del", self)
        self.Buttons['Del'].setGeometry(125,60,60,50)
        self.Buttons['Del'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['Del'].clicked.connect(self.Del)
        
        self.Buttons['Div'] = QPushButton("/", self)
        self.Buttons['Div'].setGeometry(185,60,60,50)
        self.Buttons['Div'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['Div'].clicked.connect(partial(self.OperationButton,"/"))

        #Row 2

        self.Buttons['7'] = QPushButton("7", self)
        self.Buttons['7'].setGeometry(5,110,60,50)
        self.Buttons['7'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['7'].clicked.connect(partial(self.NumberButton,7))

        self.Buttons['8'] = QPushButton("8", self)
        self.Buttons['8'].setGeometry(65,110,60,50)
        self.Buttons['8'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['8'].clicked.connect(partial(self.NumberButton,8))

        self.Buttons['9'] = QPushButton("9", self)
        self.Buttons['9'].setGeometry(125,110,60,50)
        self.Buttons['9'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['9'].clicked.connect(partial(self.NumberButton,9))

        self.Buttons['*'] = QPushButton("*", self)
        self.Buttons['*'].setGeometry(185,110,60,50)
        self.Buttons['*'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['*'].clicked.connect(partial(self.OperationButton,"*"))

        #Row 3

        self.Buttons['4'] = QPushButton("4", self)
        self.Buttons['4'].setGeometry(5,160,60,50)
        self.Buttons['4'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['4'].clicked.connect(partial(self.NumberButton,4))

        self.Buttons['5'] = QPushButton("5", self)
        self.Buttons['5'].setGeometry(65,160,60,50)
        self.Buttons['5'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['5'].clicked.connect(partial(self.NumberButton,5))

        self.Buttons['6'] = QPushButton("6", self)
        self.Buttons['6'].setGeometry(125,160,60,50)
        self.Buttons['6'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['6'].clicked.connect(partial(self.NumberButton,6))

        self.Buttons['-'] = QPushButton("-", self)
        self.Buttons['-'].setGeometry(185,160,60,50)
        self.Buttons['-'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['-'].clicked.connect(partial(self.OperationButton,"-"))

        #Row 4

        self.Buttons['1'] = QPushButton("1", self)
        self.Buttons['1'].setGeometry(5,210,60,50)
        self.Buttons['1'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['1'].clicked.connect(partial(self.NumberButton,1))

        self.Buttons['2'] = QPushButton("2", self)
        self.Buttons['2'].setGeometry(65,210,60,50)
        self.Buttons['2'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['2'].clicked.connect(partial(self.NumberButton,2))

        self.Buttons['3'] = QPushButton("3", self)
        self.Buttons['3'].setGeometry(125,210,60,50)
        self.Buttons['3'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['3'].clicked.connect(partial(self.NumberButton,3))

        self.Buttons['+'] = QPushButton("+", self)
        self.Buttons['+'].setGeometry(185,210,60,50)
        self.Buttons['+'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['+'].clicked.connect(partial(self.OperationButton,"+"))
        
        #Row 5

        self.Buttons['+/-'] = QPushButton("+/-", self)
        self.Buttons['+/-'].setGeometry(5,260,60,50)
        self.Buttons['+/-'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['+/-'].clicked.connect(self.Switch)

        self.Buttons['0'] = QPushButton("0", self)
        self.Buttons['0'].setGeometry(65,260,60,50)
        self.Buttons['0'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['0'].clicked.connect(partial(self.NumberButton,0))

        self.Buttons['.'] = QPushButton(".", self)
        self.Buttons['.'].setGeometry(125,260,60,50)
        self.Buttons['.'].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['.'].clicked.connect(self.Dot)

        self.Buttons['='] = QPushButton("=", self)
        self.Buttons['='].setGeometry(185,260,60,50)
        self.Buttons['='].setStyleSheet("font: bold 18px Verdana;")
        self.Buttons['='].clicked.connect(self.CalculateOperation)
  
        # show all the widgets
        self.show()

        self.OutputSmallText = "0"
        self.OutputSmallTextBefore = "0"

    def NumberButton(self, Number):
        self.ResetCal(False)
        if self.OutputMainNumber == "0":
            self.OutputMainNumber = str(Number)
            if self.OutputSmallText == "0":
                self.OutputSmallText = str(Number)
            else:
                self.OutputSmallText = self.OutputSmallText[:-1]
                self.OutputSmallText += str(Number)
        elif not (Number == 0 and self.OutputMainNumber == "0") :
            self.OutputMainNumber += str(Number)
            self.OutputSmallText += str(Number)
        self.OutputMain.setText(self.OutputMainNumber)
        self.OutputSmall.setText(self.OutputSmallText)

    def OperationButton(self, Symbol):
        if (not ((Symbol == "+" or Symbol == "-") and self.OutputSmallText == "")) and not self.finishedOperation:
            if not self.IsFloat(self.OutputMainNumber):
                self.Error()
                return
            self.StoredDataNumber.append(float(self.OutputMainNumber))
            self.StoredDataOperation.append(Symbol)
            self.OutputMainNumber = "0"
            if self.OutputSmallText == "":
                self.OutputSmallText = self.OutputMainNumber + " " + Symbol + " "
            else:
                self.OutputSmallText += " " + Symbol + " 0"
            self.OutputSmallTextBefore = self.OutputSmallText
            self.OutputMain.setText(self.OutputMainNumber)
            self.OutputSmall.setText(self.OutputSmallText)

    def CalculateOperation(self):
        if (not self.finishedOperation) and self.OutputMainNumber != "":
            if not self.IsFloat(self.OutputMainNumber):
                self.Error()
                return
            self.StoredDataNumber.append(float(self.OutputMainNumber))
            Result = 0
            if len(self.StoredDataOperation) == 0:
                if self.IsFloat(self.OutputMainNumber):
                    Result = float(self.OutputMainNumber)
                else:
                    self.Error()
                    return
            else:
                for I in range(len(self.StoredDataOperation)):
                    Item = self.StoredDataOperation[I]
                    if I == 0:
                        if Item == "+":
                            Result = self.StoredDataNumber[0] + self.StoredDataNumber[1]
                        elif Item == "-":
                            Result = self.StoredDataNumber[0] - self.StoredDataNumber[1]
                        elif Item == "*":
                            Result = self.StoredDataNumber[0] * self.StoredDataNumber[1]
                        elif Item == "/":
                            if self.StoredDataNumber[1] == 0:
                                Result = "Math Error"
                                break
                            Result = self.StoredDataNumber[0] / self.StoredDataNumber[1]
                    else:
                        if Item == "+":
                            Result = Result + self.StoredDataNumber[I + 1]
                        elif Item == "-":
                            Result = Result - self.StoredDataNumber[I + 1]
                        elif Item == "*":
                            Result = Result * self.StoredDataNumber[I + 1]
                        elif Item == "/":
                            if self.StoredDataNumber[I + 1] == 0:
                                Result = "Math Error"
                                break
                            Result = Result / self.StoredDataNumber[I + 1]
            if Result != "Math Error":
                if Result%1 == 0:
                    Result = int(Result)
            self.OutputSmallText += " = " + str(Result)
            self.OutputMainNumber = str(Result)
            self.OutputMain.setText(self.OutputMainNumber)
            self.OutputSmall.setText(self.OutputSmallText)

            self.finishedOperation = True

    def ResetCal(self, Override):
        if self.finishedOperation or Override:
            self.OutputMainNumber = "0"
            self.OutputSmallText = "0"
            self.OutputSmallTextBefore = "0"
            self.OutputMain.setText(self.OutputMainNumber)
            self.OutputSmall.setText(self.OutputSmallText)

            self.StoredDataOperation.clear()
            self.StoredDataNumber.clear()
            self.finishedOperation = False

    def C(self):
        if self.finishedOperation:
            self.ResetCal(True)
        else:
            self.OutputMainNumber = "0"
            self.OutputMain.setText(self.OutputMainNumber)
            self.OutputSmallText = self.OutputSmallTextBefore
            self.OutputSmall.setText(self.OutputSmallText)

    def Del(self):
        if self.finishedOperation:
            self.ResetCal(True)
        else:
            self.OutputMainNumber = self.OutputMainNumber[:-1]
            if self.OutputMainNumber == "":
               self.OutputMainNumber = "0"
            self.OutputMain.setText(self.OutputMainNumber)
            self.OutputSmallText = self.OutputSmallTextBefore[:-1] + self.OutputMainNumber
            self.OutputSmall.setText(self.OutputSmallText)
    
    def Switch(self):
        if (not self.finishedOperation) and (self.OutputMainNumber != "0"):
            if not self.OutputMainNumber.startswith("-"):
                self.OutputMainNumber = "-" + self.OutputMainNumber
            else:
                self.OutputMainNumber = self.OutputMainNumber[1:]
            self.OutputMain.setText(self.OutputMainNumber)
            self.OutputSmallText = self.OutputSmallTextBefore[:-1] + self.OutputMainNumber
            self.OutputSmall.setText(self.OutputSmallText)
    
    def Dot(self):
        if (not self.finishedOperation):
            self.OutputMainNumber += "."
            self.OutputMain.setText(self.OutputMainNumber)
            self.OutputSmallText = self.OutputSmallTextBefore[:-1] + self.OutputMainNumber
            self.OutputSmall.setText(self.OutputSmallText)
    
    def Error(self):
        self.finishedOperation = True
        self.OutputMain.setText("Number Error")
    
    def IsFloat(self, item):
        try:
            float(item)
            return True
        except:
            return False
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())