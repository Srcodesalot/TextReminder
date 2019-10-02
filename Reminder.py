# reminder object
# created on 10/1/2019
# initialized by Aidan Gutierrez
# a "G & G Enterprise" software
class Reminder (object):

    title: str
    message: str
    month: str
    day: str
    time: int
    #maybe we will add this however ignore it for now
    Repeatable = False

    def __init__(self, t, msg, mo, d, tme):
        self.title = t
        self.message = msg
        self.month = mo
        self.day = d
        self.time = tme

    def composedMessage(self):
        composition = self.Title + "\n" + "\n" + self.Message
        print(composition)
