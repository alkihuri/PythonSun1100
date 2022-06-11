#PyQt 4.0 
#work with files READ and WRITE
#presentation link https://docs.google.com/presentation/d/1bdxF5J2j9vmLCPbtVkgYI_0DsI1r05Yv_gwBHwv0ypk/edit?usp=sharing


import os


poem = ["Let me not to the marriage of true minds\n"
,"Admit impediments. Love is not love\n"
,"Which alters when it alteration finds,\n"
,"Or bends with the remover to remove.\n"]

currentFilePath     = os.path.dirname(__file__)      
newpoemFilePath = currentFilePath + "/WILLIAM SHAKESPEARE.txt"
f = open(newpoemFilePath,"w")
f.writelines(poem) 

poem = list()
currentFilePath     = os.path.dirname(__file__)                  
poemFilePath = currentFilePath + "/WILLIAM SHAKESPEARE.txt"
f = open(poemFilePath, "r")
for x in f:
    print(x)
 