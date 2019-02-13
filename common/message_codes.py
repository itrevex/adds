class MessageCode:
    def __init__(self, msg, code=""):
        self.msg = msg
        self.code = code

    def setMsg(self, msg):
        self.msg = msg

    def appendMsg(self, msg):
        self.msg = self.msg%msg

class MessageCodes:

    #Info constants
    INFO_DATA_READ = "Collecting %s info . . ."

    #Error Constants
    #EROOO1
    msg = "The file you are trying to run is from a later version of Trevexs Adds "
    msg += "\nPlease install the latest version to be able to run this file"
    ERROR_LATER_VERSION = MessageCode(msg, "EROOO1")

    #EROOO2
    msg = "Please check file path and try again"
    ERROR_WRONG_FILE_PATH = MessageCode(msg, "EROOO2")

    #EROOO3
    msg = "There is no data to use to generate output file"
    ERROR_NO_INPUT_DATA = MessageCode(msg, "EROOO3")

    #EROOO4
    msg = "File \"%s\" has an error on line %s"
    msg += "\n\nMake sure there are no trailing or missing commas after input and"
    msg += "all text is in quotes."
    msg += "\nCross check with sample input and make sure inputs are of a similar format."
    ERROR_INPUT_DATA_FORMAT = MessageCode(msg, "EROOO4")

    #EROOO5
    msg = "Please check and make sure you specified beam sections"
    ERROR_NO_BEAM_SECTIONS = MessageCode(msg, "EROOO5")

    #EROOO6
    msg = "Please check number of supports provided for %s %s"
    msg += "\n\nThe number of supports should = spans + 1. Make sure the "
    msg += "\nnumber of supports are 1 greater than the number of spans"
    ERROR_WRONG_NO_SUPPORTS= MessageCode(msg, "EROOO6")

    #EROOO7
    msg = "Dxf your are trying to create is being used by another program"
    msg += "\nPlease close the open dxf file or rename your input file to something else"
    ERROR_OPEN_DXF= MessageCode(msg, "EROOO7")

    #Warning Constants
    #WAROOO1
    msg = "The file you are trying to run is not updated to fully work with the current version"
    msg += "\nApplication is running in compatible mode"
    msg += "\n\nPlease consider updating your file to the latest version"
    WARNING_EARLIER_VERSION = MessageCode(msg, "WAROOO1")

    def __init__(self):
        pass
