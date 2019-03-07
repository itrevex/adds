from .span_points import SpanPoints
from common.constants import Constants
from common.messages import Messages
from beams.dxf_entities.entity_line import EntityLine
from beams.dxf_entities.entity_text import EntityText

class ShearCoords(SpanPoints):

    def __init__(self, span_data, left_column, right_column, scale_factor = 1):
        super(ShearCoords, self).__init__(span_data.starting_point, span_data.data.span_length, 
            span_data.beam.data.beam_depth, scale_factor)

        self.left_column_width = left_column
        self.right_column_width = right_column

        self.start_point_links = tuple(span_data.starting_point)
        self.span_data = span_data
        self.link_lines = {}
        self.label_entities = {}

        #for debug purposes
        #todo remove debug statement
        self.setLinkTypeLines()

    def setLinkTypeLines(self):
        # loop through the links contained within a single span
        for link in self.span_data.data.links:
            #get link type
            shear_link = self.span_data.shear_links[link]
            self.link_type = shear_link
            lines = self.getLinkLines()
            self.link_lines[shear_link.name] = lines
            self.label_entities[shear_link.name] = self.getLabelEntity(shear_link, lines[0])
        
        

    def getLinkLines(self):
        left_line = self.getLeftLine()
        left_top_point = left_line.pt1
        return [left_line, self.getRightLine(left_top_point)]

    def getEntitiesList(self):
        entities = []
        for name, link_lines in self.link_lines.items():
            entities.extend(link_lines)
            entities.append(self.label_entities[name])
        
        return entities

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

    def getLabelEntity(self, link, left_line):
        #get the spacing
        #get the total distance covered by links
        #see how many links can fit within the minimum offset
        number_of_links = int(link.length * SpanPoints.ONE_M_IN_MM/link.spacing)
        label = str(number_of_links)
        label += link.diameter+"-"+link.bar_mark+"-"
        label += str(int(link.spacing)) + Constants.LINK_TEXT
        link.setLabel(label)
        
        return self.getTextEntity(link, left_line)
        

    def getTextEntity(self, link, left_line):
        # find label length
        text = EntityText(link.label, height=Constants.LINK_LABEL_TEXT_HEIGHT)
        label_length = text.getTextLenth()
        
        # change y to a given constant distance from bottom beam line
        pos = self.changeY(left_line.pt2, Constants.SHEAR_DIM_BOTTOM_OFFSET)

        # change x to the center of the links length then back by the half label length
        link_length = link.length * SpanPoints.ONE_M_IN_MM

        if (link_length > label_length):
            pos = self.changeX(pos, (link_length -label_length)/2)

        text.setPos(pos)

        return text
        