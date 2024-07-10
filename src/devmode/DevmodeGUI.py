# GUI dependencies
import tkinter as tk
from tkinter import ttk
import sv_ttk

# Misc dependencies
import json
import platform
import ctypes

# Tab-specfic imports
import devmode.tabs.BotTab
import devmode.tabs.ControlTab
import devmode.tabs.SettingsTab


# The DevmodeGUI gets passed a referance to the main engine class
# Which kinda makes a loop of pointers...
class DevmodeGUI:
    # Reused paddings
    tabPadding = (20, 10)
    defaultPadding = (20, 10)

    def __init__(self, engine):
        # Save the engine the gui is running in
        self.engine = engine

        # Create root Tk window
        self.root = tk.Tk()

        # Set window icon
        self.root.iconbitmap(
            self.engine.assetsPath + "/" + self.engine.metadata["icon"]
        )
        # Set window title
        self.root.title(self.engine.metadata["project-name"])

        # Fill left 1/3 of the screen
        scaleFactor = 1
        if int(platform.release()) >= 8:
            ctypes.windll.shcore.SetProcessDpiAwareness(True)
            scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100

        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        self.root.geometry(
            str(int(screenWidth / 3 * scaleFactor))
            + "x"
            + str(int((screenHeight - 75) * scaleFactor))
            + "+0+0"
        )

        # Set theme
        self.updateToTheme()

        # Notebook fill window for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")
        # Let crtl+tab and crtl+shift+tab traverse tabs
        self.notebook.enable_traversal()

        # Constant bar on bottom of screen
        constantBar = ttk.Frame(self.root, padding=10)
        constantBar.pack(fill="x", side="bottom", anchor="s")
        # Display program version
        versionLabel = ttk.Label(constantBar, text=str(self.engine.metadata["version"]))
        versionLabel.pack(side="left", anchor="w")
        # Simulation only toggle
        simulationOnlyToggle = ttk.Checkbutton(
            constantBar, style="Switch.TCheckbutton", text="Simulation Only"
        )
        simulationOnlyToggle.pack(side="right", anchor="e")

        # (re)Load all tabs into notebook
        self.reloadTabs()

    # Function to update GUI
    def update(self):
        self.root.update()

    # Function to clear notebook of all tabs and reload new tabs
    def reloadTabs(self):
        # Note which tab selected at the moment
        # Has to start at index 0 and in try since on load there are no tabs
        selected = 0
        try:
            selected = self.notebook.index(self.notebook.select())
        except:
            pass

        # Clear all tabs
        for windowName in self.notebook.tabs():
            self.notebook.forget(windowName)

        # Now load tabs

        # Constant pages
        self.notebook.add(
            devmode.tabs.SettingsTab.load(self, self.engine), text="⚙ Settings"
        )
        self.notebook.add(
            devmode.tabs.ControlTab.load(self, self.engine), text="🎮 Control"
        )
        # Add bot tab
        self.notebook.add(
            devmode.tabs.BotTab.load(self, self.engine),
            text=str(
                "🔧 "
                + str(
                    json.load(open(self.engine.userPath + "/SETTINGS.json"))[
                        "root_settings"
                    ]["selected_robot"]
                )
            ),
        )

        # Go back to which tab was selected before reloading
        self.notebook.select(self.notebook.tabs()[selected])

    # Sets GUI theme to sv_ttk theme listed in SETTINGS.json
    # As well hides the notebook tab focus border
    # For whatever reason, the focus snipped has to run every time the theme changes
    def updateToTheme(self):
        # Set theme
        sv_ttk.set_theme(
            json.load(open(self.engine.userPath + "/SETTINGS.json"))[
                "devmode_settings"
            ]["theme"]
        )
        self.root.option_add("*font", "-size 12")

        # Following is from https://www.tutorialspoint.com/how-to-remove-ttk-notebook-tab-dashed-line-tkinter
        # Remove's tab's dashed focus indicator
        # Create an instance of ttk
        notebookStyle = ttk.Style()
        # Define Style for Notebook widget
        # fmt: off
        notebookStyle.layout( "Tab", [ ( "Notebook.tab",
        { "sticky": "nswe", "children": [ ( "Notebook.padding",
        { "side": "top", "sticky": "nswe", "children":
        [ ( "Notebook.label", {"side": "top", "sticky": ""},
        ) ], }, ) ], }, ) ], )
        # fmt: on
        # Use the Defined Style to remove the dashed line from Tabs
        notebookStyle.configure("Tab")


if __name__ == "__main__":
    pass
