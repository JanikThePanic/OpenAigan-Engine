import tkinter as tk
from tkinter import ttk


def load(tab: ttk.Frame, defaultPadding=(10, 10)):
    guiSettingsFrame = ttk.LabelFrame(tab, text="GUI Settings", padding=defaultPadding)
    guiSettingsFrame.pack(fill="x")

    label = ttk.Label(guiSettingsFrame, text="f3efe", padding=defaultPadding)
    label.pack()


if __name__ == "__main__":
    pass
