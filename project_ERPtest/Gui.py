from psychopy import gui
import os


class Gui(object):
    def __init__(self):
        self.data_name= ''
        self.data_path = ''
    def init(self):
        guidict = {"subj_id": "",
           "date": "",
           "difficulty":"",
           "samples(number)":""}
        p_gui = gui.DlgFromDict(guidict,
                               order=["subj_id",
                                      "date",
                                      "difficulty",
                                      "samples(number)"])

        self.subj_id = p_gui.data[0]
        self.subj_date = p_gui.data[1]
        self.subj_difficulty = int(p_gui.data[2]) #this value needs to be an int
        samples = int(p_gui.data[3])

        if not(os.path.exists(self.subj_id)): #create a directory for each participant
            os.mkdir(self.subj_id)
        self.data_name = self.subj_id +"_" + self.subj_date + "_lvl_" + str(self.subj_difficulty) + ".csv" # take the name, the date and the difficulty for the file name
        self.data_path = os.path.join(self.subj_id,self.data_name)


if __name__ == '__main__':
    from psychopy import gui
    import os
    gui = Gui()
    print gui.date, gui.data_path