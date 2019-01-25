
from .support_line import SupportLine
from .support_properties import SupportProps
from common.constants import Constants

class SupportLines:
    def __init__(self, support):
        self.support_lines = []
        self.support = support

        self.suppport_props = SupportProps(support.beam_depth,
            Constants.LAYER_SUPPORT_LINES, Constants.COLUMN_LINE_FACTOR)

        self.getSupportLines()
        
    def getSupportLines(self):
        if (self.support.support_location == Constants.SUPPORT_START):
            self.startSupport()
        elif (self.support.support_location == Constants.SUPPORT_END):
            self.endSupport()
        else:
            self.midSupport()

    def startSupport(self):
        # 3 support lines needed
        pt1 = list(self.support.starting_point)
        #draw full line at start
        self.suppport_props.setStartingPoint(pt1)
        self.suppport_props.setCondition("")
        support_line1 = SupportLine(self.suppport_props)

        #move the x point of starting by column section width
        pt1[Constants.X] += self.support.column_section_width * Constants.SCALE_FACTOR_COLUMNS
        #draw 2 half lines at end
        self.suppport_props.setStartingPoint(pt1)

        self.suppport_props.setCondition(SupportLine.ELEVATE)
        support_line2 = SupportLine(self.suppport_props)

        self.suppport_props.setCondition(SupportLine.LOWER)
        support_line3 = SupportLine(self.suppport_props)

        self.support_lines.append(support_line1)
        self.support_lines.append(support_line2)
        self.support_lines.append(support_line3)

    def endSupport(self):
        #3 support lines needed
        pt1 = list(self.support.starting_point)
        #draw 2 half lines at start
        self.suppport_props.setStartingPoint(pt1)
        
        self.suppport_props.setCondition(SupportLine.ELEVATE)
        support_line1 = SupportLine(self.suppport_props)

        self.suppport_props.setCondition(SupportLine.LOWER)
        support_line2 = SupportLine(self.suppport_props)

        #move the x point of starting by column section width
        #draw full line at end
        pt1[Constants.X] += self.support.column_section_width * Constants.SCALE_FACTOR_COLUMNS
        
        self.suppport_props.setCondition("")
        support_line3 = SupportLine(self.suppport_props)

        self.support_lines.append(support_line1)
        self.support_lines.append(support_line2)
        self.support_lines.append(support_line3)

    def midSupport(self):
        #4 support lines needed
        #draw 4 half lines
        pt1 = list(self.support.starting_point)
        self.suppport_props.setStartingPoint(pt1)
        
        self.suppport_props.setCondition(SupportLine.ELEVATE)
        support_line1 = SupportLine(self.suppport_props)

        self.suppport_props.setCondition(SupportLine.LOWER)
        support_line2 = SupportLine(self.suppport_props)

        pt1[Constants.X] += self.support.column_section_width * Constants.SCALE_FACTOR_COLUMNS
        self.suppport_props.setStartingPoint(pt1)
        
        self.suppport_props.setCondition(SupportLine.ELEVATE)
        support_line3 = SupportLine(self.suppport_props)

        self.suppport_props.setCondition(SupportLine.LOWER)
        support_line4 = SupportLine(self.suppport_props)

        self.support_lines.append(support_line1)
        self.support_lines.append(support_line2)
        self.support_lines.append(support_line3)
        self.support_lines.append(support_line4)

