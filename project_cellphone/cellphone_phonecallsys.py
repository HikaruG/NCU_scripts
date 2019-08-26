import pandas as pd

class Phonecallsys(object):
    def __init__(self,phone_location):
        self.phone_location = phone_location
        self.country_codes =pd.read_excel("country_codes.xls").dropna()
        # this first opens the xcl file to a dataframe, then will erase all the rows that has at least 1 argument missing
        # then finally puts the dataframe into the country_codes variable

    def dial(self):
        call_num = raw_input("please insert the phone number you want to call... ")
        calling_from = self.phone_location
        if call_num[0] == '+':
            region_num = call_num[:len(call_num)-9] #this will take the region code from the phone number
            #this will check which country you are calling to with the country_codes dataframe, the output will be a series
            dt_result = self.country_codes.Country[self.country_codes.InternationalDialing == region_num]
            calling_to = dt_result.tolist()[0] #this change the data type from a series to a string
        else:
            calling_to = calling_from
        print 'You are calling from %s to the number: %s which is located in %s' %(calling_from,call_num,calling_to)


if __name__ == '__main__':
    import pandas as pd
    phone_test = Phonecallsys('Taiwan')
    phone_test.dial()
