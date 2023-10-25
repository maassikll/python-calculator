import tkinter as tk
import tkinter as ttk
from python_calculator.classes.menuBar import menuBar

class mainPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.instance = menuBar(master)
        self.master = master
        self.pack()

        self.create_widgets()

    def create_widgets(self):
        self.title = ttk.Label(self, text="Welcome Guys !!")
        self.title.pack()
        welcome_message = "Thanks for using my application !!!"
        self.message_label = ttk.Label(self, text=welcome_message)
        self.message_label.pack(pady=20)

        self.derivee_button = ttk.Button(self, text="Derivee", command=self.instance.open_window1)
        self.derivee_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.integrale_button = ttk.Button(self, text="Integrale", command=self.instance.open_window2)
        self.integrale_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.exit_button = ttk.Button(self, text="Quitter", command=self.master.destroy)
        self.exit_button.pack(side=tk.RIGHT, padx=10, pady=10)

