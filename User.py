# User object
# created on 10/1/2019
# initialized by Aidan Gutierrez
# a "G & G Enterprise" software

class User (object):
    reminders = []
    todaysReminders = []
    name: str
    number: int
    carrier: str
    senderCode: str

    def __init__(self, tname, tnumber, tcarrier):
        self.name = tname
        self.number = tnumber
        self.carrier = tcarrier

    def addMessage(message):
        global reminders
        reminders.add(message)



