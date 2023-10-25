import tkinter as tk
from python_calculator.classes.deriveeCalculator import deriveeCalculator
from python_calculator.classes.integralClaculator import integraleCalculator


class menuBar:
    def __init__(self,root):
        self.root = root
        self.root.title("Main Window")

        #Menu Bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)



        # Create File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Derivee", command=self.open_window1)


        # Create Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)



#For each type of calcul a specific window

    def open_window1(self):
        window1 = tk.Toplevel(self.root)
        window1.title("Window 1")
        calcul_derivee1 = deriveeCalculator(window1)

    def open_window2(self):
        window2 = tk.Toplevel(self.root)
        window2.title("Window 2")
        calcul_integrale1 = integraleCalculator(window2)




