import tkinter as tk
from tkinter import ttk


# Return loaded settings tab frame
def load(devGUI, engine):
    tab = ttk.Frame(devGUI.notebook, padding=devGUI.tabPadding)

    # guiSettingsFrame = ttk.LabelFrame(
    #     tab, text="GUI Settings", padding=devGUI.defaultPadding
    # )
    # guiSettingsFrame.pack(fill="x")

    # label = ttk.Label(guiSettingsFrame, text="f3efe", padding=devGUI.defaultPadding)
    # label.pack()

    # button = ttk.Button(
    #     guiSettingsFrame, text="Click me!", command=lambda: devGUI.reloadTabs()
    # )
    # button.pack()

    return tab


if __name__ == "__main__":
    pass
