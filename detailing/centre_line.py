
from common.constants import Constants
from .support_line import SupportLine

class CentreLine(SupportLine):

    def __init__(self, support_props):
        # start point is at the centre of the drawing space
        #make point 1 of line equal to the starting point
        super().__init__(support_props)
        self.column_section_width = support_props.column_section_width
        self.centerPointsAlongX()


    def centerPointsAlongX(self):

        ## move point by half of the column section width
        x_value = self.starting_point[Constants.X] + self.column_section_width * 0.5

        # update x points for both point and point 2
        self.pt1[Constants.X] = x_value
        self.pt2[Constants.X] = x_value


