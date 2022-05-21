import PySimpleGUI as sg
import numpy as np
from settings import *

ttk_style = 'vista'
class TurnTracker:

    def __init__(self):
        sg.theme('SystemDefaultForReal')
        self.actors = []
        self.actions =  ["Art", "Craft", "Move", "Attack", "Consumable", "Dead"]
        window_layout = [
            [sg.Table(self.actors, headings = ['Name', 'Delay', 'Last Action'], justification = 'center', right_click_menu = ['&Right', ['Remove']], key = '-ACTORS-'), 
            sg.Button(button_text='Begin Combat', key = '-BEGINCOMBAT-')],

            [sg.T(text = 'No Current Actor', key = '-CURRENTACTOR-'), sg.Combo(self.actions, default_value = "Art", key = '-ACTIONS-'), 
            sg.Input(size = 5, key = '-DELAYINPUT-'), sg.Button(button_text = 'Act', use_ttk_buttons=True, key = '-ACTBUTTON-')],

            [sg.Input(size = 8, key = '-NAMEINPUT-'), 
            sg.Input(size=5, key = '-SPDINPUT-'), sg.Button(button_text = 'Add', use_ttk_buttons = True, key = '-ADDACTOR-')]

        ]
        self.in_combat = False
        self.master = sg.Window('Kiseki Turn Tracker', window_layout, ttk_theme=ttk_style)
    
    def add_actor(self, name, spd):
        if spd == "" or name == "":
            print('invalid')
        else:
            if not self.in_combat:
                self._out_combat_add(name, spd)
            else:
                self._in_combat_add(name, spd)
            
            self._update_list()
    
    def _in_combat_add(self, name, spd):
        pass # equation for adding actor in middle of combat
    
    def _out_combat_add(self, name, spd):
        self.actors.append([name,int(spd),"None"])
    
    def _update_list(self):
        self.master['-ACTORS-'].update(self.actors)
        
        if self.in_combat:
            self.master['-CURRENTACTOR-'].update(f'Current Actor: {self.actors[0][0]}')
    
    def begin_combat(self):
        self.actors.sort(key=lambda x: x[1], reverse= True)
        for x in self.actors:
            x[1] = int(100 * 20/x[1])
        
        self.in_combat = True
        self._update_list()
        self.master['-BEGINCOMBAT-'].update(disabled = True)
    
    def act(self, delay, action):
        if delay == "" or action == "":
            print('invalid')
        elif not self.in_combat:
            print('not in combat')
        else:
            pass

    def end_combat(self):
        pass

    def _print_actors(self):
        print(self.actors)

    def start(self):
        while True:
            event, values = self.master.read()

            if event == sg.WIN_CLOSED:
                break

            if event == '-ADDACTOR-':
                self.add_actor(values['-NAMEINPUT-'], values['-SPDINPUT-'])
            
            if event == '-BEGINCOMBAT-':
                self.begin_combat()
            
            if event == '-ACTBUTTON-':
                self.act(values['-DELAYINPUT-'], values['-ACTIONS-'])



if __name__ == "__main__":

    turn = TurnTracker()

    turn.start()
