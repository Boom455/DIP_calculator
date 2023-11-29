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

        self.button = tk.Button(self.root, text="/", width=5, height=2)
        self.button.place(x=175 ,y=40)

        self.button = tk.Button(self.root, text="7", width=5, height=2)
        self.button.place(x=40 ,y=80)

        self.button = tk.Button(self.root, text="8", width=5, height=2)
        self.button.place(x=85 ,y=80)

        self.button = tk.Button(self.root, text="9", width=5, height=2)
        self.button.place(x=130 ,y=80)

        self.button = tk.Button(self.root, text="*", width=5, height=2)
        self.button.place(x=175 ,y=80)

        self.button = tk.Button(self.root, text="4", width=5, height=2)
        self.button.place(x=40 ,y=120)

        self.button = tk.Button(self.root, text="5", width=5, height=2)
        self.button.place(x=85 ,y=120)

        self.button = tk.Button(self.root, text="6", width=5, height=2)
        self.button.place(x=130 ,y=120)

        self.button = tk.Button(self.root, text="-", width=5, height=2)
        self.button.place(x=175 ,y=120)

        self.button = tk.Button(self.root, text="1", width=5, height=2)
        self.button.place(x=40 ,y=160)

        self.button = tk.Button(self.root, text="2", width=5, height=2)
        self.button.place(x=85 ,y=160)

        self.button = tk.Button(self.root, text="3", width=5, height=2)
        self.button.place(x=130 ,y=160)

        self.button = tk.Button(self.root, text="+", width=5, height=2)
        self.button.place(x=175 ,y=160)

        self.button = tk.Button(self.root, text="0", width=12, height=2)
        self.button.place(x=40 ,y=200)

        self.button = tk.Button(self.root, text=".", width=5, height=2)
        self.button.place(x=130 ,y=200)

        self.button = tk.Button(self.root, text="=", width=5, height=2)
        self.button.place(x=175 ,y=200)
        self.root.mainloop()

MyCalculator()