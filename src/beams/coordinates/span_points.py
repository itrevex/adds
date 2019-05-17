from .coord_change import ChoordChange

class SpanPoints(ChoordChange):
    
    '''
    Span coordinate give the centre to centre coordinates of the span
    It gives coordinate of starting_point and end point

     |     |                              |     |
     |  ___|______________________________|___  |
     |  sta|rt                            |   en|d 
     |     |                              |     |  

     start_point is at top beam_line on the left
    '''
    ONE_M_IN_MM = 1.

    def __init__(self, starting_point, span_length, beam_depth, scale_factor = 1):
        
        super(SpanPoints, self).__init__(scale_factor)

        self.beam_depth = float(beam_depth)
        self.span_length = span_length * SpanPoints.ONE_M_IN_MM

        self.start_point = tuple(starting_point)
        self.end_point = tuple(self.changeX(self.start_point, self.span_length)) #covert length to mm
