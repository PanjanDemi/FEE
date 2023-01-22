import glob, os, sys, tkinter

from tkinter import messagebox
from tkinter import *


# Definition from commandline arguments
initialType = sys.argv[1]
outputType = sys.argv[2]
loc = sys.argv[3]
print(initialType+" "+outputType+" "+loc)
files = glob.glob(loc+"/*."+initialType)
fileCounter = 0

for x in files:
    fileName = os.path.basename(x)
    fileOld = os.path.join(loc,fileName)
    inTypeLen = len(initialType)
    outTypeLen = len(outputType)
    #TODO: Write something that chops the filetype off the file
    i = 1
    #I'm sorry god
    fileNameList = list(fileName)
    while i < inTypeLen+1:
        fileNameList[-i] = ''
        i += 1
    fileName = ''.join(fileNameList)
    fileName += outputType 
    fileName = os.path.join(loc,fileName)
    os.rename(fileOld, fileName)
    fileCounter +=1

if fileCounter >0:
    filesconverted = (str(fileCounter) +" files were converted from " + initialType + " to " + outputType)#Amount of files were converted
else:
    filesconverted = ("While the converter ran without issue, no files were found to convert") #none were converted

root = Tk()
root.withdraw()
tkinter.messagebox.showinfo(title="Python Filetype Converter", message = filesconverted)


# Input:
# File Name
# File extension
# Output:
# File with amended extension