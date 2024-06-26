import os, json

import devmode.DevmodeGUI


# Project requires the folders assets, src, and user to be in the same dirctory
class OpenAiganEngine:
    def __init__(self):
        # Save the programs's src directory path
        self.srcPath = os.path.dirname(__file__)
        # Save the programs's assets directory path
        self.assetsPath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../assets")
        )
        # Save the programs's user directory path
        self.userPath = os.path.abspath(
            os.path.join(os.path.dirname(__file__), "../user")
        )
        # Meta data about the program shouldn't be changing during runtime
        # Hence can load now
        self.metadata = json.load(open(self.assetsPath + "/meta.json"))

        # start threads here
        #
        #

        # temp: just load gui no questions
        # working on gui first
        # fun fact: tkinter cant run in thread, so everything else has to be in thread instead
        self.devGUI = devmode.DevmodeGUI.DevmodeGUI(self)

    # Comment <<<<<<<<<<<<<<<<<<<<<<<<
    def changeTheme(self, theme):
        print("Updated theme on json to " + theme)
        self.updateToTheme()

    # Comment <<<<<<<<<<<<<<<<<<<<<<<<
    def updateToTheme(self):
        print("Updated theme on sim")
        pass


if __name__ == "__main__":
    OpenAiganEngine()
