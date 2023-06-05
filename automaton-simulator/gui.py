import tkinter as tk
from automaton import Automaton
import yaml
from tkinter import ttk
from tkinter.messagebox import showinfo
import os

class Gui:

    path = './config_files'

    def __init__(self):

        root = tk.Tk()

        # config the root window
        root.geometry('300x200')
        root.resizable(False, False)
        root.title('Automaton simulator')

        # label
        label1 = ttk.Label(text="Please select a automaton:")
        label1.pack(fill=tk.X, padx=5, pady=5)

        # create a combobox
        selected_config = tk.StringVar()
        self.config_cb = ttk.Combobox(root, textvariable=selected_config)

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
        self.e1 = tk.Entry(root)
        self.e1.pack(fill=tk.X, padx=5, pady=5)

        # button
        tk.Button(root,
                text = 'verify',
                command = self.process_string).pack(fill=tk.X,
                                                padx=5,
                                                pady=5)

        tk.Button(root,
                text = 'verify step by step',
                command = self.process_string).pack(fill=tk.X,
                                                padx=5,
                                                pady=5)


        root.mainloop()

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

    def process_step_by_Step(self):
        pass

    
    def show_result(self, result: bool):

        msg = ('Belezeira' if result else 'Não aceita')
        showinfo(
            title = 'Result',
            message = f'String: {self.e1.get()}\n{msg}'
        )



Gui()
