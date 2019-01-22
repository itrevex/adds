import sys
sys.path.append('../common/')

from constants import Constants
from .entity_line import EntityLine

class SpanCoordinates:

    '''
    Span coordinate give the centre to centre coordinates of the span
    It gives coordinate of starting_point and end point

     |     |                              |     |
     |  ___|______________________________|___  |
     |  sta|rt                            |   en|d 
     |     |                              |     |  
    '''
    ONE_M_IN_MM = 1000.

    def __init__(self, starting_point, span_length, scale_factor = 1):
        
        self.scale_factor = scale_factor
        self.start_point = tuple(starting_point)

        self.end_point = self.changeX(self.start_point, 
            span_length * SpanCoordinates.ONE_M_IN_MM) #covert length to mm

        pass


    def changeX(self, coord, value):
    
        '''
        change x coordinate of coord by the value sent in.
        A scale factor is applied if it is a user preference
        multiply span length by 1000 to change from m to mm
        '''

        new_coord = list(coord)
        new_coord[EntityLine.X] += (value * self.scale_factor)

        return tuple(new_coord)


    def changeY(self, coord, value):
        
        '''
        change y coordinate of coord by the value sent in.
        A scale factor is applied if it is a user preference
        '''

        new_coord = list(coord)
        new_coord[EntityLine.Y] += (value * self.scale_factor)

        return tuple(new_coord)

    def getSpanLine(self):
        return EntityLine(self.start_point, self.end_point)



    def getColumnLines(self, top_width, bottom_width, beam_depth, left_column = True):
        column_lines = []
        if top_width != 0.0:
            line_1 = self.getColumnTopLine(-top_width/2, beam_depth, left_column)
            line_2 = self.getColumnTopLine(top_width/2, beam_depth, left_column)

            column_lines.append(line_1)
            column_lines.append(line_2)

        if bottom_width != 0.0:
            line_1 = self.getColumnBottomLine(-bottom_width/2, beam_depth, left_column)
            line_2 = self.getColumnBottomLine(bottom_width/2, beam_depth, left_column)

            column_lines.append(line_1)
            column_lines.append(line_2)

        return column_lines
        

    def getColumnTopLine(self, value, beam_depth, left_column):
        if left_column:
            start_point = list(self.start_point)
        else:
            start_point = list(self.end_point)

        pt1 = self.changeX(start_point, value)
        pt2 = self.changeY(pt1, beam_depth * Constants.COLUMN_LINE_FACTOR)

        return EntityLine(pt1, pt2)

    def getColumnBottomLine(self, value, beam_depth, left_column):
        if left_column:
            start_point = self.changeY(self.start_point, -beam_depth)
        else:
            start_point = self.changeY(self.end_point, -beam_depth)
        
        pt1 = self.changeX(start_point, value)
        pt2 = self.changeY(pt1, -beam_depth * Constants.COLUMN_LINE_FACTOR)

        return EntityLine(pt1, pt2)

    


