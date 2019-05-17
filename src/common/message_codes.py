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
    INFO_DXF_GENERATED = "Generated \"%s\" file"
    INFO_CONTINUE_PROMPT = "Press any key to continue . . ."
    INFO_CREATING_ENTITY = "Generating BEAM-%s SPAN-%s entities . . ."

    #Error Constants
    #ER0001
    msg = "The file you are trying to run is from a later version of Trevexs Adds "
    msg += "\nPlease install the latest version to be able to run this file"
    ERROR_LATER_VERSION = MessageCode(msg, "ER0001")

    #ER0002
    msg = "Please check file path and try again"
    ERROR_WRONG_FILE_PATH = MessageCode(msg, "ER0002")

    #ER0003
    msg = "There is no data to use to generate output file"
    ERROR_NO_INPUT_DATA = MessageCode(msg, "ER0003")

    #ER0004
    msg = "File \"%s\" has an error on line %s"
    msg += "\n\nMake sure there are no trailing or missing commas after input and"
    msg += "all text is in quotes."
    msg += "\nCross check with sample input and make sure inputs are of a similar format."
    ERROR_INPUT_DATA_FORMAT = MessageCode(msg, "ER0004")

    #ER0005
    msg = "Please check and make sure you specified beam sections"
    ERROR_NO_BEAM_SECTIONS = MessageCode(msg, "ER0005")

    #ER0006
    msg = "Please check number of supports provided for %s %s"
    msg += "\n\nThe number of supports should = spans + 1. Make sure the "
    msg += "\nnumber of supports are 1 greater than the number of spans"
    ERROR_WRONG_NO_SUPPORTS= MessageCode(msg, "ER0006")

    #ER0007
    msg = "Dxf your are trying to create is being used by another program"
    msg += "\nPlease close the open dxf file or rename your input file to something else"
    ERROR_OPEN_DXF= MessageCode(msg, "ER0007")

    #ER0008
    msg="There is an error in your input"
    msg+="\nPlease %s line: \n%s"
    ERROR_IN_INPUT= MessageCode(msg, "ER0008")

    #ER0009
    msg="The \"Name\" parameter value should be unique and cannot be used morethan once"
    msg+="\nPlease check %s under %s"
    ERROR_UNIQUE_PARAM_NAME= MessageCode(msg, "ER0009")

    #ER0010
    msg = "Section-%s specified for span-%s beam-%s is not listed under sections \n"
    msg += "Please make you have specified section with 'Name' \"%s\" under sections"
    ERROR_SPAN_SECTION_NOT_SPECIFIED= MessageCode(msg, "ER0010")

    #ER0011
    msg = "Link-%s specified for span-%s beam-%s is not listed under links \n"
    msg += "Please make you have specified link with 'Name' \"%s\" under links"
    ERROR_SPAN_LINKS_NOT_SPECIFIED= MessageCode(msg, "ER0011")

    #ER0011
    msg = "Support_type-%s specified for support %s beam-%s is not listed under supports \n"
    msg += "Please make you have specified support_type with 'Name' \"%s\" under supports types"
    ERROR_SUPPORT_NOT_SPECIFIED= MessageCode(msg, "ER0011")

    #Warning Constants
    #WAR0001
    msg = "The file you are trying to run is not updated to fully work with the current version"
    msg += "\nApplication is running in compatible mode"
    msg += "\n\nPlease consider updating your file to the latest version"
    WARNING_EARLIER_VERSION = MessageCode(msg, "WAR0001")

    #WAR0002
    msg = "%s %s links were not provided"
    WARNING_NO_LINKS = MessageCode(msg, "WAR0002")

    #WAR0003
    msg = "%s deeper than beam"
    WARNING_DEEPER_SECTION = MessageCode(msg, "WAR0003")

    #WAR0004
    msg = "Beam depth has been adjusted to meet the deepest section requirements."
    msg += "\nIf this was the intended behaviour, please contact developer"
    WARNING_BEAM_DEPTH_ALTERED = MessageCode(msg, "WAR0004")

