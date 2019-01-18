class Section:
    L_RIGHT_SECTION = "l_right_section"
    L_LEFT_SECTION = "l_left_section"
    T_SECTION = "t_section"
    SQUARE_SECTION = "square_section"

    SECTIONS_B = "b" #b - total width of section
    SECTIONS_BF_TOP = "bf_top" #bf_top - width  of flange on top
    SECTIONS_BF_BOTTOM = "bf_bottom" #bf_bottom - width of flange at the bottom
    SECTIONS_BW = "bw" #bw - width of web
    SECTIONS_D = "d" #d - total depth of section
    SECTIONS_DF = "df" #df - depth of flange
    SECTIONS_W_OFFSET = "w_offset" #w_offset - off set of web from left starting point of section

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

    
    def __init__(self, name, props):
        self.b = self.updateProp(props, Section.SECTIONS_B)
        self.bf_top = self.updateProp(props, Section.SECTIONS_BF_TOP)
        self.bf_bottom = self.updateProp(props, Section.SECTIONS_BF_BOTTOM)
        self.bw = self.updateProp(props, Section.SECTIONS_BW)
        self.d = self.updateProp(props, Section.SECTIONS_D)
        self.df = self.updateProp(props, Section.SECTIONS_DF)
        self.w_offset = self.updateProp(props, Section.SECTIONS_W_OFFSET)
        self.bf = self.setBf()
        self.name = name

        #method has to be called after initializing other parameters
        self.type = self.getSectionType()

    def updateProp(self, props, key):
        try:
            if(props[key] == ""):
                return 0.
            return float(props[key])
        except KeyError:
            return 0.

    def getSectionType(self):
        # 3 section type
        # T, L and square
        if (self.df == 0.):
            #this is a square section, it has no flange depth
            return Section.SQUARE_SECTION
        else:
            if (self.w_offset == 0.):
                #this is an L section with flange protruding to the right
                return Section.L_RIGHT_SECTION
            elif (self.w_offset + self.bw >= self.bf):
                #this is still an L section with flange protruding to the left
                return Section.L_LEFT_SECTION
            else:
                return Section.T_SECTION
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

    def getVertices(self, starting_point):

        pass

