import glob, os, sys
import tkinter as tk
from tkinter import *
from tkinter import filedialog



window = tk.Tk()
window.title("FEE")
#The type frames are packed into the top frame
typeFrames = tk.Frame(window)

initialTypeFrame = tk.Frame(typeFrames)
itLabel = tk.Label(master=initialTypeFrame, text="Initial Extension:") #Label for entry
itEntry = tk.Entry(master=initialTypeFrame) #entry
itLabel.pack(side=TOP)
itEntry.pack(side=TOP)


outputTypeFrame = tk.Frame(typeFrames)
otLabel = tk.Label(master=outputTypeFrame, text="Output Extension:") #Label for entry\
otEntry = tk.Entry(master=outputTypeFrame) #entry
otLabel.pack(side=TOP)
otEntry.pack(side=TOP)

def dirSelectButton():
    folder = folder_select()
    locEntry.delete(0,tk.END)
    locEntry.insert(0,folder)


def folder_select():
    folder_select = filedialog.askdirectory()
    return folder_select


locFrame = tk.Frame(window)
locLabel = tk.Label(master=locFrame, text="Directory Location:") #label for Entry
locEntry = tk.Entry(master=locFrame) #Entry
locSel = tk.Button(master=locFrame, text="", command=dirSelectButton) #Select Directory #TODO: Update this to a photo :3
    #https://www.geeksforgeeks.org/python-add-image-on-a-tkinter-button/
locLabel.pack(side=TOP)
locEntry.pack(side=LEFT, padx=5)
locSel.pack(side=LEFT)


def run_Converter():
    initialType = itEntry.get()
    outputType = otEntry.get()
    loc = locEntry.get()
    convert_Files(initialType, outputType, loc)

def convert_Files(initialType, outputType, loc):
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
        filesconverted = (str(fileCounter) +" files were converted from " + initialType + " to " + outputType) #Amount of files were converted
    else:
        filesconverted = ("While the converter ran without issue, no files were found to convert") #none were converted

    root = Tk()
    root.withdraw()
    tk.messagebox.showinfo(title="File Extension Exchanger", message = filesconverted)

butFrame = tk.Frame(window)
convert_But = tk.Button(master=butFrame, text="Convert", command=run_Converter)
convert_But.pack()

initialTypeFrame.pack(side=LEFT, padx=5, pady=5)
outputTypeFrame.pack(side=LEFT, padx=5, pady=5)
typeFrames.pack(side=TOP, padx=5, pady=5)
locFrame.pack(side=TOP, padx=5, pady=5)
butFrame.pack(side=TOP, padx=5, pady=5)

window.mainloop()



# Input:
# File Name
# File extension
# Output:
# File with amended extension