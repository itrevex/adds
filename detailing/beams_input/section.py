from ..coordinates.section_coord import SectionCoordinates

class Section:

    # SECTIONS_B = "b" #b - total width of section
    SECTIONS_BF_TOP = 2 #bf_top - width  of flange on top
    # SECTIONS_BF_BOTTOM = "bf_bottom" #bf_bottom - width of flange at the bottom
    SECTIONS_BW = 3 #bw - width of web
    SECTIONS_D = 4 #d - total depth of section
    SECTIONS_DF = 5 #df - depth of flange
    SECTIONS_W_OFFSET = 6 #w_offset - off set of web from left starting point of section
    SECTION_NAME = 1
    '''
    "b" stands for width and "d" stands for depth
    "f" stands for flange and "w" stands for web

    b - total width of section
    bf_top - width  of flange on top
    bf_bottom - width of flange at the bottom
    bw - width of web
    d - total depth of section
    df - depth of flange
    w_offset - off set of web from left starting point of section
    '''

    
    def __init__(self, section_props):
        self.b = 0.
        self.section_props = section_props
        self.bf_top = self.updateProp(Section.SECTIONS_BF_TOP)
        self.bf_bottom = 0.
        self.bw = self.updateProp(Section.SECTIONS_BW)
        self.d = self.updateProp(Section.SECTIONS_D)
        self.df = self.updateProp(Section.SECTIONS_DF)
        self.w_offset = self.updateProp(Section.SECTIONS_W_OFFSET)
        self.bf = self.setBf()
        self.name = self.section_props[Section.SECTION_NAME]

        #method has to be called after initializing other parameters
        self.type = self.getSectionType()

    def updateProp(self, key):
        try:
            if(self.section_props[key] == "X"):
                return 0.
            return float(self.section_props[key])
        except IndexError:
            return 0.

    def getSectionType(self):
        # 3 section type
        # T, L and square
        if (self.df == 0.):
            #this is a square section, it has no flange depth
            return SectionCoordinates.SQUARE_SECTION
        else:
            if (self.w_offset == 0.):
                #this is an L section with flange protruding to the right
                return SectionCoordinates.L_RIGHT_SECTION
            elif (self.w_offset + self.bw >= self.bf):
                #this is still an L section with flange protruding to the left
                return SectionCoordinates.L_LEFT_SECTION
            else:
                return SectionCoordinates.T_SECTION
                #L flanged section
            

    def setBf(self):
        bf = self.bf_top
        if (bf == 0.):
            bf = self.bf_bottom
        return bf

    def setName(self, name):
        self.name = name

    def setB(self, b):
        self.b = float(b)

    def setBfTop(self, bf_top):
        self.bf_top = float(bf_top)

    def setBfBottom(self, bf_bottom):
        self.bf_bottom = float(bf_bottom)

    def setBw(self, bw):
        self.bw = float(bw)

    def setD(self, d):
        self.d = float(d)

    def setDf(self, df):
        self.df = float(df)
    
    def setWOffset(self, w_offset):
        self.w_offset = float(w_offset)

    def getCoordinates(self, starting_point, beam_depth):
        return SectionCoordinates(starting_point, self, beam_depth)

    def toString(self):
        string = ""
        string +="\nb = " + str(self.b)
        string +="\nbf_top = " + str(self.bf_top)
        string +="\nbf_bottom = " + str(self.bf_bottom)
        string +="\nbw = " + str(self.bw)
        string +="\nd = " + str(self.d)
        string +="\ndf = " + str(self.df)
        string +="\nw_offset = " + str(self.w_offset)
        string +="\nbf = " + str(self.bf)
        string +="\nname = " + str(self.name)
        
        return string