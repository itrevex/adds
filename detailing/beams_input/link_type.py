from common.constants import Constants
from common.messages import Messages
from common.message_codes import MessageCodes

class LinkType:
    '''
    Defines A link
    This class will be used to calculate the links labels and return
    offset on the end depending on whether the links span length is 
    provided or not

    diameter: Strength and diameter of link
    bar_mark: Bar mark for link
    shape_code: Shape code for link BS 8666: 2005
    spacing: Link spacing
    offset: Offset from edge of support, default is 50
    length: 2.3 
    '''
    DIAMETER = 2
    BAR_MARK = 3
    SHAPE_CODE = 4
    SPACING = 5
    OFFSET = 6
    LENGTH = 7 
    LINK_NAME = 1

    def __init__(self, links):
        self.links_input = links
        self.name = self.getStringValue(LinkType.LINK_NAME)
        self.diameter = self.getStringValue(LinkType.DIAMETER)
        self.bar_mark = self.getStringValue(LinkType.BAR_MARK)
        self.shape_code =self.getStringValue(LinkType.SHAPE_CODE)
        
        self.spacing = self.getFloatValue(LinkType.SPACING)
        self.offset = self.getOffset()
        self.length = self.getFloatValue(LinkType.LENGTH)

        self.label = None #dimension label
        # self.showWarning()


    def getStringValue(self, key):
        return self.links_input[key]
    
    def getFloatValue(self, key):
        try:
            if self.links_input[key] == 'X':
                return None
            else:
                return float(self.links_input[key])
        except IndexError:
            return None

    def getSpacing(self, key):
        try:
            if self.links_input[key] == 'X':
                self.showErrorMsg("Spacing must be passed")
            else:
                return float(self.links_input[key])
        except IndexError:
            self.showErrorMsg("Spacing must be passed")

    def showErrorMsg(self, errorMsg=""):
        msg = MessageCodes.ERROR_IN_INPUT
        print(self.links_input)
        msg.setMsg(msg.msg%("Links", " ".join(self.links_input)+"\n%s"%errorMsg))
        Messages.showError(msg)

    def getLength(self):
        try:
            if self.links_input[LinkType.LENGTH] == 'X':
                return None
            else:
                return float(self.links_input[LinkType.LENGTH])
        except IndexError:
            return None

    def setLength(self, length):
        self.length = length

    def getOffset(self):
        try:
            if self.links_input[LinkType.OFFSET] == 'X':
                return Constants.LINKS_DEFAULT_OFFSET 
            else:
                return float(self.links_input[LinkType.OFFSET])
        except ValueError:
            return Constants.LINKS_DEFAULT_OFFSET 

    def setLabel(self, label):
        self.label = label

    def toString(self):
        return ("\nName = " + str(self.name)  +
        "\nDiameter = " + str(self.diameter) +
        "\nBar mark = " + str(self.bar_mark)  +
        "\nShape code = " + str(self.shape_code)  +
        "\nSpacing = " + str(self.spacing)  +
        "\nOffset = " + str(self.offset) +
        "\nLength = " + str(self.length) +
        "\nLabel = " + str(self.label))


        