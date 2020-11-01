try:
    import Tkinter as Tk
except ModuleNotFoundError:
    import tkinter as Tk

from pathlib import Path
from consts import *

from view import View
from model import Model

from is_raspberry_pi import is_raspberry_pi
from sound import Sound

class Controller:
    def __init__(self):
        user_dir = Path.home()
        data_path = Path.joinpath(user_dir, '.' + FILE_NAME)

        self.is_raspberry_pi = is_raspberry_pi()

        self.model = Model(data_path)

        self.sound = Sound(self.model)

        self.root = Tk.Tk()
        self.view = View(self.model, self)

    def run(self):
        self.root.title(NAME)
        self.root.deiconify()
        self.root.mainloop()

    def play_sound(self, sound_number):
        self.sound.play(sound_number)

    def quit(self):
        self.root.quit()
