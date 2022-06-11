#PyQt 4.0 
#work with files READ and WRITE
#presentation link https://docs.google.com/presentation/d/1bdxF5J2j9vmLCPbtVkgYI_0DsI1r05Yv_gwBHwv0ypk/edit?usp=sharing


import os
poem = list()
currentFilePath     = os.path.dirname(__file__)                  
poemFilePath = currentFilePath + "/RUDYARD KIPLING.txt"
f = open(poemFilePath, "r")
for x in f:
    print(x)

newpoemFilePath = currentFilePath + "/WILLIAM SHAKESPEARE.txt"
f = open(newpoemFilePath,"w")

