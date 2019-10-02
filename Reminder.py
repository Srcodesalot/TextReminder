# reminder object
# created on 10/1/2019
# initialized by Aidan Gutierrez
# a "G & G Enterprise" software
class Reminder (object):

    Title = " "
    Message = " "
    Month = 0
    Day = 00
    time = 0000
    #maybe we will add this however ignore it for now
    Repeatable = False

    def init (title, message, month, day, time):
        global Title
        global Message
        global Month
        global Day
        global Time
        Title = title
        Message = message
        Month = month
        Day = day
        Time = time

    def composedMessage(self):
        composition = self.Title + "\n" + "\n" + self.Message
        print(composition)
