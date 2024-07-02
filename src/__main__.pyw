import os, json
from shutil import copyfile

import devmode.DevmodeGUI


# Project requires the folders assets, src, and user to be in the same dirctory
class OpenAiganEngine:
    # List of all supported bot types to be referenced
    # Should prob be moved to meta.json
    supportedBotTypes = ["Hexapod", "gabeNewell"]

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

        # Make sure all user dir and files exist
        self.preCheckAllUserFiles()

        # Pull all current engine-level data
        self.theme = json.load(open(self.userPath + "/SETTINGS.json"))[
            "devmode_settings"
        ]["theme"]
        self.bot = json.load(open(self.userPath + "/SETTINGS.json"))["root_settings"][
            "selected_robot"
        ]

        #
        #
        # start threads here
        #
        #

        # temp: just load gui no questions
        # working on gui first
        # fun fact: tkinter cant run in thread, so everything else has to be in thread instead
        self.devGUI = devmode.DevmodeGUI.DevmodeGUI(self)

    # Comment <<<<<<<<<<<<<<<<<<<<<<<<
    def updateToTheme(self):
        self.theme = json.load(open(self.userPath + "/SETTINGS.json"))[
            "devmode_settings"
        ]["theme"]
        print("Updated theme on sim to " + self.theme)

        # updateSim()

    # Comment <<<<<<<<<
    def updateToRobot(self):
        self.bot = json.load(open(self.userPath + "/SETTINGS.json"))["root_settings"][
            "selected_robot"
        ]
        print("Updated to: " + self.bot)

        # updateSim()

    # Checks to make sure all user/setting files and dirs exist
    # First check user and /build and /controls dirs exist
    # Check if settings.json exists
    # All indv stuff per bot
    def preCheckAllUserFiles(self):
        # Default path
        defaultPath = self.assetsPath + "/defaults"

        # Check if user dir exists
        if not os.path.isdir(self.userPath):
            # Make one if not
            os.makedirs(self.userPath)

        # Check if user/build dir exists
        if not os.path.isdir(self.userPath + "/build"):
            # Make one if not
            os.makedirs(self.userPath + "/build")

        # Check if user/build dir exists
        if not os.path.isdir(self.userPath + "/controls"):
            # Make one if not
            os.makedirs(self.userPath + "/controls")

        # Check SETTINGS.json exists
        if not os.path.exists(self.userPath + "/SETTINGS.json"):
            # Copy one over from defaults if not
            copyfile(defaultPath + "/SETTINGS.json", self.userPath + "/SETTINGS.json")

        # Check for every robot controls + build file
        for bot in OpenAiganEngine.supportedBotTypes:
            # Check {bot}_controls.json exists
            checking = f"/controls/{bot}_controls.json"
            if not os.path.exists(self.userPath + checking):
                # Copy one over from defaults if not
                copyfile(defaultPath + checking, self.userPath + checking)
        for bot in OpenAiganEngine.supportedBotTypes:
            # Check {bot}_build.json exists
            checking = f"/build/{bot}_build.json"
            if not os.path.exists(self.userPath + checking):
                # Copy one over from defaults if not
                copyfile(defaultPath + checking, self.userPath + checking)


if __name__ == "__main__":
    OpenAiganEngine()
