try:
    import Tkinter as Tk
    from Tkinter import filedialog
except ModuleNotFoundError:
    import tkinter as Tk
    from tkinter import filedialog


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

        sound_1_label= Tk.Label(self, text="Sound 1", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=0, column=0, columnspan=2)
       
        sound_1_pin_label = Tk.Label(self, text="Pin", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=1, column=0)

        sound_1_pin_name_var = Tk.StringVar()
        sound_1_pin_name_var.set("Not Assigned");
        sound_1_pin_option_menu = Tk.OptionMenu(self, sound_1_pin_name_var, *model.get_gpio_pin_names()).grid(sticky=Tk.W, row=1, column=1)

        sound_1_file_label = Tk.Label(self, text="File", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=2, column=0)
        sound_1_choose_file_button = Tk.Button(self, text="Open", command=self.on_choose_sound_file).grid(sticky=Tk.W, row=2, column=1)


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

    def on_choose_sound_file(self):
        file_path = filedialog.askopenfile()
        print(file_path)

