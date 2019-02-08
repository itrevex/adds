from .span_points import SpanPoints
from common.constants import Constants
from detailing.dxf_entities.entity_line import EntityLine

class ShearCoords(SpanPoints):

    def __init__(self, starting_point, span_length, beam_depth, link_type,
        left_column, right_column, scale_factor = 1):
        super(ShearCoords, self).__init__(starting_point, span_length, 
            beam_depth, scale_factor)

        self.left_column_width = left_column
        self.right_column_width = right_column
        self.link_type = link_type

    def getLines(self):
        return [self.getLeftLine(), self.getRightLine()]

    def getLeftLine(self):
        left_line_top_point = self.changeX(self.start_point, 
            self.left_column_width/2 + self.link_type.offset * SpanPoints.ONE_M_IN_MM)
        
        left_line_bottom_point =  self.changeY(left_line_top_point, -self.beam_depth)

        return EntityLine(left_line_top_point, left_line_bottom_point,
            Constants.LAYER_SHEAR_LINKS)

    def getRightLine(self):
        right_line_top_point = self.changeX(self.end_point, 
            -self.right_column_width/2 - self.link_type.offset * SpanPoints.ONE_M_IN_MM)
        
        right_line_bottom_point =  self.changeY(right_line_top_point, -self.beam_depth)

        return EntityLine(right_line_top_point, right_line_bottom_point, 
            Constants.LAYER_SHEAR_LINKS)