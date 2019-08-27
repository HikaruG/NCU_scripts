import numpy as np
import Modules.py as mod
reload(mod)

class Datas(object):
    def __init__(self):
        self.list_colors = []
        self.timings = []
        self.stim_colors = []  # which color each stimulus has been attributed
        self.side = []  # which side the tester clicked on
        self.correctness = []
        self.pid = []  # the correct color
        self.list_colors = []
        self.random_lvalue = -1  # the color's index for the left side stimulus
        self.random_rvalue = -1  # the color's index for the right side stimulus
        self.correct_value = -1  # the correct color's index
        self.random_lvalue_font = 0 #the left word's font color
        self.random_rvalue_font = 0 #the right word's font color
        self.random_lvalue_rect = 0 #the left box font color
        self.random_rvalue_rect = 0 #the right box font color
        self.dict_values = {}

    def init_values(self,difficulty):
        # this creates the list of colors that will be shown for the experience
        with open("colors.txt", "r") as f:
            self.list_colors = [color.strip('/n').split() for color in f.readlines()]
        if difficulty == 1:
            self.random_lvalue_font = 0
            self.random_rvalue_font = 0
            self.random_lvalue_rect = 1
            self.random_rvalue_rect = 1
        elif difficulty == 2:
            self.random_lvalue_font = 0
            self.random_rvalue_font = 0


    def update_values(self,difficulty):
        self.correct_value = np.random.randint(0, len(self.list_colors) - 1)
        left_true = np.random.randint(2) # randomize the correct answer, if true => the left side will have the correct output
        if left_true:
            self.random_lvalue = self.correct_value
            self.random_rvalue = mod.random_exc(len(self.list_colors) - 1
                                                ,self.random_lvalue)  # the random value is situated at the right side
        else:
            self.random_rvalue = self.correct_value
            self.random_lvalue = mod.random_exc(len(self.list_colors) - 1,
                                                self.random_rvalue)  # the random value is situated at the left side

        if difficulty == 3:
            self.random_lvalue_font = np.random.randint(1, len(
                self.list_colors) - 1)  # the color of the font can differ from the content
            self.random_rvalue_font = np.random.randint(1, len(
                self.list_colors) - 1)  # the color of the font can differ from the content

        if difficulty == 2 | difficulty == 3:
            self.random_lvalue_rect = mod.random_exc(len(self.list_colors) - 1,
                                                self.random_lvalue_font)  # changes the value for the rectangle's color
            self.random_rvalue_rect = mod.random_exc(len(self.list_colors) - 1,
                                                self.random_rvalue_font)  # changes the value for the rectangle's color
        if difficulty == 4:
            rect_bait = np.random.randint(2)
            if left_true:
                self.random_lvalue_font = mod.random_exc(len(self.list_colors) - 1,
                                                         self.random_lvalue)  # the color of the font differs from the content
                self.random_lvalue_rect = mod.random_exc(len(self.list_colors) - 1,
                                                         self.random_lvalue,
                                                         self.random_lvalue_font) # the color of the rect differs from the content + the font
                if rect_bait:
                    self.random_rvalue_rect = self.correct_value
                    self.random_rvalue_font = mod.random_exc(len(self.list_colors) - 1,
                                                         self.random_rvalue_rect) # the color of the font differs from the rectangle
                else:
                    self.random_rvalue_font = self.correct_value
                    self.random_rvalue_rect = mod.random_exc(len(self.list_colors) - 1,
                                                             self.random_rvalue_font)  # the color of the font differs from the rectangle
            else:





if __name__ == '__main__':
    import numpy as np
    import Modules.py as mod
    reload(mod)

    ex_datas = Datas()
    ex_datas.init_values(1)
    print "this is the right rectangle's font color: ", ex_datas.random_rvalue_rect
    print "this is the right word's font color: ", ex_datas.random_rvalue_font

    ex_datas.init_values(2)
    print "this is the right word's font color: ", ex_datas.random_rvalue_font

    ex_datas.update_values(3)
