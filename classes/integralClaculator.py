from python_calculator.classes.deriveeCalculator import deriveeCalculator
from python_calculator.functions import *
from tkinter import messagebox


class integraleCalculator(deriveeCalculator):#its simple u neeed to add this
    def __init__(self, root):
        super().__init__(root)
        self.modify_widgets()


    def create_widgets(self):
        super().create_widgets()

    def modify_widgets(self):
        self.submit_button.config(command=self.display_result_integrale)
        self.label.config(text="Here you calculate your Integrale")

        self.entry.unbind('<Return>')
        self.entry.bind('<Return>', lambda event: self.display_result_integrale())

    def display_result_integrale(self):
        super().display_result_derivee()

        try:
            user_input = self.entry.get()
            result_integrale = calcul_integrale(user_input)
            self.result_label.config(text=f"The integral result: {result_integrale}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")



