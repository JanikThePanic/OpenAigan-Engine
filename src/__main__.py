import os, json
from shutil import copyfile

import devmode.DevmodeGUI


# Project requires the folders assets, src, and user to be in the same dirctory
class OpenAiganEngine:
    # List of all supported bot types to be referenced
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
        print(
            "Updated theme on sim to "
            + str(
                json.load(open(self.userPath + "/SETTINGS.json"))["devmode_settings"][
                    "theme"
                ]
            )
        )
        pass

    #
    # >>>> Comment for janik later <<<<
    # When given the chance make it so the program on launch checks the user dir exists and if not, make it.
    # Then check all the SETTINGS, CONTROLS, possible bot params jsons exist, if not make them.
    # so like run through supportedBotTypes and make sure for each bot type
    # CONTROLS_{supportedBotTypes} and BUILD_{supportedBotTypes} exist.
    # https://stackoverflow.com/questions/8933237/how-do-i-check-if-a-directory-exists-in-python
    # https://stackoverflow.com/questions/1274405/how-to-create-new-folder
    #

    # first check user dir exists
    # check if settings.json exists
    # all indv stuff per bot
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

        #
        # still to do: check every robot controls + build file
        #
        #

        for bot in OpenAiganEngine.supportedBotTypes:
            try:
                pass
            except:
                pass


if __name__ == "__main__":
    OpenAiganEngine()
