from .entity_line import EntityLine

class SectionCoordinates:

    '''
    starting_point is a tuple representing with
    x at the centre of the section and y at the bottom 
    of the beam (at beam depth = max_value or beam height = 0.)
    '''

    L_RIGHT_SECTION = "l_right_section"
    L_LEFT_SECTION = "l_left_section"
    T_SECTION = "t_section"
    SQUARE_SECTION = "square_section"

    VERTEX_1 = "vertex_1"
    VERTEX_2 = "vertex_2"
    VERTEX_3 = "vertex_3"
    VERTEX_4 = "vertex_4"
    VERTEX_5 = "vertex_5"
    VERTEX_6 = "vertex_6"
    VERTEX_7 = "vertex_7"
    VERTEX_8 = "vertex_8"

    #Connectivities for the different entities
    #square connectivies
    SQUARE_CONNECTIVITIES = ((1,2), (2,3), (3,4), (4,1))
    L_CONNECTIVITIES = ((1,2), (2,3), (3,4), (4,5), (5,6), (6,1))
    T_CONNECTIVITIES = ((1,2), (2,3), (3,4), (4,5), (5,6), (6,7), (7,8), (8,1))

    def __init__(self, starting_point, section, beam_depth = None, scale_factor = 1.):
        
        self.starting_point = list(map(float, starting_point))
        self.section = section
        self.scale_factor = float(scale_factor)
        self.section_depth = self.getSectionDepth(beam_depth)
        self.vertices = self.getVertices()
        

    def getSectionDepth(self, beam_depth):
        if (beam_depth == None):
            return self.section.d
        return beam_depth

    def getVertices(self):
        if (self.section.type == SectionCoordinates.SQUARE_SECTION):
            return self.getSquareVertices()

        if (self.section.type == SectionCoordinates.L_RIGHT_SECTION):
            return self.getLRightVertices()

        if (self.section.type == SectionCoordinates.L_LEFT_SECTION):
            return self.getLLeftVertices()

        if (self.section.type == SectionCoordinates.T_SECTION):
            return self.getTVertices()

        return None
    
    def getEntities(self):
        if (self.section.type == SectionCoordinates.SQUARE_SECTION):
            return self.getLines(SectionCoordinates.SQUARE_CONNECTIVITIES)

        if self.section.type == SectionCoordinates.T_SECTION:
            return self.getLines(SectionCoordinates.T_CONNECTIVITIES)   

        return self.getLines(SectionCoordinates.L_CONNECTIVITIES)
    
    def getVertexName(self, id):
        return "vertex_" + str(id)

    
    def getLines(self, connectivities):
        lines = []
        for connectivity in connectivities:
            vertex_start = self.getVertexName(connectivity[0])
            vertex_end = self.getVertexName(connectivity[1])
            line = EntityLine(self.vertices[vertex_start], 
                self.vertices[vertex_end])
            lines.append(line)
            
        return lines

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
                   bf
          2  ------------------- 3
            |                   | df
            |                   |
            |        ----------- 4
   section  |       | 5
    depth   |       |
            |       |
            |       |
            |       |
         1   -------  6
               bw
        '''
        vertex_1 = list(self.starting_point)
        vertex_2 = self.changeY(vertex_1, self.section_depth)
        vertex_3 = self.changeX(vertex_2, self.section.bf)
        vertex_4 = self.changeY(vertex_3, -(self.section.df))
        vertex_6 = self.changeX(vertex_1, self.section.bw)
        vertex_5 = self.changeY(vertex_6, (self.section_depth - self.section.df))

        vertices = {}
        vertices [SectionCoordinates.VERTEX_1] = vertex_1
        vertices [SectionCoordinates.VERTEX_2] = vertex_2
        vertices [SectionCoordinates.VERTEX_3] = vertex_3
        vertices [SectionCoordinates.VERTEX_4] = vertex_4
        vertices [SectionCoordinates.VERTEX_5] = vertex_5
        vertices [SectionCoordinates.VERTEX_6] = vertex_6

        return vertices


    def getLLeftVertices(self):
        '''

        Vertices for L section left flange
                  bf
          4  -------------------   5
         df |                   |
            |                   |
          3  -----------        |        
                      2 |       |  section
                        |       |   depth
                        |       |
                        |       |
                        |       |
                      1  -------   6
                           bw
        '''
        vertex_1 = list(self.starting_point)
        vertex_6 = self.changeX(vertex_1, self.section.bw)
        vertex_5 = self.changeY(vertex_6, self.section_depth)
        vertex_4 = self.changeX(vertex_5, -self.section.bf)
        vertex_3 = self.changeY(vertex_4, -self.section.df)
        vertex_2 = self.changeX(vertex_3, (self.section.bf - self.section.bw))

        

        vertices = {}
        vertices [SectionCoordinates.VERTEX_1] = vertex_1
        vertices [SectionCoordinates.VERTEX_2] = vertex_2
        vertices [SectionCoordinates.VERTEX_3] = vertex_3
        vertices [SectionCoordinates.VERTEX_4] = vertex_4
        vertices [SectionCoordinates.VERTEX_5] = vertex_5
        vertices [SectionCoordinates.VERTEX_6] = vertex_6

        return vertices

    def getTVertices(self):
        '''

        Vertices for T sections
                        bf
          4  -------------------------------    5     |
            |                               | df      |
            |                               |         | 
          3  -----------         -----------   6      |
            w_offset  2 |       |  7                  |
                        |       |                     |  section
                        |       |                     |   depth
                        |       |                     |
                        |       |                     |
                      1  -------   8                  
                           bw
        '''

        vertex_1 = list(self.starting_point)
        vertex_2 = self.changeY(vertex_1, self.section_depth - self.section.df)
        vertex_3 = self.changeX(vertex_2, -self.section.w_offset)
        vertex_4 = self.changeY(vertex_3, self.section.df)
        vertex_5 = self.changeX(vertex_4, self.section.bf)
        vertex_6 = self.changeY(vertex_5, -self.section.df)
        vertex_7 = self.changeX(vertex_3, self.section.w_offset + self.section.bw)
        vertex_8 = self.changeX(vertex_1, self.section.bw)

        

        vertices = {}
        vertices [SectionCoordinates.VERTEX_1] = vertex_1
        vertices [SectionCoordinates.VERTEX_2] = vertex_2
        vertices [SectionCoordinates.VERTEX_3] = vertex_3
        vertices [SectionCoordinates.VERTEX_4] = vertex_4
        vertices [SectionCoordinates.VERTEX_5] = vertex_5
        vertices [SectionCoordinates.VERTEX_6] = vertex_6
        vertices [SectionCoordinates.VERTEX_7] = vertex_7
        vertices [SectionCoordinates.VERTEX_8] = vertex_8

        return vertices
