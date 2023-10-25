import tkinter as tk
from classes.deriveeCalculator import deriveeCalculator
from classes.integralClaculator import integraleCalculator
from classes.menuBar import menuBar
from main_Page.main_page import mainPage


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x200")
    app = menuBar(root)
    app = mainPage(root)
    root.mainloop()
    print("Program closed")
