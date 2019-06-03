from common.messages import Messages
from common.message_codes import MessageCodes
from common.constants import Constants

class Span:
    '''
    defines span with the span centre to centre length as span_length
    in m
    The section on the left of the span and the section on the right of the span
    '''

        #SPANS
    SPAN_LENGTH = 2
    SPAN_SECTION_LEFT = 3
    SPAN_SECTION_RIGHT = 3
    SPAN_SECTION = 3
    SPAN_LINKS = 4

    def __init__(self, name, props, beam_name, index = 0):
        self.name = name
        self.props = props
        self.beam_name = beam_name
        self.span_length = float(props[Span.SPAN_LENGTH])
        self.section_left = self.getSectionLeft()
        self.section_right = self.getSectionLeft()
        self.links = self.getLinks()
        self.index = index

    def getSectionLeft(self):
        section = ""
        try:
           section = self.props[Span.SPAN_SECTION_LEFT]
        except ValueError:
            #show error message to user
            self.showErrorMsg("No column for span")
            pass


        return section
    def showErrorMsg(self, errorMsg=""):
        msg = MessageCodes.ERROR_IN_INPUT
        msg.setMsg(msg.msg%("Spans", " ".join(self.props)+"\n%s"%errorMsg))
        Messages.showError(msg)

    def getSpanLinks(self, props, build):
        links = []
        if (build < Constants.CURRENT_BUILD):
            return links
        try:
            links = props[Span.SPAN_LINKS]
        except KeyError:
            warning = MessageCodes.WARNING_NO_LINKS
            warning.setMsg(warning.msg%(self.beam_name, self.name))
            Messages.showWarning(warning)

        return links

    def getLinks(self):
        links = self.props[ Span.SPAN_LINKS: ]
        return links

    def getSectionRight(self, props):
        section = ""
        try:
           section = props[Span.SPAN_SECTION_RIGHT]
        except KeyError:
            try:
                section = props[Span.SPAN_SECTION_LEFT]
            except:
                try:
                    section = props[Span.SPAN_SECTION]
                except:
                    Messages.showError(MessageCodes.ERROR_NO_BEAM_SECTIONS)


        return section

    def setSpanLength(self, span_length):
        self.span_length = float(span_length)

    def setSectionLeft(self, section_left):
        self.section_left = section_left

    def setSectionRight(self, section_right):
        self.section_right = section_right

    def setColumnRight(self, column):
        self.column_right = column

    def setColumnLeft(self, column):
        self.column_left = column

    def setName(self, name):
        self.name = name

    def toString(self):
        string = ""
        string += "\nName = " + str(self.name)
        string += "\nbeam_name = " + str(self.beam_name)
        string += "\nspan_length = " + str(self.span_length) 
        string += "\nsection_left = " + str(self.section_left)
        string += "\nsection_right = " + str(self.section_right)
        string += "\nlinks = " + str(self.links)
        string += "\nindex = " + str(self.index)
        return string