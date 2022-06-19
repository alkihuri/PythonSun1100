#final project
from tkinter import *
from webbrowser import open
link1 = input('What is your favourite website link?')
name1 = input('What do you want to call the shortcut?')
link2 = input('What other website link do you like?')
name2 = input('What do you want to call the shortcut?')
link3 = input('What other website link do you like?')
name3 = input('What do you want to call the shortcut?')
clrtxt = input('What colour do you want the text to be?')
clrbkg = input('What colour do you want the buttons to be?')
def bAaction():
    open(link1)
def bBaction():
    open(link2)
def bCaction():
    open(link3)
window = Tk()
buttonA = Button(window, text=name1, command=bAaction, width=15, bg=clrbkg, fg=clrtxt)
buttonB = Button(window, text=name2, command=bBaction, width=15, bg=clrbkg, fg=clrtxt)
buttonC = Button(window, text=name3, command=bCaction, width=15, bg=clrbkg, fg=clrtxt)
buttonA.pack()
buttonB.pack()
buttonC.pack()
