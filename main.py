import datetime
import webbrowser
import os

# Welcome message
d = datetime.datetime.now()
print("Welcome back today is " + d.strftime("%A") + ", " + d.strftime("%B") + " " + d.strftime("%d"))

# Open url
def openUrl(url):
    webbrowser.open(url)

# Open file
def openFile(path):
    os.startfile(path)

# Create a macro
def createMacro():
    done = False
    nameOfMacro = input("Enter the name of the macro: ")
    commands = []
    while (done != True):
        action = input("Enter an action: ")
        if (action == "open url"):
            url = input("Enter the url you'd like to open: ")
            commands.append("ourl " + url)
        elif (action == "open file"):
            path = input("Enter the path to the file you'd ike to open: ")
            commands.append("ofil " + path)
        elif (action == "done"):
            done = True
        else:
            print("Error: Please enter a valid action.")

    return commands

cmds = createMacro()
for x in cmds:
    action = x[0:4]
    if (action == "ourl"):
        openUrl(x[5:])
    elif (action == "ofil"):
        openFile(x[5:])
