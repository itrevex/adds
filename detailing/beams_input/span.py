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
    SPAN_LENGTH = "length_m"
    SPAN_SECTION_LEFT = "section_left"
    SPAN_SECTION_RIGHT = "section_right"
    SPAN_SECTION = "section"
    SPAN_LINKS = "links"

    def __init__(self, name, props, beam_name, build, index = 0):
        self.name = name
        self.beam_name = beam_name
        self.span_length = float(props[Span.SPAN_LENGTH])
        self.section_left = self.getSectionLeft(props)
        self.section_right = self.getSectionRight(props)
        self.links = self.getSpanLinks(props, build)
        self.index = index
    
    def getSectionLeft(self, props):
        section = ""
        try:
           section = props[Span.SPAN_SECTION_LEFT]
        except KeyError:
            try:
                section = props[Span.SPAN_SECTION_RIGHT]
            except KeyError:
                try:
                    section = props[Span.SPAN_SECTION]
                except KeyError:
                    Messages.showError(MessageCodes.ERROR_NO_BEAM_SECTIONS)


        return section

    def getSpanLinks(self, props, build):
        links = []
        if (build < Constants.CURRENT_BUILD):
            return links
        try:
            links = props[Span.SPAN_LINKS]
        except KeyError:
            Messages.showWarning("%s %s links were not provided"%(self.beam_name, self.name))

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
        pass