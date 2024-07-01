import tkinter as tk
from tkinter import ttk

import platform

import devmode.DevmodeGUI as gui


# Collections of common widgets and frames and sorts for the GUI


# Scrollable Frame class
class VerticalScrolledFrame(ttk.Frame):
    """A pure Tkinter scrollable frame that actually works!
    * Use the 'interior' attribute to place widgets inside the scrollable frame.
    * Construct and pack/place/grid normally.
    * This frame only allows vertical scrolling.
    """

    def __init__(self, parent, *args, **kw):
        ttk.Frame.__init__(self, parent, *args, **kw)

        # Create a canvas object and a vertical scrollbar for scrolling it.
        vscrollbar = ttk.Scrollbar(self, orient="vertical")
        vscrollbar.pack(fill="y", side="right", expand=False)
        self.canvas = tk.Canvas(
            self, bd=0, highlightthickness=0, yscrollcommand=vscrollbar.set
        )
        self.canvas.pack(side="left", fill="both", expand=True)
        vscrollbar.config(command=self.canvas.yview)

        # Reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = ttk.Frame(self.canvas)
        self.interior.bind("<Enter>", self.onEnter)
        self.interior.bind("<Leave>", self.onLeave)

        interior_id = self.canvas.create_window(0, 0, window=interior, anchor="nw")

        # Track changes to the canvas and frame width and sync them,
        # also updating the scrollbar.
        def _configure_interior(event):
            # Update the scrollbars to match the size of the inner frame.
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            self.canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != self.canvas.winfo_width():
                # Update the canvas's width to fit the inner frame.
                self.canvas.config(width=interior.winfo_reqwidth())

        interior.bind("<Configure>", _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != self.canvas.winfo_width():
                # Update the inner frame's width to fill the canvas.
                self.canvas.itemconfigure(interior_id, width=self.canvas.winfo_width())

        self.canvas.bind("<Configure>", _configure_canvas)

    def onMouseWheel(self, event):  # cross platform scroll wheel event
        if platform.system() == "Windows":
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif platform.system() == "Darwin":
            self.canvas.yview_scroll(int(-1 * event.delta), "units")
        else:
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")

    def onEnter(self, event):  # bind wheel events when the cursor enters the control
        if platform.system() == "Linux":
            self.canvas.bind_all("<Button-4>", self.onMouseWheel)
            self.canvas.bind_all("<Button-5>", self.onMouseWheel)
        else:
            self.canvas.bind_all("<MouseWheel>", self.onMouseWheel)

    def onLeave(self, event):  # unbind wheel events when the cursorl leaves the control
        if platform.system() == "Linux":
            self.canvas.unbind_all("<Button-4>")
            self.canvas.unbind_all("<Button-5>")
        else:
            self.canvas.unbind_all("<MouseWheel>")


# Frame with text and a entry for floats
class FloatEntry(ttk.Frame):
    # Needs devGUI, parent, label title, initial value
    def __init__(self, parent, title, value):
        # Make frame
        super().__init__(parent, padding=gui.DevmodeGUI.defaultPadding)

        # Make label
        makeEntryLabel(self, title)

        # Make entry
        self.entry = Lotfi(self)
        self.entry.set(value)
        self.entry.pack(fill="x", anchor="e")

    # To get value of entry
    def get(self):
        return self.entry.get()


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


# Makes all the labels for the entries
# Keeps the formatting in one place
# Really Entry should be a class and all the different formats of it inherit from it...
# But oops
def makeEntryLabel(entry: ttk.Frame, title):
    label = ttk.Label(entry, text=title)
    label.pack(side="left", anchor="w", padx=(0, gui.DevmodeGUI.defaultPadding[0]))


if __name__ == "__main__":
    pass
