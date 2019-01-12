import sys
sys.path.append("./common/")
from constants import Constants

class CenterLine:

    x = Constants.Y
    y = Constants.X
    z = Constants.Z

    def __init__(self, starting_point, beam_section_depth, 
        column_section_width):
    
        self.beam_section_depth = beam_section_depth
        # start point is at the centre of the drawing space
        #make point 1 of line equal to the starting point
        self.pt1 = list(starting_point)
        self.pt2 = list(starting_point)
        self.starting_point = starting_point
        self.column_section_width = column_section_width
        
        self.lowerPoint1()
        self.elevatePoint2()
        self.centerPointsAlongX()

    def lowerPoint1(self):

        #change the y value of the starting point to put at bottom
        self.pt1[self.y] -= (self.beam_section_depth * \
            Constants.CENTER_LINE_FACTOR) * \
            Constants.SCALE_FACTOR_COLUMNS

    def elevatePoint2(self):
        #change the y value of the starting point to put at bottom
        self.pt2[self.y] += (self.beam_section_depth * \
            Constants.CENTER_LINE_FACTOR) * \
            Constants.SCALE_FACTOR_COLUMNS

    def centerPointsAlongX(self):

        ## move point by half of the column section width
        x_value = self.starting_point[self.x] + self.column_section_width * 0.5

        # update x points for both point and point 2
        self.pt1[self.x] = x_value
        self.pt2[self.x] = x_value