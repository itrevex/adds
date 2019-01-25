
from common.constants import Constants
from .entity_line import EntityLine

class SupportLine(EntityLine):

    x = Constants.X
    y = Constants.Y
    z = Constants.Z

    ELEVATE = "elevate"
    LOWER = "lower"

    def __init__(self, support_props):
    
        self.beam_section_depth = support_props.beam_depth
        self.height_multiplication_factor = support_props.mulltiplication_factor
        self.condition = support_props.condition
        self.starting_point = support_props.starting_point
        # start point is at the centre of the drawing space
        #make point 1 of line equal to the starting point
        
        pt1 = list(support_props.starting_point)
        pt2 = list(support_props.starting_point)

        super().__init__(pt1, pt2, support_props.layer)

        
        self.full_evalation = self.beam_section_depth * Constants.COLUMN_LINE_FACTOR
        self.elevation_to_beam_top = self.beam_section_depth * 0.5

        self.getLinePoints()
        
    def getLinePoints(self):
        if (self.condition == SupportLine.ELEVATE):
            self.pt2 = self.elevatePoint(self.pt2,self.full_evalation)
            self.pt1 = self.elevatePoint(self.pt1, self.elevation_to_beam_top)
        elif(self.condition == SupportLine.LOWER):
            self.pt2 = self.lowerPoint(self.pt2, self.full_evalation)
            self.pt1 = self.lowerPoint(self.pt1, self.elevation_to_beam_top)
        else:
            self.pt2 = self.elevatePoint(self.pt2,self.full_evalation)
            self.pt1 = self.lowerPoint(self.pt1, self.full_evalation)

    def lowerPoint(self, pt, value):

        #change the y value of the starting point to put at bottom
        pt[self.y] -=  value * self.height_multiplication_factor
        return pt

    def elevatePoint(self, pt, value):
        #change the y value of the starting point to put at bottom
        pt[self.y] += value * self.height_multiplication_factor
        return pt


