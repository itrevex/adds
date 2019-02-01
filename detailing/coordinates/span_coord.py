
from common.constants import Constants
from detailing.dxf_entities.entity_line import EntityLine
from detailing.dxf_entities.entity_circle import EntityCircle
from .coord_change import ChoordChange

class SpanCoordinates(ChoordChange):

    '''
    Span coordinate give the centre to centre coordinates of the span
    It gives coordinate of starting_point and end point

     |     |                              |     |
     |  ___|______________________________|___  |
     |  sta|rt                            |   en|d 
     |     |                              |     |  
    '''
    ONE_M_IN_MM = 1000.

    def __init__(self, starting_point, span_length, beam_depth, scale_factor = 1):
        
        super(SpanCoordinates, self).__init__(scale_factor)

        self.beam_depth = float(beam_depth)
        self.span_length = span_length * SpanCoordinates.ONE_M_IN_MM

        self.start_point = tuple(starting_point)
        self.end_point = self.changeX(self.start_point, self.span_length) #covert length to mm

        

        pass

    def getSpanLine(self):
        return EntityLine(self.start_point, self.end_point)

    def getColumnLines(self, top_width, bottom_width, left_column = True):
        column_lines = []

        #check to see if there is a top column
        if top_width != 0.0:
            #draw left and right lines of the column
            left_line = self.getColumnTopLine(-top_width/2, left_column)
            right_line = self.getColumnTopLine(top_width/2, left_column)

            #draw zigzag lines on top of column
            z_lines = self.drawZ(top_width, left_line.pt2, right_line.pt2)

            column_lines.append(left_line)
            column_lines.append(right_line)
            column_lines.extend(z_lines)

        #check to see if there is a bottom column
        if bottom_width != 0.0:
            
            left_line = self.getColumnBottomLine(-bottom_width/2, left_column)
            right_line = self.getColumnBottomLine(bottom_width/2, left_column)

            z_lines = self.drawZ(bottom_width, left_line.pt2, right_line.pt2)

            column_lines.append(left_line)
            column_lines.append(right_line)
            column_lines.extend(z_lines)

        #get the centerline for column
        center_line = self.getCenterLine(left_column)

        #get circle on top of centre line. EntityLine pt1 is top and pt2 is bottom
        circle = self.getCentreLineCircle(center_line)

        #get grid letter/number to add inside circle

        column_lines.append(center_line)
        column_lines.append(circle)

        return column_lines

    def getGridText(self):
        pass
        
    def getCentreLineCircle(self, centre_line):
        '''
        centre_line.pt1 - top point,
        centre_line.pt2 - bottom point
        circle is drawn on the top point
        '''
        # EntityCircle
        radius = Constants.GRID_CIRCLE_RADIUS * Constants.GRID_CIRCLE_FACTOR
        pt1 = self.changeY(centre_line.pt1, radius)
        return EntityCircle(pt1, radius, Constants.LAYER_GRID_LINES)

    def getColumnTopLine(self, value, left_column):
        if left_column:
            start_point = list(self.start_point)
        else:
            start_point = list(self.end_point)

        pt1 = self.changeX(start_point, value)
        pt2 = self.changeY(pt1, self.beam_depth * Constants.COLUMN_LINE_FACTOR)

        return EntityLine(pt1, pt2, Constants.LAYER_SUPPORT_LINES)

    def getColumnBottomLine(self, value, left_column):
        if left_column:
            start_point = self.changeY(self.start_point, -self.beam_depth)
        else:
            start_point = self.changeY(self.end_point, -self.beam_depth)
        
        pt1 = self.changeX(start_point, value)
        pt2 = self.changeY(pt1, -self.beam_depth * Constants.COLUMN_LINE_FACTOR)

        return EntityLine(pt1, pt2, Constants.LAYER_SUPPORT_LINES)

    def getCenterLine(self, left_column):
        if left_column:
            start_point = list(self.start_point)
        else:
            start_point = list(self.end_point)

        top_point = self.changeY(start_point, 
            self.beam_depth * Constants.CENTER_LINE_FACTOR)
        bottom_line = self.changeY(start_point, 
            -self.beam_depth - self.beam_depth * Constants.CENTER_LINE_FACTOR)

        return EntityLine(top_point, bottom_line, Constants.LAYER_CENTER_LINES)

    def drawZ(self, column_width, end_left, end_right):
        '''
        Z is the the zizzag that closes up or breaks the column at the end

                           4
                           /\
             1 _______ 2  /  \______ 6
                      \  /   5
                       \/
                       3
        '''

        pt1 = self.changeX(end_left, -column_width * Constants.Z_OUTER_SEGMENT)
        pt2 = self.changeX(end_left, column_width * Constants.Z_INNER_SEGMENT)

        pt6 = self.changeX(end_right, column_width * Constants.Z_OUTER_SEGMENT)
        pt5 = self.changeX(end_right, -column_width * Constants.Z_OUTER_SEGMENT)

        pt3 = self.changeXY(end_left, column_width * Constants.Z_TIP_LENGTH,
            -column_width * Constants.Z_TIP_DEPTH)

        pt4 = self.changeXY(end_right, -column_width * Constants.Z_TIP_LENGTH,
            column_width * Constants.Z_TIP_DEPTH)


        line_1_2 = EntityLine(pt1, pt2, Constants.LAYER_ZIGZAG_LINES)
        line_2_3 = EntityLine(pt2, pt3, Constants.LAYER_ZIGZAG_LINES)
        line_3_4 = EntityLine(pt3, pt4, Constants.LAYER_ZIGZAG_LINES)
        line_4_5 = EntityLine(pt4, pt5, Constants.LAYER_ZIGZAG_LINES)
        line_5_6 = EntityLine(pt5, pt6, Constants.LAYER_ZIGZAG_LINES)

        return [line_1_2, line_2_3, line_3_4, line_4_5, line_5_6]

    def getBeamLines(self, beam_start_point, total_span_length, 
        column_widths):
        
        #set up input data
        column_start_top_width = column_widths[0]
        column_start_bottom_width = column_widths[1]
        column_end_top_width = column_widths[2]
        column_end_bottom_width = column_widths[3]

        total_length = total_span_length * SpanCoordinates.ONE_M_IN_MM

        #beam top line
        top_start_point = self.changeX(beam_start_point, -column_start_top_width/2)
        top_end_point = self.changeX(beam_start_point, total_length + column_end_top_width/2)
        top_line = EntityLine(top_start_point, top_end_point, 
            Constants.LAYER_BEAM_LINES)

        #beam bottom line
        bottom_start_point = self.changeXY(beam_start_point, 
            -column_start_bottom_width/2, -self.beam_depth)

        bottom_end_point = self.changeXY(beam_start_point, 
            total_length + column_end_bottom_width/2, -self.beam_depth)

        bottom_line = EntityLine(bottom_start_point, bottom_end_point, 
            Constants.LAYER_BEAM_LINES)

        #left and right closing line
        left_line = EntityLine(top_start_point, bottom_start_point, 
            Constants.LAYER_BEAM_LINES)
        right_line = EntityLine(top_end_point, bottom_end_point, 
            Constants.LAYER_BEAM_LINES)

        return [top_line, bottom_line, left_line, right_line]

    def getSectionLines(self, column_widths, left_section, right_section, beam_name = "beam"):

        '''
        Beam name is only required in the event that there is a warning that 
        needs to be shown to the user
        
                    |                                               |
        self.start _|___4_____________________________________8_____|___________
                    |   |______________________________________|    |
                    |   3                                     7     |
                    |    ______________________________________     |
                    |   | 2                                  6 |    |
                    |   |                                      |    |
                   _|___| 1                                  5 |____|__
                    |                                               |
                    |                                               |

        if points 3 or 7 above 4 or 8 at start of beam depth,
        don't draw 3 to 7
        '''

        #set up in put data
        left_column_top_width = column_widths[0]
        left_column_bottom_width = column_widths[1]
        right_column_top_width = column_widths[2]
        right_column_bottom_width = column_widths[3]

        #lines list
        section_lines = []

        pt1 = self.changeXY(self.start_point, self.getHalfWidth(left_column_bottom_width), 
            -self.beam_depth)
        pt3 = self.changeY(pt1, left_section.d)
        pt2 = self.changeY(pt3, -left_section.df)
        pt4 = self.changeX(self.start_point, self.getHalfWidth(left_column_top_width))
        
        pt5 = self.changeXY(self.start_point, self.span_length 
            - self.getHalfWidth(right_column_bottom_width),-self.beam_depth)
        pt7 = self.changeY(pt5, right_section.d)
        pt6 = self.changeY(pt7, -right_section.df)
        pt8 = self.changeX(self.start_point, self.span_length 
            - self.getHalfWidth(right_column_top_width))

        self.showWarning(pt2, pt4, pt3, pt6, pt7, pt8, 
            left_section, right_section)

        line_1_2 = EntityLine(pt1, pt2, Constants.LAYER_BEAM_LINES)
        line_5_6 = EntityLine(pt5, pt6, Constants.LAYER_BEAM_LINES)

        #add created lines to lines pool
        section_lines.append(line_1_2)
        section_lines.append(line_5_6)
        
        #Do the neccessary checks so that you do not draw useless lines

        #line 2 to 6 if both 2 and 6 are not above or equal to 4 and 8
        #respectively
        if pt2[EntityLine.Y] < pt4[EntityLine.Y] or pt6[EntityLine.Y] < pt8[EntityLine.Y]:
            line_2_6 = EntityLine(pt2, pt6, Constants.LAYER_BEAM_LINES)
            section_lines.append(line_2_6)

        #same logic as above for line 3 to 7
        if pt3[EntityLine.Y] < pt4[EntityLine.Y] or pt7[EntityLine.Y] < pt8[EntityLine.Y]:
            line_3_7 = EntityLine(pt3, pt7, Constants.LAYER_BEAM_LINES)
            section_lines.append(line_3_7)

        
        #Lines 3 to 4 and 7 to 8 will the logic above but each independently
        #Draw line 3 to 4 if pt3 is below pt4 vertically
        if pt3[EntityLine.Y] < pt4[EntityLine.Y]:
            line_3_4 = EntityLine(pt3, pt4, Constants.LAYER_BEAM_LINES)
            section_lines.append(line_3_4)

        #Use similar logic for line 7 to 8
        if pt7[EntityLine.Y] < pt8[EntityLine.Y]:
            line_7_8 = EntityLine(pt7, pt8, Constants.LAYER_BEAM_LINES)
            section_lines.append(line_7_8)
        
        return section_lines

    def showWarning(self, pt2, pt4, pt3, pt6, pt7, pt8, left_section, right_section):
        #check to see if left section is deeper than beam 
        if pt2[EntityLine.Y] > pt4[EntityLine.Y] or \
            pt3[EntityLine.Y] > pt4[EntityLine.Y]:
        
            print("Waring! %s deeper than beam" 
                %(left_section.name))

        #check to see if right section is deeper than beam 
        if pt6[EntityLine.Y] > pt8[EntityLine.Y] or \
            pt7[EntityLine.Y] > pt8[EntityLine.Y]: 

            print("Waring! %s deeper than beam" %(right_section.name))
            pass

    def getHalfWidth(self, column_width):
        '''
        This is done to prevent the divide by zero error incase of cantilevered
        beams
        '''
        if column_width == 0.:
            return 0.

        return column_width / 2

    


