from python_calculator.functions import *
import tkinter as tk
from tkinter import messagebox

class deriveeCalculator:
    def __init__(self, root):

        self.root = root
        self.root.title("Calcul All")
        self.create_widgets()


    def create_widgets(self):

        self.label1 = tk.Label(self.root, text="Enter your function")
        self.label1.grid(row=0, column=0, pady=5)
        self.label = tk.Label(self.root, text = "Here you calculate your derivee ")
        self.label.grid(row=1,column=0,pady=10)

        # Create an Entry widget for input
        self.entry = tk.Entry(self.root, width=50)
        self.entry.grid(row=2, column=0, pady=10, padx=50)

        # Create a Button to submit the input
        self.submit_button = tk.Button(self.root, text="Submit", command=self.display_result_derivee)
        self.submit_button.grid(row=4, column=0, pady=5)

        # Create a Label to display the result
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, pady=10)

        self.entry.bind('<Return>', lambda event: self.display_result_derivee())
    # def open_new_window(self):
    #     new_window = tk.Toplevel(self.root)
    #     new_window.title("new window")
    #     label = tk.Label(new_window, text="This is a new window!")
    #     label.pack(pady=10)

    def display_result_derivee(self):
        user_input = self.entry.get()
        try:
            result_derv = calcul_derivee(user_input)
            self.result_label.config(text=f"The derivative result: {result_derv}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")






