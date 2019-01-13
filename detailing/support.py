from centre_line import CentreLine
from support_lines import SupportLines

class Support:
    STARTING_POINT = "starting_point"
    BEAM_DEPTH = "beam_depth"
    COLUMN_SECTION_WIDTH = "column_section_width"
    SUPPORT_LOCATION = "support_location"

    def __init__(self):
        self.support_location = "mid"
        self.beam_depth = 400
        self.column_section_width = 300
        self.starting_point = [0.,0.,0.]
        self.support_objects = []
        pass

    def getSupportObjects(self):
      
        centreline = CentreLine(self.starting_point, 
            self.beam_depth, self.column_section_width)

        support_lines = SupportLines(self)

        self.support_objects.append(centreline)
        self.support_objects.extend(support_lines.support_lines)
 
        return self.support_objects

    def setStartingPoint(self, starting_point):
        self.starting_point = starting_point

    def setBeamDepth(self, beam_depth):
        self.beam_depth = beam_depth

    def setColumnSectionWidth(self, column_section_width):
        self.column_section_width = column_section_width

    def setSupportLocation(self, support_location):
        self.support_location = support_location

    