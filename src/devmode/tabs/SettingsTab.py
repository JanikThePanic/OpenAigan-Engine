import tkinter as tk
from tkinter import ttk
import json


# Return loaded settings tab frame
def load(devGUI, engine):
    tab = ttk.Frame(devGUI.notebook, padding=devGUI.tabPadding)

    #
    # Group GUI settings
    #
    guiSettingsFrame = ttk.LabelFrame(
        tab, text="GUI Settings", padding=devGUI.defaultPadding
    )
    guiSettingsFrame.pack(fill="x", pady=devGUI.tabPadding[1])

    # Theme setting
    themeSettingFrame = ttk.Frame(guiSettingsFrame, padding=devGUI.defaultPadding)
    themeSettingFrame.pack(fill="x")
    themeSettingLabel = ttk.Label(themeSettingFrame, text="Theme")
    themeSettingLabel.pack(side="left", anchor="w", padx=(0, devGUI.defaultPadding[0]))
    themeSettingList = ttk.Combobox(
        themeSettingFrame, state="readonly", values=["dark", "light"]
    )
    themeSettingList.set(
        json.load(open(engine.userPath + "/SETTINGS.json"))["devmode_settings"]["theme"]
    )
    themeSettingList.bind(
        "<<ComboboxSelected>>",
        lambda event, list=themeSettingList, main=engine, gui=devGUI: handleThemeEverywhere(
            list, main, gui
        ),
    )
    themeSettingList.pack(fill="x", anchor="e")

    #
    # Group other Devmode settings
    #
    devSettingsFrame = ttk.LabelFrame(
        tab, text="Devmode Settings", padding=devGUI.defaultPadding
    )
    devSettingsFrame.pack(fill="x", pady=devGUI.tabPadding[1])

    # Change bot setting
    selectBotFrame = ttk.Frame(devSettingsFrame, padding=devGUI.defaultPadding)
    selectBotFrame.pack(fill="x")
    selectBotLabel = ttk.Label(selectBotFrame, text="Robot Type")
    selectBotLabel.pack(side="left", anchor="w", padx=(0, devGUI.defaultPadding[0]))
    selectBotList = ttk.Combobox(
        selectBotFrame, state="readonly", values=engine.supportedBotTypes
    )
    selectBotList.set(
        json.load(open(engine.userPath + "/SETTINGS.json"))["root_settings"][
            "selected_robot"
        ]
    )
    selectBotList.bind(
        "<<ComboboxSelected>>",
        lambda event, list=selectBotList, main=engine, gui=devGUI: handleBotChange(
            list, main, gui
        ),
    )
    selectBotList.pack(fill="x", anchor="e")

    # Return settings frame tab
    return tab


# Handles theme change and calls it to change everywhere
# God this is such spaghetti code at this point
def handleThemeEverywhere(list: ttk.Combobox, main, gui):
    # Needed otherwise stays highlighted
    current = list.get()
    list.set("")
    list.set(current)

    # Change theme in json
    settings = json.load(open(main.userPath + "/SETTINGS.json"))
    settings["devmode_settings"]["theme"] = current
    with open(main.userPath + "/SETTINGS.json", "w") as f:
        json.dump(settings, f, indent=4)

    # Calls theme update in main for sim
    main.updateToTheme()

    # Update GUI theme
    gui.updateToTheme()


# Handles bot change and calls it to change everywhere
# God this is such spaghetti code at this point AGAIN
def handleBotChange(list: ttk.Combobox, main, gui):
    # Needed otherwise stays highlighted
    current = list.get()
    list.set("")
    list.set(current)

    # Change bot in json
    settings = json.load(open(main.userPath + "/SETTINGS.json"))
    settings["root_settings"]["selected_robot"] = current
    with open(main.userPath + "/SETTINGS.json", "w") as f:
        json.dump(settings, f, indent=4)

    # Calls bot update in main for sim
    # main.bot update something()

    # Update tabs
    gui.reloadTabs()


if __name__ == "__main__":
    pass
