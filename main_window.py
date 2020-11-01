try:
    import Tkinter as Tk
    from Tkinter import ttk
    from Tkinter import filedialog
    from Tkinter import scrolledtext
except ModuleNotFoundError:
    import tkinter as Tk
    from tkinter import ttk
    from tkinter import filedialog
    from tkinter import scrolledtext

from consts import *
from about_dialog import AboutDialog
from frame_with_scroll_bar import FrameWithScrollBar

class MainWindow(Tk.Frame):
    def __init__(self, model, root):

        self.model = model
        self.model.register_observer(self)

        self.root = root
        self.root.minsize(395, 372)

        Tk.Frame.__init__(self, self.root)

        self.menubar = Tk.Menu(self.master)
        self.master.config(menu=self.menubar)

        
        # file menu
        file_menu = Tk.Menu(self.menubar)
        file_menu.add_command(label="About", command=self.on_about)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=self.root.quit)

        self.menubar.add_cascade(label="File", menu=file_menu)

        self.sound_file_path_vars = [Tk.StringVar() for i in range(self.model.get_num_sounds())] 
        self.sound_pin_name_vars = [Tk.StringVar() for i in range(self.model.get_num_sounds())]

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.sound_file_path_vars = [Tk.StringVar() for i in range(self.model.get_num_sounds())] 
        self.sound_pin_name_vars = [Tk.StringVar() for i in range(self.model.get_num_sounds())]
        self.sound_pin_option_menus = []

        sounds_frame = FrameWithScrollBar(self.root)
        sounds_frame.frame.columnconfigure(1, weight=1)

        sounds_frame.pack(expand=True, fill=Tk.BOTH)

        row_counter = 0

        for sound_number in range(1,self.model.get_num_sounds()+1):
            # sound number
            sound_label= Tk.Label(sounds_frame.frame, text="Sound " + str(sound_number), justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=row_counter+0, column=0, columnspan=3)

            # sound file selection
            sound_file_label = Tk.Label(sounds_frame.frame, text="File", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=row_counter+1, column=0)

            self.sound_file_path_vars[sound_number-1].set(self.model.get_file_path_for_sound(sound_number))
            sound_file_path_entry = Tk.Entry(sounds_frame.frame, textvariable=self.sound_file_path_vars[sound_number-1], state='readonly').grid(sticky=Tk.W+Tk.E, row=row_counter+1, column=1)
            sound_choose_file_button = Tk.Button(sounds_frame.frame, text="Open", command=lambda sound_number=sound_number: self.on_choose_sound_file(sound_number)).grid(sticky=Tk.W, row=row_counter+1, column=2, padx=5)

            # GPIO pin selection
            sound_pin_label = Tk.Label(sounds_frame.frame, text="Pin", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W, row=row_counter+2, column=0)
            self.sound_pin_name_vars[sound_number-1].set(self.model.get_pin_for_sound(sound_number))

            sound_number_copy=sound_number

            sound_pin_option_menu = Tk.OptionMenu(sounds_frame.frame, self.sound_pin_name_vars[sound_number-1], *model.get_unassigned_gpio_pin_names(), command=lambda pin_name=sound_number, sound_number=sound_number_copy: self.on_choose_sound_pin(pin_name, sound_number)).grid(sticky=Tk.W, row=row_counter+2, column=1)

            # volume slider 
            sound_volume_label = Tk.Label(sounds_frame.frame, text="Vol.", justify=Tk.LEFT, anchor="w").grid(sticky=Tk.W+Tk.S, row=row_counter+3, column=0)
            sound_volume_slider_var = Tk.IntVar()
            sound_volume_slider_var.set(100*self.model.get_volume_for_sound(sound_number))

            sound_volume_slider = Tk.Scale(sounds_frame.frame, variable=sound_volume_slider_var, command=lambda volume=sound_number, sound_number=sound_number_copy: self.on_volume_change(volume, sound_number), from_=0, to_=100, orient=Tk.HORIZONTAL).grid(sticky=Tk.W+Tk.E, row=row_counter+3, column=1)

            # play button
            sound_play_button = Tk.Button(sounds_frame.frame, text="Play", command=lambda sound_number=sound_number: self.on_play_sound(sound_number)).grid(sticky=Tk.W+Tk.E+Tk.S, row=row_counter+3, column=2, padx=5)

            # dont display last separator
            if sound_number != self.model.get_num_sounds():
                sound_separator = ttk.Separator(sounds_frame.frame, orient=Tk.HORIZONTAL).grid(sticky=Tk.W+Tk.E, row=row_counter+4, column=0, columnspan=3, pady=5)


            row_counter = row_counter + 5

        sounds_frame.frame.update()
        self.root.maxsize(600, sounds_frame.frame.winfo_height()+31)


    def notify(self):
        for sound_number in range(1, self.model.get_num_sounds()+1):
            self.sound_file_path_vars[sound_number-1].set(self.model.get_file_path_for_sound(sound_number))
            self.sound_pin_name_vars[sound_number-1].set(self.model.get_pin_for_sound(sound_number))

    def on_about(self):
        about_dialog = AboutDialog(self.root)

        # make window modal
        about_dialog.wait_visibility()
        about_dialog.focus_set()
        about_dialog.grab_set()
        about_dialog.transient(self.root)

    def on_choose_sound_file(self, sound_number):
        file_path = filedialog.askopenfilename(initialdir="~/Music", title="Select Sound File")

        if file_path != None:
            self.model.set_file_path_for_sound(sound_number, file_path)

    def on_choose_sound_pin(self, pin_name, sound_number):
        self.model.set_pin_for_sound(sound_number, pin_name)

    def on_volume_change(self, volume, sound_number):
        self.model.set_volume_for_sound(sound_number, float(volume)/100)

    def on_play_sound(self, sound_number):
        print("play sound ", sound_number)


