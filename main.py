import tkinter as tk    

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x300")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="Hello DIP01", font=("Arial", 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", width=5, height=2)
        self.button.place(x=40, y=40)

        self.button = tk.Button(self.root, text="+/-", width=5, height=2)
        self.button.place(x=85, y=40)
        
        self.button = tk.Button(self.root, text="%", width=5, height=2)
        self.button.place(x=130 ,y=40)

        self.root.mainloop()

MyCalculator()