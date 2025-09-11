# main.py
from tkinter import Tk
from logic import copy_last_file
from gui import LastinatorGUI

if __name__ == "__main__":
    root = Tk()
    app = LastinatorGUI(root, copy_last_file)
    root.mainloop()
