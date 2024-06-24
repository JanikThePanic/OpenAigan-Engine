import json
import os
from devmode import DevmodeGUI


def main():
	# Get the programs's src directory path
	srcDirectory = os.path.dirname(__file__)

	# Load program meta data
	metaDatafile = open(os.path.join(srcDirectory, "../assets/", "meta.json"))
	metaData = json.load(metaDatafile)
	metaDatafile.close()

	# temp for gui dev
	# pass metadata as optional
	myDev = DevmodeGUI.DevmodeGUI(metadata=metaData, srcPath=srcDirectory)


if __name__ == "__main__":
	main()
