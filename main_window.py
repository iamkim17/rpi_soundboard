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

        sound_number = 1
        sound_1_label= Tk.Label(self, text="Sound " + str(sound_number), justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=0, column=0, columnspan=2)
       
        sound_1_pin_label = Tk.Label(self, text="Pin", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=1, column=0)

        self.sound_1_pin_name_var = Tk.StringVar()
        self.sound_1_pin_name_var.set(self.model.get_pin_for_sound(1))

        sound_1_pin_option_menu = Tk.OptionMenu(self, self.sound_1_pin_name_var, *model.get_gpio_pin_names(), command=lambda sound_number=sound_number: self.on_choose_sound_pin(1)).grid(sticky=Tk.W, row=1, column=1)

        sound_1_file_label = Tk.Label(self, text="File", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=2, column=0)

        self.sound_1_file_path_var = Tk.StringVar()
        self.sound_1_file_path_var.set(self.model.get_file_path_for_sound(1))

        sound_1_file_path_entry = Tk.Entry(self, textvariable=self.sound_1_file_path_var, state='readonly').grid(sticky=Tk.W, row=2, column=1)
        sound_1_choose_file_button = Tk.Button(self, text="Open", command=lambda sound_number=sound_number: self.on_choose_sound_file(sound_number)).grid(sticky=Tk.W, row=2, column=2)


    def notify(self):
        self.sound_1_file_path_var.set(self.model.get_file_path_for_sound(1))

    def on_about(self):
        about_dialog = AboutDialog(self.root)

        # make window modal
        about_dialog.wait_visibility()
        about_dialog.focus_set()
        about_dialog.grab_set()
        about_dialog.transient(self.root)

    def on_choose_sound_pin(self, sound_number):
        self.model.set_pin_for_sound(sound_number, self.sound_1_pin_name_var.get())

    def on_choose_sound_file(self, sound_number):
        file_path = filedialog.askopenfilename(initialdir="~/Music", title="Select Sound File")

        if file_path != None:
            self.model.set_file_path_for_sound(sound_number, file_path)

