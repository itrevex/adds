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

        self.end_point = self.changeX(self.start_point, span_length)

        pass


    def changeX(self, coord, value):
    
        '''
        change x coordinate of coord by the value sent in.
        A scale factor is applied if it is a user preference
        multiply span length by 1000 to change from m to mm
        '''

        new_coord = list(coord)
        new_coord[EntityLine.X] += (value * self.scale_factor 
            * SpanCoordinates.ONE_M_IN_MM)

        return tuple(new_coord)

    def getSpanLine(self):
        return EntityLine(self.start_point, self.end_point)

