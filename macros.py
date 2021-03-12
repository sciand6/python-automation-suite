import datetime
import webbrowser
import os

# Welcome message
def getWelcomeMessage():
    d = datetime.datetime.now()
    return "Welcome back, today is " + d.strftime("%A") + ", " + d.strftime("%B") + " " + d.strftime("%d")

# Open url
def openUrl(url):
    webbrowser.open(url)

# Open file
def openFile(path):
    os.startfile(path)

# Open file and run commands
def runMacros(macro):
    with open("macros/" + macro + ".txt") as file:
        while True:
            command = file.readline().rstrip()
            action = file.readline().rstrip()
            if command == '':
                break
            else:
                if (command == "ourl"):
                    openUrl(action)
                elif (command == "ofil"):
                    openFile(action)
                else:
                    print("Something went wrong.")
                    break