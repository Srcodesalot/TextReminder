# reminder object
# created on 10/1/2019
# Created by Aidan Gutierrez and Josh Graf
# A "G & G Enterprise" software
from Reminder import Reminder
reminders = []
todaysReminders = []
phoneBook = []

def main():
    print("~TEXT REMINDER~\n")
    print("Welcome to the text reminder!")
    print("To create a reminder please type 'new' ")
    print("To terminate the program please type 'close' ")
    print("for help or information please type 'info")
    command = input(" :")
    while command != "terminate":
        if command == "close":
            termPrompt()
        elif command == "info":
            # write some definition of the program here along with some commands
            print("test definition")
        elif command == "new":
            #create a new reminder
            createStore()
        else:
            print ("error")
        command = input(" :")

def termPrompt():
    print("::WARNING::")
    print("if you choose to exit this will delete all reminders meaning none will be sent")
    print("Are You sure you want to do this yes/no ")
    conformation = input(" :")
    if conformation == "yes":
        exit(0)
    else:
        return

def createStore ():
    #prompt user to make reminder adding all parameters
    #store reminder in array
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

def addNumber():
    print("adds number")

rem = Reminder
rem.composedMessage(rem)
main()
