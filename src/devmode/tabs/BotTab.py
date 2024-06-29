import tkinter as tk
from tkinter import ttk
import json

from devmode.tabs.widgets import *


# Return loaded settings tab frame
def load(devGUI, engine):
    tab = VerticalScrolledFrame(devGUI.notebook)
    tab.interior.configure(padding=devGUI.defaultPadding)

    # Currently selected bot
    selectedBot = json.load(open(engine.userPath + "/SETTINGS.json"))["root_settings"][
        "selected_robot"
    ]
    # Path to the build json
    buildJson = json.load(open(engine.userPath + f"/build/{selectedBot}_build.json"))

    # Load meta data
    meta = buildJson["meta"]
    # Load build parameters
    params = buildJson["build_parameters"]

    # Information up top
    metaFrame = ttk.Frame(tab.interior, padding=devGUI.defaultPadding)
    metaFrame.pack(fill="x", pady=devGUI.tabPadding[1])

    # Note about profile
    note = ttk.Label(metaFrame, text=meta["note"], padding=devGUI.defaultPadding)
    note.pack(side="left", anchor="w")

    # temp save button to test things
    saveButton = ttk.Button(metaFrame, text="Save", command=lambda: devGUI.reloadTabs())
    saveButton.pack(side="right", anchor="e")

    # Robot parameters section
    botParams = ttk.LabelFrame(
        tab.interior,
        text=meta["profile_name"] + " Parameters",
        padding=devGUI.defaultPadding,
    )
    botParams.pack(fill="x", pady=devGUI.tabPadding[1])

    # Robot parameters
    for param in params.items():
        param = param[1]
        # If param a...

        # Float entry
        if param["type"] == "float":
            paramFrame = FloatEntry(botParams, param["title"], param["value"])
            paramFrame.pack(fill="x", pady=devGUI.tabPadding[1])

    return tab


if __name__ == "__main__":
    pass
