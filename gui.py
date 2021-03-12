from tkinter import *
from macros import *
import os
import glob

# Globals
currentUrl = ""
newActionLabelCurRow = 2
currentFilePath = ""
newAction = []

def runMainWindow():
    # MAIN WINDOW
    root = Tk()
    root['bg'] = "#00004f"
    root.title("Python Virtual Assistant")

    # Welcome label
    welcomeLabel = Label(root, text=getWelcomeMessage(), bg = "#00004f", fg = "white")
    welcomeLabel.grid(row = 0, column = 0, columnspan = 3)

    # Entry Field
    entryField = Entry(root, width = 35, borderwidth=5)
    entryField.grid(row = 1, column = 0)

    # Run button
    runButton = Button(root, text = "Run", padx = 10, bg = "green", fg = "white", command = lambda: runMacros(entryField.get()))
    runButton.grid(row = 1, column = 2)

    # Create action button
    createActionButton = Button(root, text = "Create New Action", padx = 35, bg = "red", fg = "white", command=runCreateActionWindow)
    createActionButton.grid(row = 2, column = 0, columnspan = 3)

    root.mainloop()
    # END MAIN WINDOW

def runCreateActionWindow():
    # IMPLEMENT BUTTON PROMPTS
    # For open url button
    def openUrlPrompt():
        def killOpenUrlWindow():
            global currentUrl
            global newActionLabelCurRow
            global newAction
            currentUrl = urlEntryField.get()
            newAction.insert(0, "ourl " + currentUrl)
            newActionLabel = Label(createActionWindow, text = "Url " + currentUrl, bg = "#00004f", fg = "white")
            newActionLabel.grid(row = newActionLabelCurRow, column = 1)
            newActionLabelCurRow = newActionLabelCurRow + 1
            currentUrl = ""
            openUrlWindow.destroy()
        
        # OPEN URL WINDOW
        openUrlWindow = Tk()
        openUrlWindow.title("Enter The Url")

        # Entry field
        urlEntryField = Entry(openUrlWindow, width = 35, borderwidth=5)
        urlEntryField.grid(row = 0, column = 0)

        # Enter button
        urlEnterButton = Button(openUrlWindow, text = "Enter", padx = 20, command = killOpenUrlWindow)
        urlEnterButton.grid(row = 1, column = 0)
        # END OPEN URL WINDOW

    # For open file button
    def openFilePrompt():
        def killOpenFileWindow():
            global currentFilePath
            global newActionLabelCurRow
            global newAction
            currentFilePath = fileEntryField.get()
            newAction.insert(0, "ofil " + currentFilePath)
            newActionLabel = Label(createActionWindow, text = "File " + currentFilePath, bg = "#00004f", fg = "white")
            newActionLabel.grid(row = newActionLabelCurRow, column = 1)
            newActionLabelCurRow = newActionLabelCurRow + 1
            currentFilePath = ""
            openFileWindow.destroy()
        
        # OPEN FILE WINDOW
        openFileWindow = Tk()
        openFileWindow.title("Enter The File Path")

        # Entry field
        fileEntryField = Entry(openFileWindow, width = 35, borderwidth=5)
        fileEntryField.grid(row = 0, column = 0)

        # Enter button
        fileEnterButton = Button(openFileWindow, text = "Enter", padx = 20, command = killOpenFileWindow)
        fileEnterButton.grid(row = 1, column = 0)
        # END OPEN FILE WINDOW

    # CREATE ACTION WINDOW
    createActionWindow = Tk()
    createActionWindow['bg'] = "#00004f"
    createActionWindow.title("Create New Action")

    def saveActionNow():
        saveAction()
        on_closing()

    # Close protocol
    def on_closing():
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        newAction = []
        createActionWindow.destroy()

    createActionWindow.protocol("WM_DELETE_WINDOW", on_closing)

    # Create new action label
    createActionLabel = Label(createActionWindow, text = "Create New Action", bg = "#00004f", fg = "white")
    createActionLabel.grid(row = 0, column = 0, columnspan = 3)

    # Open URL button
    openUrlButton = Button(createActionWindow, text = "Open Url", bg = "#00006d", fg = "white", command = openUrlPrompt)
    openUrlButton.grid(row = 2, column = 0)

    # Open file button
    openFileButton = Button(createActionWindow, text = "Open File", bg = "#00006d", fg = "white", command = openFilePrompt)
    openFileButton.grid(row = 4, column = 0)

    # New action list label
    newActionListLabel = Label(createActionWindow, text = "New Action", bg = "#00004f", fg = "white")
    newActionListLabel.grid(row = 1, column = 1)

    # Actions list label
    actionsListLabel = Label(createActionWindow, text = "Current Actions", bg = "#00004f", fg = "white")
    actionsListLabel.grid(row = 1, column = 2)

    # Save action button
    saveActionButton = Button(createActionWindow, text = "Save", bg = "green", fg = "white", command = saveActionNow)
    saveActionButton.grid(row = 6, column = 0)

    # Get actions for actions list
    if (os.path.isdir("macros") == True):
        os.chdir(os.getcwd() + "\\macros")
    actionFiles = glob.glob("*.txt")
    curRow = 2
    for f in actionFiles:
        actionLabel = Label(createActionWindow, text = f, bg = "#00004f", fg = "white")
        actionLabel.grid(row = curRow, column = 2)
        curRow = curRow + 1
    # END CREATE ACTION WINDOW

def saveAction():
    # IMPLEMENT SAVE FEATURE
    def save():
        nameOfMacro = actionEntryField.get()
        macroFile = open("macros/" + nameOfMacro + ".txt", "w")
        for action in newAction:
            action = action.split()
            if (action[0] == "ofil"):
                macroFile.write("ofil\n")
                macroFile.write(action[1] + "\n")
            elif (action[0] == "ourl"):
                macroFile.write("ourl\n")
                macroFile.write(action[1] + "\n")
        saveActionWindow.destroy()

    # SAVE ACTION WINDOW
    saveActionWindow = Tk()
    saveActionWindow.title("Enter The Name Of The Action")

    # Entry field
    actionEntryField = Entry(saveActionWindow, width = 35, borderwidth=5)
    actionEntryField.grid(row = 0, column = 0)

    # Enter button
    actionEnterButton = Button(saveActionWindow, text = "Enter", padx = 20, command = save)
    actionEnterButton.grid(row = 1, column = 0)
    # END OPEN FILE WINDOW

runMainWindow()