import sys
sys.path.append("./common/")
from constants import Constants

class EntityLine:
    '''
    Line entity base class
    it is initialized with pt1(x,y,z), pt2(x,y,z)
    and the layer on which the point is sitting
    '''
    ENTITY_LINE = "entity_line"

    X = 0
    Y = 1
    Z = 2
    
    def __init__(self, pt1, pt2, layer):

        self.pt1 = pt1
        self.pt2 = pt2
        self.layer = layer
        self.type = Constants.ENTITY_LINE

    def setPt1(self, pt):
        self.pt1 = pt

    def setPt2(self, pt):
        self.pt2 = pt

    def setPt1(self, layer):
        self.layer = layer

