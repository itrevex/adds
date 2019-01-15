import sys
sys.path.append("./common/")
from constants import Constants

from centre_line import CentreLine
from support_lines import SupportLines
from support_properties import SupportProps

class Support:
    STARTING_POINT = "starting_point"
    BEAM_DEPTH = "beam_depth"
    COLUMN_SECTION_WIDTH = "column_section_width"
    SUPPORT_LOCATION = "support_location"

    def __init__(self, attribs):
        self.support_location = attribs[Support.SUPPORT_LOCATION] #"mid"
        self.beam_depth = attribs[Support.BEAM_DEPTH] #400
        self.column_section_width = attribs[Support.COLUMN_SECTION_WIDTH] #300
        self.starting_point = tuple(attribs[Support.STARTING_POINT]) #[0.,0.,0.]
        pass

    def getSupportObjects(self):
        '''
        return list of drawable support objects
        These include the centre line, support vertical lines
        and zigzag decoration on top of support
        '''
        support_objects = []
        support_objects.append(self.getCentreLine())
        support_objects.extend(self.getSupportLines())
 
        return support_objects

    def getCentreLine(self):
        '''
        return single drawable object
        '''

        support_props = SupportProps(self.beam_depth, Constants.LAYER_CENTER_LINES, 
            Constants.CENTER_LINE_FACTOR, self.starting_point, 
            column_section_width=self.column_section_width)
        centreLine =  CentreLine(support_props)
        
        return centreLine

    def getSupportLines(self):
        '''
        return list of drawable objects
        '''
        return SupportLines(self).support_lines

    def setStartingPoint(self, starting_point):
        self.starting_point = starting_point

    def setBeamDepth(self, beam_depth):
        self.beam_depth = beam_depth

    def setColumnSectionWidth(self, column_section_width):
        self.column_section_width = column_section_width

    def setSupportLocation(self, support_location):
        self.support_location = support_location

    