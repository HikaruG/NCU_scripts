class Contact(object):
    def __init__(self):
        self.contacts = []

    def new_contact(self):
        name = raw_input('please insert the name : ')
        number = raw_input('please  insert the number : ')
        self.contacts.append([name,number])

    def display(self):
        print 'here is the list of your current contacts: \n %s'%self.contacts

    def del_contact(self):
        print 'here is your current contacts :\n', self.contacts
        res = raw_input('please give the name of the contact you want to delete ... :')
        if res == 'all':
            self.contacts = []
        for i in range(len(self.contacts)):
            if self.contacts[i][0] == res:
                self.contacts.pop(i) #this will delete the list which index is i
                break

if __name__ == '__main__':
    contact = Contact()
    contact.new_contact()
    contact.new_contact()
    contact.display()
    contact.del_contact()

