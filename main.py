# reminder object
# created on 10/1/2019
# Created by Aidan Gutierrez and Josh Graf
# A "G & G Enterprise" software
from Reminder import Reminder
from User import User
reminders = []
todaysReminders = []
phoneBook = {}
user = User
def main():
    global user
    print("~TEXT REMINDER~\n")
    print("Welcome to the text reminder!")
    print("To get started please enter your phone number")
    number = input("Format(xxxxxxxxxx):")
    try:
        if phoneBook[number]:
            print("is user")
    except:
        print("looks like you are'nt registered yet")
        print("follow the prompts and we'll get you all setup \n")
        addUser()
        ##eventually well need saftey mesures to ensure the number is real (probably by length)
    print("welcome " + user.name)
    print("To create a reminder please type 'new' ")
    print("To terminate the program please type 'close' ")
    print("for help or information please type 'info")
    command = input(" :")
    while command != "terminate":
        if command.casefold() == "close":
            termPrompt()
        elif command.casefold() == "info":
            # write some definition of the program here along with some commands
            print("test definition")
        elif command.casefold() == "new":
            #create a new reminder
            createStore()
        else:
            print ("error")
        command = input(" :")
    print(user.reminders)

def termPrompt():
    print("")
    print("::WARNING::")
    print("if you choose to exit this will delete all reminders meaning none will be sent")
    print("Are You sure you want to do this yes/no ")
    conformation = input(" :")
    if conformation.casefold() == "yes":
        exit(0)
    else:
        return

def createStore ():
    #prompt user to make reminder adding all parameters
    #store reminder in array
    rem = Reminder

    print ("TEST")

def dayTimer():
    # check the date and time and then set a timer that ends at midnight (basicallly sorting)
    # then this function will load the Queue and then run again at the begining of every day
    # if the event isnt repeatable delete it
    print("TEST DAYTIMER")

def textTimer():
    print("TEST TEXTTIMER")

def sendText():
    print("TEXT")

def addUser():
    global phoneBook
    global user
    number = input("please enter your Phone number:")
    carrier = input("please enter your carrier (ex. T-mobile, AT&T):")
    name = input("please enter your name:")
    newUser = User
    newUser.__init__(newUser,name, number, carrier)
    user = newUser
    phoneBook[number] = newUser
    print("")
    return

def removeRem():
    print ("remove")

rem = Reminder
main()
