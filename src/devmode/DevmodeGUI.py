import tkinter as tk
from tkinter import ttk
import os
import sv_ttk

from devmode.tabs import SettingsTab
from devmode.tabs import ControlTab


class DevmodeGUI:
    # Devmode GUI initialization
    # The DevmodeGUI class requires the folders assets, src, and user to be in the same dirctory
    # metadata is a passed loaded json
    # srcPath is a os path to the src directory
    def __init__(self, metaData, srcPath):
        # Save metaData and path to src folder
        self.metaData = metaData
        self.srcPath = srcPath

        # Create root Tk window
        self.root = tk.Tk()

        # Set theme
        sv_ttk.set_theme("dark")
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

        # Set window icon
        self.root.iconbitmap(
            os.path.join(self.srcPath, "../assets/", self.metaData["icon"])
        )
        # Set window title
        self.root.title(self.metaData["project-name"])

        # Fill left half the screen
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()
        self.root.geometry(
            str(int(screenWidth / 2)) + "x" + str(screenHeight - 75) + "+0+0"
        )

        # Notebook fill window for tabs
        notebook = ttk.Notebook(self.root, padding=10)
        notebook.pack(expand=True, fill="both")

        # Constant bar on bottom of screen
        constantBar = ttk.Frame(self.root, padding=10)
        constantBar.pack(fill="x", side="bottom", anchor="s")
        # Display program version
        versionLabel = ttk.Label(constantBar, text=str(metaData["version"]))
        versionLabel.pack(side="left", anchor="w")
        # Simulation only toggle
        simulationOnlyToggle = ttk.Checkbutton(
            constantBar, style="Switch.TCheckbutton", text="Simulation Only"
        )
        simulationOnlyToggle.pack(side="right", anchor="e")

        # Load tabs into notebook
        self.loadTabs(notebook)

        # Run window
        self.root.mainloop()

    # Function will load necessary tabs to passed ttk notebook
    def loadTabs(self, notebook: ttk.Notebook):
        # Reused paddings
        tabPadding = (15, 10)
        defaultPadding = (20, 10)

        # Load constant tabs
        settingsTab = ttk.Frame(notebook, padding=tabPadding)
        controlTab = ttk.Frame(notebook, padding=tabPadding)
        # Load bot dependant tabs
        robotTab = ttk.Frame(notebook, padding=tabPadding)

        # Populate tabs
        SettingsTab.load(settingsTab, defaultPadding)
        ControlTab.load(controlTab, defaultPadding)

        # Add tab frames to notebook
        notebook.add(settingsTab, text="⚙ Settings")
        notebook.add(controlTab, text="🎮 Control")

        notebook.add(robotTab, text="{bot type}")


if __name__ == "__main__":
    DevmodeGUI()
