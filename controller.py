try:
    import Tkinter as Tk
except ModuleNotFoundError:
    import tkinter as Tk

import threading
import time

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
        gpio_polling_thread = threading.Thread(target=self.start_gpio_polling)

        # set as deamon such that the thread is killed when the main thread is killed
        gpio_polling_thread.setDaemon(True) 
        gpio_polling_thread.start()

        self.root.title(NAME)
        self.root.deiconify()
        self.root.mainloop()


    def play_sound(self, sound_number):
        self.sound.play(sound_number)

    def start_gpio_polling(self):
        while True:
            print("blub")
            time.sleep(1)

    def quit(self):
        self.root.quit()
