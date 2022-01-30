import tkinter as tk
from time import strftime

class App():
    
    def __init__(self):
        self.main_window = tk.Tk()
        
        self.lbl = tk.Label(self.main_window, font = ('calibri', 40, 'bold'))
        self.lbl.pack(anchor=tk.CENTER)
        self.time()
        self.main_window.mainloop()


    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text = string)
        self.lbl.after(1000, self.time)



if __name__ == '__main__':
    app = App()