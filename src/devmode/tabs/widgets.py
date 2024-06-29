import tkinter as tk
from tkinter import ttk

import devmode.DevmodeGUI as gui


# Collections of common widgets and frames and sorts for the GUI


# Frame with text and a entry for floats
class FloatEntry(ttk.Frame):
    # Needs devGUI, parent, label title, initial value
    def __init__(self, parent, title, value):
        # Make frame
        super().__init__(parent, padding=gui.DevmodeGUI.defaultPadding)

        # Make label
        self.label = ttk.Label(self, text=title, padding=gui.DevmodeGUI.defaultPadding)
        self.label.pack(side="left", anchor="w")

        # Make entry
        self.entry = Lotfi(self)
        self.entry.set(value)
        self.entry.pack(fill="x", anchor="e")


# Some amazing code I stole from stackoverflow
# Minor edit, added to allow float
class Lotfi(ttk.Entry):
    def __init__(self, master=None, **kwargs):
        self.var = tk.StringVar()
        ttk.Entry.__init__(self, master, textvariable=self.var, **kwargs)
        self.old_value = ""
        self.var.trace("w", self.check)
        self.get, self.set = self.var.get, self.var.set

    def check(self, *args):
        if self.get().replace(".", "", 1).isdigit():
            # the current value is only digits; allow this
            self.old_value = self.get()
        else:
            # there's non-digit characters in the input; reject this
            self.set(self.old_value)


if __name__ == "__main__":
    pass
