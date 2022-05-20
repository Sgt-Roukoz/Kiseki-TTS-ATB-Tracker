import PySimpleGUI as sg
from settings import *

ttk_style = 'vista'
class TurnTracker:

    def __init__(self):
        sg.theme('SystemDefaultForReal')
        self.actors = [["Ash", 20, 'None'], ["Sim", 30, 'Attack']]
        self.actions =  ["Art", "Craft", "Move", "Attack", "Consumable", "Dead"]
        window_layout = [
            [sg.Listbox(self.actors, size=(20,10))],
            [],
            []

        ]
        self.master = sg.Window('Kiseki Turn Tracker', window_layout, ttk_theme=ttk_style)
    
    def add_actor(self, name, spd):
        if spd == "" or name == "":
            self.label.config(text = "Invalid Input for Adding Actor")
        else:
            self.actors.append([name,int(spd),"None"])
            self.label.config(text = "")
    
    def print_actors(self):
        print(self.actors)
    
    #def update_listbox(self):

    def read(self):
        self.master.read()



if __name__ == "__main__":

    turn = TurnTracker()

    while True:
        event, values = turn.read()

        if event == sg.WIND_CLOSED:
            break
