import tkinter as tk
from tkinter import ttk
import os
import sv_ttk


class DevmodeGUI:
	# Devmode GUI initialization
	def __init__(self, metadata, srcPath):
		# Create root Tk window
		self.root = tk.Tk()

		# Set theme
		sv_ttk.set_theme("dark")

		# Set window icon
		self.root.iconbitmap(os.path.join(srcPath, "../assets/", metadata["icon"]))
		# Set window title
		self.root.title(metadata["project-name"])

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
		versionLabel = ttk.Label(constantBar, text="v" + str(metadata["version"]))
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
		# Load constant tabs
		settingsTab = ttk.Frame(notebook)
		controlTab = ttk.Frame(notebook)
		# Load bot dependant tabs
		robotTab = ttk.Frame(notebook)

		# You can create more frames (tab3, tab4, etc.) as needed
		notebook.add(settingsTab, text="⚙ Settings")
		notebook.add(controlTab, text="🎮 Control")

		notebook.add(robotTab, text="{bot type}")


if __name__ == "__main__":
	DevmodeGUI()
