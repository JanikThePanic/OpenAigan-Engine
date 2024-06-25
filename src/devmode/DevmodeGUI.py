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
	def __init__(self, metadata, srcPath):
		# Save metadata and path to src folder
		self.metadata = metadata
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
		notebookStyle.layout("Tab", [('Notebook.tab', {'sticky': 'nswe', 'children':
		[('Notebook.padding', {'side': 'top', 'sticky': 'nswe', 'children':
			[('Notebook.label', {'side': 'top', 'sticky': ''})],
		})],
		})]
		)
		# Use the Defined Style to remove the dashed line from Tabs
		notebookStyle.configure("Tab")

		# Set window icon
		self.root.iconbitmap(os.path.join(self.srcPath, "../assets/", self.metadata["icon"]))
		# Set window title
		self.root.title(self.metadata["project-name"])

		# Fill left half the screen
		screenWidth = self.root.winfo_screenwidth()
		screenHeight = self.root.winfo_screenheight()
		self.root.geometry(str(int(screenWidth / 2)) + "x" + str(screenHeight - 75) + "+0+0")

		# Notebook fill window for tabs
		notebook = ttk.Notebook(self.root, padding=10)
		notebook.pack(expand=True, fill="both")

		# Constant bar on bottom of screen
		constantBar = ttk.Frame(self.root, padding=10)
		constantBar.pack(fill="x", side="bottom", anchor="s")
		# Display program version
		versionLabel = ttk.Label(constantBar, text="v" + str(metadata["version"]))
		versionLabel.pack(side="left", anchor="w")
		# Simulation only toggle
		simulationOnlyToggle = ttk.Checkbutton(constantBar, style="Switch.TCheckbutton", text="Simulation Only")
		simulationOnlyToggle.pack(side="right", anchor="e")

		# Load tabs into notebook
		self.loadTabs(notebook)

		# Run window
		self.root.mainloop()

	# Function will load necessary tabs to passed ttk notebook
	def loadTabs(self, notebook: ttk.Notebook):
		# Load constant tabs
		settingsTab = ttk.Frame(notebook)
		controlTab = ttk.Frame(notebook)
		# Load bot dependant tabs
		robotTab = ttk.Frame(notebook)

		# Populate tabs
		SettingsTab.load(settingsTab)
		ControlTab.load(controlTab)

		# Add tab frames to notebook
		notebook.add(settingsTab, text="⚙ Settings")
		notebook.add(controlTab, text="🎮 Control")

		notebook.add(robotTab, text="{bot type}")


if __name__ == "__main__":
	DevmodeGUI()
