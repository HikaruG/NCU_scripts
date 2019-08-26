"""
this demo will be done in 2 steps:
1- create a morse code transmitter; with the led + buzzer
2- create a morse code receiver; with light sensor + microphone

"""

import pyfirmata2 as pfm
import numpy as np
import sys

from psychopy import visual, event, core, gui
import psychopy.gui
import pandas as pd
from collections import defaultdict

dict_morsepng = {"blank": "blanck.png",
                    "separator": "seperator.png",
                    "dot": "dot.png",
                    "dash":"dash.png"
                    }

dict_morsedecoder = {"dotdash" : "a",
                     "dashdotdotdot" : 'b',
                     "dashdotdashdot" : 'c',
                     "dashdotdot": 'd',
                     "dot": 'e',
                     "dotdotdashdot":'f',
                     "dashdashdot":'g',
                     "dotdotdotdot":'h',
                     "dotdot":'i',
                     "dotdashdashdash":'j',
                     "dashdotdash":'k',
                     "dotdashdotdot":'l',
                     "dashdash":'m',
                     'dashdot':'n',
                     'dashdashdash':'o',
                     'dotdashdashdot':'p',
                     "dashdashdotdash":'q',
                     "dotdashdot":"r",
                     "dotdotdot":'s',
                     "dash":'t',
                     "dotdotdash":'u',
                     "dotdotdotdash":'v',
                     "dotdashdash":'w',
                     "dashdotdotdash":'x',
                     "dashdotdashdash":'y',
                     "dashdashdotdot":'z'
                     }

dict_morsedecoder = defaultdict(lambda: "error",dict_morsedecoder)

morse_unit = 0.3
seperator_unit = morse_unit * 6

#this function will serve as a decorder that will determine whether the recorded signal is a:
#1. dot (1 unit ON value)
#2. blank (1 unit OFF value)
#3. dash (3 units ON value)
#4. separator (3 units OFF value)
def time_to_morse(times,states):
    if len(times) != len(states):
        print "error, please redo your recording..."
        return -1
    message = []
    for i in range (len(states)):
        if states[i]:
            if times[i] > 3 * morse_unit:
                message.append("dash")
            else:
                message.append("dot")
        else:
            if times[i] > seperator_unit:
                message.append("seperator")
            #else:#maybe this else condition is unecessary, we only need to keep in track the seperator
                #message.append("blank")
    return message

debug_letter = ''
#this function will decode the recording to a letter/word
def morse_decoder(recording):
    word = []
    letter = ''
    for i in range(len(recording)):
        if recording[i] =='seperator':
            if not(len(letter)): #if the letter variable is a empty list, it's skips the value => if the 1st input was put after 3secs
                continue
            debug_letter = dict_morsedecoder[letter]
            word.append(debug_letter)
            #word.append(dict_morsedecoder[letter])
            print letter,'\n'
            letter = ''
            continue
        letter += recording[i]
        if i == len(recording)-1:
            #word.append(dict_morsedecoder[letter])
            debug_letter =dict_morsedecoder[letter]
            word.append(debug_letter)
    return word


try:
    #setting up the digital pins
    board = pfm.Arduino(pfm.Arduino.AUTODETECT)  # this line detects the COM on which the arduino is connected
    PIN_Button = int(raw_input("please input the pin number for the Button: "))
    PIN_LED = int(raw_input("please input the pin number for the LED: "))
    PIN_PIEZO = board.get_pin('d:6:p') # set digital pin 6 to PWM mode
    PIN_Rotator= 0
    threshold_rotator = 0.8

    it = pfm.util.Iterator(board)  # required for all reading
    it.start()  # required for all reading

    din_button = board.digital[PIN_Button]
    din_button.mode = pfm.INPUT  # alternative way to set the reading/writing mode
    dout_light = board.digital[PIN_LED]
    din_rotator = board.analog[PIN_Rotator]
    din_rotator.enable_reporting() #required for reading
    #setting up the experiment windows
    clk = core.Clock()
    current_state = False; previous_state = False;
    times = []
    state= []
    win = visual.Window(size=(1920, 1080), fullscr=False)

    text_box = visual.TextStim(win,pos= [0,0.9],
                               text='Please create your own morse code based on this graph',
                               height=0.1)
    text2_box = visual.TextStim(win,pos= [0,-0.8],
                               text='Conditions : \n'
                                    '1. An unit = 0.3sec\n'
                                    '2. blank of 10 units or more = separator',
                               height=0.08)

    picture_box = visual.ImageStim(win,'morse_code.png')
    picture_box.draw()
    text_box.draw()
    text2_box.draw()
    win.flip()


    print("Attempt to read from %s (D%d)" % (board.name, PIN_Button))
    code_length = int(raw_input("Please input the number of letter you want to create : "))
    seperator_count = 0
    while seperator_count - 1 < code_length:
        current_state = False; previous_state = False
        t0 = clk.getTime()
        if(din_rotator.read() >= threshold_rotator):
            print "you can now record your morse code... recording..."
        while din_rotator.read() >= threshold_rotator:
            if seperator_count - 1 >= code_length:
                break
            current_state = din_button.read()
            if din_button.read():
                dout_light.write(1)
            else:
                dout_light.write(0)
            if current_state != previous_state:
                #this section gets the necessary info to recreate a list of the ON-OFF states and their durations
                t1 = clk.getTime() #gets the duration of one state
                if t1 - t0 > morse_unit: #if the duration of the pressed putton is under 0.3s, we don't consider it as a valid signal
                    times.append(t1-t0)
                    state.append(previous_state)#stocks the current state
                    t0 = t1 #updates the t0 to get the next duration of the state
                    if not (state[-1]):
                        t2 = clk.getTime()
                        if times[-1] > morse_unit * 6:
                            seperator_count += 1
                    previous_state = current_state #the shift between high and low are only counted when the state duration is over 1s
        #if t0 > 10:
        #    break #if the timer goes above this value, it automatically ends the recording

    text_box.text = 'Now lets try to reproduce your morse code, shall we ?'
    text_box.draw()
    win.flip()
    text_box.draw()#don't know why but needs to be drawn twice ...
    win.flip()

    #this section is for the sound output
    for i in range (len(times)):
        clk.reset()
        while clk.getTime() < times[i]:
            if state[i]:
                PIN_PIEZO.write(1)
            else:
                PIN_PIEZO.write(0)
                if clk.getTime() > 1: #if there is a blank, just stop for 1sec and move on => speeding the process
                    break
    PIN_PIEZO.write(0)

    #this section is for the recording and printing it out with a stimulus:
    recording = time_to_morse(times,state)
    text_box.text = 'So, you sent me this following message, right ?'
    text_box.draw()
    result_morse = visual.TextStim(win)
    result_morse.text = morse_decoder(recording)  #
    result_morse.draw()
    win.flip()
    text_box.draw()
    result_morse.draw()
    win.flip()
    event.waitKeys(keyList='return',maxWait=5)

    #tried to print out the dots and dashes as stimuli, but couldn't find a good way, other than creating the same amount
    #of ImageStim as the length of message... Which is too forced so didn't implemented it
    """
    record_length = len(recording)
    xs = []
    image_size = 0.1
    x_minus = [-1*image_size*i for i in reversed(range (record_length/2))] #makes the first half of the xs, the order is reversed to get the lowest x value as the first value
    x_plus = [1*image_size*i for i in range (record_length/2)]#second half of the xs
    xs = x_minus + x_plus #add the 2 lists to make the final real list of x values for the stimuli

    for i_letter in range(record_length):
        result_morse = visual.ImageStim(win, pos=(xs[i_letter],0))
        result_morse.tex = dict_morsepng[recording[i_letter]] #this will give the path to the image according to the value of the letter
        result_morse.draw()
        print "the image box should be now drawn"
    #win.flip()
    """

except KeyboardInterrupt:
    print('\nGoodbye!')

finally:
    board.exit()  # release the digital pin
    win.close()
