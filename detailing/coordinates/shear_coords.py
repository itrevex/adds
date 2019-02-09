from .span_points import SpanPoints
from common.constants import Constants
from common.messages import Messages
from detailing.dxf_entities.entity_line import EntityLine

class ShearCoords(SpanPoints):

    def __init__(self, starting_point, span_length, beam_depth,
        left_column, right_column, scale_factor = 1):
        super(ShearCoords, self).__init__(starting_point, span_length, 
            beam_depth, scale_factor)

        self.left_column_width = left_column
        self.right_column_width = right_column
        self.start_point_links = self.start_point
        self.link_lines = {}

    def setLinkTypeLines(self, link_type):
        self.link_type = link_type
        self.link_lines[link_type.name] = self.getLinkLines()

    def getLinkLines(self):
        left_line = self.getLeftLine()
        left_top_point = left_line.pt1
        return [left_line, self.getRightLine(left_top_point)]

    def getLinesList(self):
        lines = []
        for link_lines in self.link_lines.values():
            lines.extend(link_lines)
        
        return lines

    def getLeftLine(self):
        
        left_line_top_point = self.changeXY(self.start_point_links, 
            self.left_column_width/2 + self.link_type.offset * SpanPoints.ONE_M_IN_MM,
            -Constants.LINKS_CUT_OFF_FROM_EDGE_OF_BEAM_LINE)
        
        left_line_bottom_point =  self.changeY(left_line_top_point, -self.beam_depth +
            2 * Constants.LINKS_CUT_OFF_FROM_EDGE_OF_BEAM_LINE)

        return EntityLine(left_line_top_point, left_line_bottom_point,
            Constants.LAYER_SHEAR_LINKS)

    def getRightLine(self, left_top_point):
        right_line_top_point = None
        if self.link_type.length != None:
            right_line_top_point = self.changeX(left_top_point, 
                self.link_type.length * SpanPoints.ONE_M_IN_MM)
            
        else:
            right_line_top_point = self.changeXY(self.end_point, 
                -self.right_column_width/2 - self.link_type.offset * SpanPoints.ONE_M_IN_MM,
                -Constants.LINKS_CUT_OFF_FROM_EDGE_OF_BEAM_LINE)
        
        right_line_bottom_point =  self.changeY(right_line_top_point, -self.beam_depth 
            + 2 * Constants.LINKS_CUT_OFF_FROM_EDGE_OF_BEAM_LINE)
        
        #this point needs to be returned to top of beam without the small cut off
        self.start_point_links = tuple(self.changeY(right_line_top_point, 
            Constants.LINKS_CUT_OFF_FROM_EDGE_OF_BEAM_LINE))
        #with new start point, there is no left column, but column on the right 
        #is still present
        self.left_column_width = 0

        return EntityLine(right_line_top_point, right_line_bottom_point, 
            Constants.LAYER_SHEAR_LINKS)
