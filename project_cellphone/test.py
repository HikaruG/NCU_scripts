#this is a python test file 

from psychopy import event, core
clk = core.Clock()

a_list = []
a = []

while 1:
    a = event.getKeys()
    print a
    if len(a) > 0:
        print a
        break
print a
