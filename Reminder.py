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

    def composedMessage(self):
        composition = self.Title + "\n" + "\n" + self.Message
        print(composition)

    def setTitle(title):
        global Title
        Title = title

    def setMessage(message):
        global Message
        Message = message

    def setMonth(month):
        global Month
        Month = month

    def setDay(day):
        global Day
        Day = day

    def setTime(time):
        global Time
        Day = Time
