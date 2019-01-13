import sys
sys.path.append("./common/")
from constants import Constants

class SupportLine:

    x = Constants.X
    y = Constants.Y
    z = Constants.Z

    ELEVATE = "elevate"
    LOWER = "lower"

    def __init__(self, starting_point, beam_section_depth, condition = ""):
    
        self.beam_section_depth = beam_section_depth
        # start point is at the centre of the drawing space
        #make point 1 of line equal to the starting point
        self.layer = Constants.LAYER_SUPPORT_LINES
        self.pt1 = list(starting_point)
        self.pt2 = list(starting_point)
        self.starting_point = starting_point
        
        self.full_evalation = self.beam_section_depth * Constants.COLUMN_LINE_FACTOR
        self.elevation_to_beam_top = self.beam_section_depth * 0.5

        #This is if it is a starting point
        if (condition == SupportLine.ELEVATE):
            self.pt2 = self.elevatePoint(self.pt2,self.full_evalation)
            self.pt1 = self.elevatePoint(self.pt1, self.elevation_to_beam_top)
        elif(condition == SupportLine.LOWER):
            self.pt2 = self.lowerPoint(self.pt2, self.full_evalation)
            self.pt1 = self.lowerPoint(self.pt1, self.elevation_to_beam_top)
        else:
            self.pt2 = self.elevatePoint(self.pt2,self.full_evalation)
            self.pt1 = self.lowerPoint(self.pt1, self.full_evalation)
        

    def lowerPoint(self, pt, value):

        #change the y value of the starting point to put at bottom
        pt[self.y] -=  value* Constants.SCALE_FACTOR_COLUMNS
        return pt

    def elevatePoint(self, pt, value):
        #change the y value of the starting point to put at bottom
        pt[self.y] += value* Constants.SCALE_FACTOR_COLUMNS
        return pt

    def getLayerName(self):
        return self.layer

