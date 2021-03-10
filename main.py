import datetime
import webbrowser
import os

# Welcome message
d = datetime.datetime.now()
print("Welcome back, today is " + d.strftime("%A") + ", " + d.strftime("%B") + " " + d.strftime("%d"))

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
    macroFile = open("macros/" + nameOfMacro + ".txt", "w")
    while (done != True):
        action = input("Enter an action: ")
        if (action == "open url"):
            url = input("Enter the url you'd like to open: ")
            macroFile.write("ourl\n")
            macroFile.write(url + "\n")
        elif (action == "open file"):
            path = input("Enter the path to the file you'd ike to open: ")
            macroFile.write("ofile\n")
            macroFile.write(path + "\n")
        elif (action == "done"):
            done = True
        else:
            print("Error: Please enter a valid action.")

# Open file and run commands
def runMacros(macro):
    with open(macro) as file:
        while True:
            command = file.readline().rstrip()
            action = file.readline().rstrip()
            if command == '':
                break
            else:
                if (command == "ourl"):
                    openUrl(action)
                elif (command == "ofile"):
                    openFile(action)
                else:
                    print("Something went wrong.")
                    break