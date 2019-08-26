# storing contact
"""
data = {
'name':['Mary', 'David', 'James', 'Dorothy', 'Michelle'],
'phone number':['0912600035', '09876256284', '0978394723', '0964758342', '0956354121']}

class contact(object):

    def __init__(self,name,number):
        self.name = name
        self.number = number

        print ('name: %s, phone number: %s ')%(self.name, self.number)
"""

class Contact():
    name_list = []
    def __init__(self, name, number):
        Contact.name_list.append(self)
        self.name = name
        self.number = number

    def __str__(self):
        return "Name: {} || Phone number: {}".format(self.name, self.number)

#again for output formatting
def update(): print([str(contact) for contact in Contact.name_list])

update()
Contact("Mary","0912600035")
Contact("David","09876256284")
Contact("James","0978394723")
Contact("Dorothy","0964758342")
Contact("Michelle","0956354121")
update()
