#main.py
import tkinter as tk
from gui import TrussApp

if __name__ == "__main__":
    root = tk.Tk()
    app = TrussApp(root)
    root.mainloop()

