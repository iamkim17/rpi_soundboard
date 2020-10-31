try:
    import Tkinter as Tk
    from Tkinter import ttk
except ModuleNotFoundError:
    import tkinter as Tk
    from tkinter import ttk

import ttkthemes
from pathlib import Path
from consts import *

from view import View
from model import Model

from is_raspberry_pi import is_raspberry_pi

class Controller:
    def __init__(self):
        user_dir = Path.home()
        data_path = Path.joinpath(user_dir, '.' + FILE_NAME)

        self.is_raspberry_pi = is_raspberry_pi()

        self.model = Model(data_path)

        # TODO check why not working
        self.root = Tk.Tk()
        self.root.style = ttkthemes.ThemedStyle()
        self.root.style.theme_use('black')

        self.view = View(self.model, self)

    def run(self):
        self.root.title(NAME)
        self.root.deiconify()
        self.root.mainloop()

    def quit(self):
        self.root.quit()
