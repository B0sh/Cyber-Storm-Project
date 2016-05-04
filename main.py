from Tkinter import *
import threading
import time
import random

TEAMS = []
DEFAULT_SCORE = 0
CURRENT_TEAM = 0
ROUNDS = 0
ROUND_DELAY = 12

def createTeams():
    TEAMS.append(Team('GLADOS', DEFAULT_SCORE)) 
    TEAMS.append(Team('CONKER', DEFAULT_SCORE))
    TEAMS.append(Team('SANIC', DEFAULT_SCORE))
    TEAMS.append(Team('FUNKY KONG', DEFAULT_SCORE))
    TEAMS.append(Team('ROB', DEFAULT_SCORE))
    TEAMS.append(Team('BOWSER', DEFAULT_SCORE))
    TEAMS.append(Team('KIRBY', DEFAULT_SCORE))
    TEAMS.append(Team('SHODAN', DEFAULT_SCORE))
    return True

class Team(object):
    def __init__(self, team_name, score):
        self.name = team_name
        self.score = IntVar(window)
        self.score.set(score)

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        
    def setupGUI(self):
        label1 = Label(self.master, text="CYBERSTORM", width=100)
        label1.grid(row=0, column=0, columnspan=4)
        
        gridPosition = {
            'x': 0,
            'y': 1
        }
        for t in TEAMS:
            t.nameLabel = (Label(self.master, text=t.name))
            t.nameLabel.grid(row=gridPosition['y'], column=gridPosition['x'])
            
            t.scoreLabel = Label(self.master, textvariable = t.score)
            t.scoreLabel.grid(row=gridPosition['y']+1, column=gridPosition['x'])

            gridPosition['x'] += 1
            if gridPosition['x'] == 4:
                gridPosition['x'] = 0
                gridPosition['y'] += 2
            window.update_idletasks()

        button1 = Button(self.master, text="1", command=button1action)
        button1.grid(row=6, column=0)
        button2 = Button(self.master, text="2", command=button2action)
        button2.grid(row=6, column=1)
        button3 = Button(self.master, text="3", command=button3action)
        button3.grid(row=6, column=2)
        button4 = Button(self.master, text="4", command=button4action)
        button4.grid(row=7, column=0)
        button5 = Button(self.master, text="5", command=button5action)
        button5.grid(row=7, column=1)
        button6 = Button(self.master, text="6", command=button6action)
        button6.grid(row=7, column=2)

        self.dispTime = IntVar(self.master)
        self.timerLabel = Label(self.master, textvariable=self.dispTime)
        self.timerLabel.grid(row=6, column=3, rowspan=2)

def button1action():
    endTurn()
def button2action():
    endTurn()
def button3action():
    endTurn()
def button4action():
    endTurn()
def button5action():
    endTurn()
def button6action():
    endTurn()

def endTurn():
    global CURRENT_TEAM
    global ROUNDS
    window.update_idletasks()
    TEAMS[CURRENT_TEAM].nameLabel.config(fg="black")
    if CURRENT_TEAM == 7:
        ROUNDS += 1
        CURRENT_TEAM = 0
    else:
        CURRENT_TEAM += 1
    TEAMS[CURRENT_TEAM].nameLabel.config(fg="red")
    timer()

def timer():
    global ROUND_DELAY
    global CURRENT_TEAM
    global ROUNDS
    start = time.time()
    currentRound = [CURRENT_TEAM, ROUNDS]
    dispSec = 0
    while (time.time() - start < ROUND_DELAY and currentRound == [CURRENT_TEAM, ROUNDS]):
        time.sleep(0.1)
        if (time.time() - start != dispSec):
            dispSec = time.time() - start
            app.dispTime.set(dispSec)
            window.update_idletasks()
    
    if (currentRound == [CURRENT_TEAM, ROUNDS]):
        buttons = {
            0: button1action,
            1: button2action,
            2: button3action,
            3: button4action,
            4: button5action,
            5: button6action
        }

        buttons[random.randint(0, 5)]()
        

def startTimer():
    timerThread = threading.Thread(target=timer)
    timerThread.start()

window = Tk()
createTeams()
#window.attributes("-fullscreen", True)
app = App(window)
app.setupGUI()
window.mainloop()
