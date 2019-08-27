"""
This is the Choice reaction time experience:

- the following experience has 3 different difficulties which the tester will be asked to choose from:
    1st level: 2 boxes of different colors; choose the correct one
    2nd level: 2 boxes and 2 text boxes; Box color, the text's content may vary;
    3rd level: 2 boxes and 2 text boxes; Box's color, the text's content and the text's font may vary;

- this experiment uses a colors.txt file to retrieve the colors used; therefore, one can add their colors:
    one may add more colors if needed, respecting the following rules:
    1. the order for the arguments:
    ColorName RedValue GreenValue BlueValue
    2. The seperator is the space, so either a space or tab is needed between each arguments
    3. One color per line

NB:
1. the black color shouldn't be used because the screen's background color is already black
"""

import numpy as np

from psychopy import visual, event, core, gui
import pandas as pd

# this random function is a random_integers with value exclusions
def random_exc(y, length, x=-1): #y is the value to exclude
    #                         length is the range for the random_integers
    #                         x will be the output of the random int
    #                         x is the last parameter cause sometimes it will not be given
    if x == -1:
        x = np.random.randint(0,length) # if x has no value it takes a random value
    while x==y:
        x = np.random.randint(0, length)
        if x!=y:
            break
    return x

guidict = {"subj_id": "",
           "date": "",
           "difficulty":""}
p_gui = gui.DlgFromDict(guidict,
                               order=["subj_id",
                                      "date",
                                      "difficulty"])

subj_id = p_gui.data[0]
subj_date = p_gui.data[1]
subj_difficulty = p_gui.data[2]
samples = 5

data_path = subj_id +"_" + subj_date + "_lvl_" + subj_difficulty + ".csv" # take the name, the date and the difficulty for the file name

clk = core.Clock()
win = visual.Window(colorSpace='rgb255', color=[0,0,0], size=(1920, 1080), fullscr=False)
mou = event.Mouse()
mou.setPos() # place it at the center of the screen

timings = []
stim_colors = []# which color each stimulus has been atttributed
side = []# which side the tester clicked on
correctness = []
pid = [] # the correct color
list_colors = []
random_lvalue = -1 # the color's index for the left side stimulis
random_rvalue = -1 # the color's index for the right side stimulis
correct_value = -1 # the correct color's index

# this creates the list of colors that will be shown for the experience
with open("colors.txt", "r") as f:
    list_colors = [ color.strip('/n').split() for color in f.readlines()]


text_instructions = visual.TextStim(win,
                                    text='Please click on the colored box of the same color as the instructions \n Press enter to start',
                                    pos=(0,0.7)
                                    )
text_instructions.draw()
win.flip()
event.waitKeys(keyList='return', maxWait=5)

# after each stimulus, a waiting screen will be shown
waiting_box = visual.TextStim(win,
                           text='The next stimus will be shown in 2secondes, press enter to skip',
                           height=0.2)

# the stimuli for the right and left sides:
x_right = 0.5
x_left = -0.5
text_left = visual.TextStim(win,
                            height=0.2,
                            pos=(x_left,0)
                            )

text_right = visual.TextStim(win,
                             height=0.2,
                             pos=(x_right,0)
                             )

rect_left = visual.Rect(win, colorSpace= 'rgb255', height =0.59, width = 0.4, pos=(x_left,0), lineColor = [0,0,0])
rect_left.setLineWidth(5)

rect_right = visual.Rect(win, colorSpace= 'rgb255', height =0.59, width = 0.4, pos=(x_right,0), lineColor = [0,0,0])
rect_right.setLineWidth(5)

object = "word"
color_name = ""

#if the diffuclty is set to 1, only the word itself will be modified
if subj_difficulty == 1:
    random_lvalue_font = 0
    random_rvalue_font = 0
    random_lvalue_rect = 0
    random_rvalue_rect = 0

elif subj_difficulty == 2:
    random_lvalue_rect = 0
    random_rvalue_rect = 0


for i in range(samples):
    mou.setPos()  #  place the mouse cursor at the center of the screen
    #  setting up the variables for the color index
    correct_value = np.random.randint(0,len(list_colors)-1)
    if np.random.randint(2) == True: # randomize the correct answer to be on either right or left side text box
        random_lvalue = correct_value
        random_rvalue= random_exc(random_lvalue, len(list_colors)-1)# the random value is situated at the right side
    else:
        random_rvalue = correct_value
        random_lvalue= random_exc(random_rvalue, len(list_colors)-1)# the random value is situated at the left side
    print "Showing %s... Press any key to continue..." % i

    # a waiting time of 2 secs before every turn
    waiting_box.text = 'Please click on the word : %s' %(list_colors[correct_value][0])
    waiting_box.draw()
    win.flip()
    event.waitKeys(keyList='return', maxWait=2)

    # this segment is for the text boxes :
    text_instructions.text = waiting_box.text
    text_left.text = '%s' % list_colors[random_lvalue][0] # give the text stimulus the 1st value of the list, which is the ColorName
    if subj_difficulty == 3: #the font varies only at level 3
        random_lvalue_font = np.random.randint(1,len(list_colors)-1)# the color of the font can differ from the content
    text_left.setColor(list_colors[random_lvalue_font][1:],'rgb255')
    text_left.height = 0.2
    text_right.text = '%s' % list_colors[random_rvalue][0] # give the text stimulus the 1st value of the list, which is the ColorName
    random_rvalue_font = np.random.randint(1,len(list_colors)-1)# the color of the font can differ from the content
    text_right.setColor(list_colors[random_rvalue_font][1:], 'rgb255')
    text_right.height = 0.2

    # this segment is for the rectangles:
    random_lvalue_rect = random_exc(random_lvalue_font,len(list_colors)-1) # changes the value for the rectangle's color
    rect_left.setFillColor(list_colors[random_lvalue_rect][1:],'rgb255')
    random_rvalue_rect = random_exc(random_rvalue_font,len(list_colors)-1) # changes the value for the rectangle's color
    rect_right.setFillColor(list_colors[random_rvalue_rect][1:],'rgb255')

    # the drawing order should be: first the box, then the text
    rect_left.draw()
    rect_right.draw()
    text_left.draw()
    text_right.draw()
    text_instructions.draw()
    win.flip()
    mou.clickReset()  # necessary to reset the timer of the mouse

    # the data processing part:
    pid.append(list_colors[correct_value][0])
    stim_colors.append([[list_colors[random_lvalue][0],list_colors[random_lvalue_font][0], list_colors[random_lvalue_rect][0]],
                        [list_colors[random_rvalue][0],list_colors[random_rvalue_font][0],list_colors[random_rvalue_font][0]]])
    while True:
        buttons, times = mou.getPressed(getTime = True)
        if not(times[0]):
            continue
        if mou.isPressedIn(rect_left, buttons=[0]):
            print times
            correctness.append(random_lvalue==correct_value)
            side.append("left")
            timings.append(times[0])
            # keep waiting if any button is still pressed
            # while np.any(buttons):
            #  buttons, times = mou.getPressed(getTime=True) # check for mouse click
            break
        elif mou.isPressedIn(rect_right, buttons=[0]):
            print times
            correctness.append(random_rvalue==correct_value)
            side.append("right")
            timings.append(times[0])
            # keep waiting if any button is still pressed
            # while np.any(buttons):
            #   buttons, times = mou.getPressed(getTime=True) # check for mouse click
            break

print 'pid %s, side %s, correctness %s, timings %s, stim_colors %s, \n %s' %(pid, side,correctness,timings, stim_colors,  len(stim_colors))
data = pd.DataFrame({'id': pid,'your side': side ,'Correct': correctness, 'resp time': timings})
data.to_csv(data_path)
win.close()