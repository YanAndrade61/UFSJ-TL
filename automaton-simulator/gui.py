import tkinter as tk
from automaton import Automaton
import yaml
from tkinter import ttk
from tkinter.messagebox import showinfo
import os

class Gui:

    path = './config_files'

    def __init__(self):

        self.root = tk.Tk()

        # config the root window
        self.root.geometry('300x200')
        self.root.resizable(False, False)
        self.root.title('Automaton simulator')

        # label
        label1 = ttk.Label(text="Please select a automaton:")
        label1.pack(fill=tk.X, padx=5, pady=5)

        # create a combobox
        selected_config = tk.StringVar()
        self.config_cb = ttk.Combobox(self.root, textvariable=selected_config)

        # include config files options
        self.config_cb['values'] = [c for c in os.listdir(self.path) if 'md' not in c]

        # prevent typing a value
        self.config_cb['state'] = 'readonly'

        # place the widget
        self.config_cb.pack(fill=tk.X, padx=5, pady=5)
        
        # bind the selected config changes
        self.config_cb.bind('<<ComboboxSelected>>',self.load_config)

        # label
        label2 = ttk.Label(text="Insert a word to check: ")
        label2.pack(fill=tk.X, padx=5, pady=5)

        # entry
        self.e1 = tk.Entry(self.root)
        self.e1.pack(fill=tk.X, padx=5, pady=5)

        # button
        tk.Button(self.root,
                text = 'verify',
                command = self.process_string).pack(fill=tk.X,
                                                padx=5,
                                                pady=5)
        tk.Button(self.root,
                text = 'verify step by step',
                command = self.init_step).pack(fill=tk.X,
                                                padx=5,
                                                pady=5)


        self.root.mainloop()

    def load_config(self, kwargs):
        with open(f'{self.path}/{self.config_cb.get()}', "r") as f:
            self.config = yaml.safe_load(f)

    def process_string(self):

        # Verify if an automaton was selected
        if len(self.config_cb.get()) < 1:
            showinfo(
                title='Alert',
                message=f'You should select an automaton first!'
            )
            return

        automaton = Automaton(self.config)
        result = automaton.process(self.e1.get())
        
        self.show_result(result)
    
    def init_step(self):
        
        # Verify if an automaton was selected
        if len(self.config_cb.get()) < 1:
            showinfo(
                title='Alert',
                message=f'You should select an automaton first!'
            )
            return

        self.i = 0
        self.process_step_by_step()

    def process_step_by_step(self):
        
        newWindow = tk.Toplevel(self.root)
        
        # config the new window
        newWindow.geometry('300x200')
        newWindow.resizable(False, False)
        newWindow.title('Step-by-step')

        # label string
        string = self.e1.get()
        tmplabel1 = ttk.Label(newWindow, text=f"String: {string}")
        tmplabel1.pack(fill=tk.X, padx=5, pady=5)

        # procedure of symbols
        automaton = Automaton(self.config)  
        result, all_states = automaton.process_step_by_step(string)
        
        # label symbol
        self.tmplabel2 = ttk.Label(newWindow, text=f"Symbol: {string[self.i]}")
        self.tmplabel2.pack(fill=tk.X, padx=5, pady=5)

        # label set
        self.tmplabel3 = ttk.Label(newWindow, text=f"Active states: {all_states[self.i]}")
        self.tmplabel3.pack(fill=tk.X, padx=5, pady=5)

        # button
        tk.Button(newWindow,
                text = 'process',
                command = lambda: self.increment(string,all_states,result)).pack(fill=tk.X,
                                                                             padx=5,
                                                                             pady=5)

    def increment(self,string, all_states, result):
        self.i+=1
        if self.i < len(string):
            self.tmplabel2.config(text = f"Symbol: {string[self.i]}")
            self.tmplabel3.config(text = f"Active states: {all_states[self.i]}")
        else:
            self.show_result(result)

    def show_result(self, result: bool):

        msg = ('Belezeira' if result else 'Não aceita')
        showinfo(
            title = 'Result',
            message = f'String: {self.e1.get()}\n{msg}'
        )



Gui()
