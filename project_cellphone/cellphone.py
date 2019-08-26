import cellphone_phonecallsys
reload(cellphone_phonecallsys)
import cellphone_calendar
reload(cellphone_calendar)
import cellphone_contact
reload(cellphone_contact)

class Cellphone(object):
    def __init__(self, phone_id, phone_num,phone_location):
        self.phone_id = phone_id
        self.phone_num = phone_num
        self.phone_location = phone_location
        self.calls = cellphone_phonecallsys.Phonecallsys(phone_location)
        self.contacts = cellphone_contact.Contact()
        self.calendar = cellphone_calendar.Calendar()

    def startup(self): #this startup method will generate the dict for the operations
        print 'Starting up the process... '
        #self.contacts =
        #self.calendar =
        self.operations = {1:'You selected the operation : PhoneCall',
                           2:'You selected the operation : Contacts',
                           3:'You selected the operation : Calendar'
                           }
        self.calloperations = {1: self.calls.dial,
                               2: "hello its not done yet... "}
        self.contactoperations = {1: self.contacts.new_contact,
                                   2: self.contacts.display,
                                   3: self.contacts.del_contact}

        self.calendaroperations = {1: self.calendar.new_calendar,
                                   2: self.calendar.display,
                                   3: self.calendar.clear}
        print 'Welcome back %s!' %self.phone_id


    def choose_operation(self):
        sel_op = -1 #reset of the variable
        sel_op = int(raw_input("please choose the action you want to operate...\n" \
              "1. Phonecall \n" \
              "2. Contacts \n" \
              "3. Calendar \n"
              "Your input: "))
        print self.operations[sel_op]
        self.sel_op = sel_op

    def processing(self):
        if self.sel_op == 1:
            option = int(raw_input('please select how you want to make the phonecall ... \n'
                      '1. From dial\n'
                      '2. From contacts\n'
                      'Your input: '))
            self.calloperations[option]()

        elif self.sel_op == 2:
            option = int(raw_input('please select what you want to do with the contacts ... \n'
                      '1. Add a new contact\n'
                      '2. Check your current contacts\n'
                      '3. delete a contact\n'
                      'Your input: '))
            self.contactoperations[option]()
        elif self.sel_op == 3:
            option = int(raw_input('please select what you want to do with the calendar ... \n'
                      '1. Add a new event\n'
                      '2. Check your current calendar\n'
                      '3. clear the calendar\n'
                      'Your input: '))
            self.calendaroperations[option]()


if __name__ == '__main__':
    oppo = Cellphone('OppoR15','0686907924','Taiwan')
    oppo.startup()
    while 1:
        oppo.choose_operation()
        oppo.processing()
        oppo.processing()
        oppo.choose_operation()
        oppo.processing()
        oppo.processing()


