from beams.section import Section
from .entity_line import EntityLine

class SectionCoordinates:

    '''
    starting_point is a tuple representing with
    x at the centre of the section and y at the bottom 
    of the beam (at beam depth = max_value or beam height = 0.)
    '''

    VERTEX_1 = "vertex_1"
    VERTEX_2 = "vertex_2"
    VERTEX_3 = "vertex_3"
    VERTEX_4 = "vertex_4"
    VERTEX_5 = "vertex_5"
    VERTEX_6 = "vertex_6"
    VERTEX_7 = "vertex_7"
    VERTEX_8 = "vertex_8"

    def __init__(self, starting_point, section, beam_depth = None, scale_factor = 1.):
        
        self.starting_point = list(map(float, starting_point))
        self.section = section
        self.scale_factor = float(scale_factor)
        self.section_depth = self.getSectionDepth(beam_depth)
        

    def getSectionDepth(self, beam_depth):
        if (beam_depth == None):
            return self.section.d
        return beam_depth

    def getVertices(self):
        if (self.section.type == Section.SQUARE_SECTION):
            return self.getSquareVertices()

        return None

    def changeY(self, coord, value):
    
        '''
        change y coordinate of coord by the value sent in.
        A scale factor is applied if it is a user preference
        '''

        new_coord = list(coord)
        new_coord[EntityLine.Y] += (value * self.scale_factor)

        return new_coord

    def changeX(self, coord, value):

        '''
        change x coordinate of coord by the value sent in.
        A scale factor is applied if it is a user preference
        '''

        new_coord = list(coord)
        new_coord[EntityLine.X] += (value * self.scale_factor)

        return new_coord

    def getSquareVertices(self):
        '''

        Vertices for square sections

                bw
          2  -------  3
            |       |
            |       |
   section  |       |
    depth   |       |
            |       |
         1   -------  4

        '''

        vertex_1 = list(self.starting_point)
        vertex_2 = self.changeY(vertex_1, self.section_depth)
        vertex_3 = self.changeX(vertex_2, self.section.bw)
        vertex_4 = self.changeX(vertex_1, self.section.bw)
        vertices = {}

        vertices [SectionCoordinates.VERTEX_1] = vertex_1
        vertices [SectionCoordinates.VERTEX_2] = vertex_2
        vertices [SectionCoordinates.VERTEX_3] = vertex_3
        vertices [SectionCoordinates.VERTEX_4] = vertex_4

        return vertices



    def getLRightVertices(self):
        '''

        Vertices for L ection right flange

          2  ------------------- 3
            |                   |
            |                   |
            |        ----------- 4
            |       | 5
            |       |
            |       |
            |       |
            |       |
         1   -------  6

        '''
        pass

    def getLLeftVertices(self):
        '''

        Vertices for L section left flange

          4  -------------------   5
            |                   |
            |                   |
          3  -----------        |        
                      2 |       |
                        |       |
                        |       |
                        |       |
                        |       |
                      1  -------   6

        '''
        pass

    def tVertices(self):
        '''

        Vertices for T sections

          4  -------------------------------    5
            |                               |
            |                               |
          3  -----------         -----------   6    
                    2   |       |  7
                        |       |
                        |       |
                        |       |
                        |       |
                      1  -------   8

        '''
        pass
