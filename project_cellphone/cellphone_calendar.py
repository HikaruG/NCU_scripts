import pandas as pd

dict_months={'01':'January',
             '02':'February',
             '03':'March',
             '04':'April',
             '05':'May',
             '06':'June',
             '07':'July',
             '08':'August',
             '09':'September',
             '10':'October',
             '11':'November',
             '12':'December'}

class Calendar(object):
    def __init__(self):
        self.calendars = []

    #record the date(time):event
    def new_calendar(self):
        date = raw_input('date yyyy-mm-dd: ')
        time = raw_input('time hh-hh : ')
        event = raw_input('event : ')
        self.calendars.append([str(date), str(time), str(event)])
        #print "%s (%s) : %s" %(self.date, self.time, self.event)
        self.calendars.sort()

    #print out the current calendar
    def display(self):
        same_month = '0'
        for i in range (len(self.calendars)):
            if same_month != self.calendars[i][0][:-2]:
                same_month = self.calendars[i][0][:-2]
                print "This %s you have those events :" %dict_months[self.calendars[i][0][4:-2]]
            print "The %sth you have %s from %s to %s" %(self.calendars[i][0][-2:],self.calendars[i][2],self.calendars[i][1][:2],self.calendars[i][1][2:])

    def clear(self):
        self.calendars = []

if __name__ == '__main__':
    a = Calendar()
    a.new_calendar()
    a.new_calendar()
    a.new_calendar()
    a.display()
