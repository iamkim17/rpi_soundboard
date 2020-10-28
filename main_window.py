try:
    import Tkinter as Tk
except ModuleNotFoundError:
    import tkinter as Tk


from consts import *
from about_dialog import AboutDialog

import copy

class MainWindow(Tk.Frame):
    def __init__(self, model, root):

        self.model = model
        self.model.register_observer(self)

        self.root = root

        Tk.Frame.__init__(self, self.root)

        self.pack(fill="both", expand=True)

        self.menubar = Tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        
        # file menu
        file_menu = Tk.Menu(self.menubar)
        file_menu.add_command(label="About", command=self.on_about)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)

        self.menubar.add_cascade(label="File", menu=file_menu)

    def notify(self):
        None
        # TODO

    def on_about(self):
        about_dialog = AboutDialog(self.root)

        # make window modal
        about_dialog.wait_visibility()
        about_dialog.focus_set()
        about_dialog.grab_set()
        about_dialog.transient(self.root)
