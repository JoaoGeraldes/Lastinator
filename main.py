# main.py
from tkinter import Tk, PhotoImage
from logic import copy_last_file
from gui import LastinatorGUI

if __name__ == "__main__":
    root = Tk()
    icon = PhotoImage(file="icon.png")
    root.iconphoto(True, icon)
    app = LastinatorGUI(root, copy_last_file)
    root.mainloop()
