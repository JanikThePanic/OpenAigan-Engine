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
    buildPath = engine.userPath + f"/build/{selectedBot}_build.json"
    buildJson = json.load(open(buildPath))

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
    saveButton = ttk.Button(
        metaFrame,
        text="Save",
        command=lambda: saveBuild(buildPath=buildPath, botParams=botParams),
    )
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
            FloatEntry(botParams, param["title"], param["value"]).pack(
                fill="x", pady=devGUI.tabPadding[1]
            )

    return tab


# Save all parameters to the json
def saveBuild(buildPath, botParams: ttk.LabelFrame):
    # buildJson is a path to the build JSON
    # botParams refers to the build_parameters displayed in the labelFrame in the JSON
    # When I get my act tgt, this tab will be a class extenting a tab calss

    buildJson = json.load(open(buildPath))

    # Save all build params
    indexer = 0
    buildParamNames = list(buildJson["build_parameters"].keys())
    for i in botParams.winfo_children():
        # Make sure save values as right type
        valueType = buildJson["build_parameters"][buildParamNames[indexer]]["type"]
        if valueType == "float":
            value = float(i.get())
        # elif
        ##### other value types
        else:
            value = i.get()

        buildJson["build_parameters"][buildParamNames[indexer]]["value"] = value
        indexer += 1

    with open(buildPath, "w") as f:
        json.dump(buildJson, f, indent=4)

    # Not my proudest code here...


if __name__ == "__main__":
    pass
