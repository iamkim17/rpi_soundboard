# adapted from: https://stackoverflow.com/a/57745179/2096060

try:
    import Tkinter as Tk
    from Tkinter import ttk
except ModuleNotFoundError:
    import tkinter as Tk
    from tkinter import ttk

class FrameWithScrollBar(Tk.Frame):

    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.canvas = Tk.Canvas(self)
        self.frame = Tk.Frame(self.canvas)
        self.scrollbar = Tk.Scrollbar(self, orient='vertical',
                                command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=True)
        self.scrollbar.pack(side=Tk.RIGHT, fill=Tk.BOTH)
        self.frame.pack(fill=Tk.BOTH, expand=True)
        self._frame_id = self.canvas.create_window(
                                 self.canvas.winfo_width(), 0,
                                 anchor='nw',
                                 window=self.frame)
        self.frame.bind('<Configure>', self.onFrameConfigure)
        self.canvas.bind('<Configure>', self.onCanvasConfigure)

    def onFrameConfigure(self, event):       
        self.canvas.configure(scrollregion=self.frame.bbox('all'))

    def onCanvasConfigure(self, event):
        width = event.width
        self.canvas.itemconfigure(self._frame_id, width=self.canvas.winfo_width())

