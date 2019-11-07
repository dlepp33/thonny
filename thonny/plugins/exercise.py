import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from thonny import get_workbench

class ExerciseView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        txt = ttk.Label(self, text = "Sinu ülesanne:")
        txt.grid(row=0, column=0, padx=50, pady=10)

        ex_txt = tk.Text(self, height=10, width=30, wrap="word")
        ex_txt.grid(row=1, column=0, padx=10, pady=10)
        ex_txt.insert(tk.END,'Kirjutada programm, mis väljastab ekraanile: Tere maailm!\n')

        btn = ttk.Button(self, text="Esita", command=self.on_click)
        btn.grid(row=2, column=0, padx=50, pady=10)
    
    def on_click(self):
        messagebox.showinfo("Info", "Juhuu!!!")
        
def load_plugin():    
    get_workbench().add_view(ExerciseView, "Exercise", "ne")
