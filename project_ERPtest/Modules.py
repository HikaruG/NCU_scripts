"this file will contain every function used in the project"
import numpy as np

def random_exc(length,y1,y2 = -1, x=-1): #y is the value to exclude
    #                         length is the range for the random_integers
    #                         x will be the output of the random int
    #                         x is the last parameter cause sometimes it will not be given
    if x == -1:
        x = np.random.randint(0,length) # if x has no value it takes a random value
    if y2 ==-1:
        while x==y1:
            x = np.random.randint(0, length)
            if x!=y1:
                break
        return x
    else:
        while x==y1 | x==y2:
            x = np.random.randint(0, length)
            if x!=y1 & x!=y2:
                break
        return x