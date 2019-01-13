import sys
sys.path.append("./common/")
from support_line import SupportLine
from constants import Constants

class SupportLines:
    def __init__(self, support):
        self.support_lines = []
        self.support = support
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
        pt1 = self.support.starting_point
        #draw full line at start
        support_line1 = SupportLine(pt1, self.support.beam_depth)

        #move the x point of starting by column section width
        pt1[Constants.X] += self.support.column_section_width * Constants.SCALE_FACTOR_COLUMNS
        #draw 2 half lines at end
        support_line2 = SupportLine(pt1, self.support.beam_depth, SupportLine.ELEVATE)
        support_line3 = SupportLine(pt1, self.support.beam_depth, SupportLine.LOWER)

        self.support_lines.append(support_line1)
        self.support_lines.append(support_line2)
        self.support_lines.append(support_line3)

    def endSupport(self):
        #3 support lines needed
        pt1 = self.support.starting_point
        #draw 2 half lines at start
        support_line1 = SupportLine(pt1, self.support.beam_depth, SupportLine.ELEVATE)
        support_line2 = SupportLine(pt1, self.support.beam_depth, SupportLine.LOWER)

        #move the x point of starting by column section width
        #draw full line at end
        pt1[Constants.X] += self.support.column_section_width * Constants.SCALE_FACTOR_COLUMNS
        support_line3 = SupportLine(pt1, self.support.beam_depth)

        self.support_lines.append(support_line1)
        self.support_lines.append(support_line2)
        self.support_lines.append(support_line3)

    def midSupport(self):
        #4 support lines needed
        #draw 4 half lines
        pt1 = self.support.starting_point
        support_line1 = SupportLine(pt1, self.support.beam_depth, SupportLine.ELEVATE)
        support_line2 = SupportLine(pt1, self.support.beam_depth, SupportLine.LOWER)

        pt1[Constants.X] += self.support.column_section_width * Constants.SCALE_FACTOR_COLUMNS
        
        support_line3 = SupportLine(pt1, self.support.beam_depth, SupportLine.ELEVATE)
        support_line4 = SupportLine(pt1, self.support.beam_depth, SupportLine.LOWER)

        self.support_lines.append(support_line1)
        self.support_lines.append(support_line2)
        self.support_lines.append(support_line3)
        self.support_lines.append(support_line4)

