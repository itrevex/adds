import sys
sys.path.append("./common/")

from constants import Constants


class Section:
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

    
    def __init__(self, section_name, props):
        self.b = self.updateProp(props, Constants.SECTIONS_B)
        self.bf_top = self.updateProp(props, Constants.SECTIONS_BF_TOP)
        self.bf_bottom = self.updateProp(props, Constants.SECTIONS_BF_BOTTOM)
        self.bw = self.updateProp(props, Constants.SECTIONS_BW)
        self.d = self.updateProp(props, Constants.SECTIONS_D)
        self.df = self.updateProp(props, Constants.SECTIONS_D)
        self.w_offset = self.updateProp(props, Constants.SECTIONS_B)
        self.section_name = section_name

    def updateProp(self, props, key):
        try:
            if(props[key] == ""):
                return 0.
            return float(props[key])
        except KeyError:
            return 0.

    def setB(self, b):
        self.b = b

    def setBfTop(self, bf_top):
        self.bf_top = bf_top

    def setBfBottom(self, bf_bottom):
        self.bf_bottom = bf_bottom

    def setBw(self, bw):
        self.bw = bw

    def setD(self, d):
        self.d = d

    def setDf(self, df):
        self.df = df
    
    def setWOffset(self, w_offset):
        self.w_offset = w_offset

    def getBeamVertices(self, starting_point):
        '''
        starting_point is a tuple representing with
        x at the centre of the section and y at the bottom 
        of the beam (at beam depth = max_value or beam height = 0.)
        '''
        pass

