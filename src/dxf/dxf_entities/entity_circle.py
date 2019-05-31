from src.common.constants import Constants

class EntityCircle:
    '''
    Line entity base class
    it is initialized with pt1(x,y,z), pt2(x,y,z)
    and the layer on which the point is sitting
    '''
    
    X = 0
    Y = 1
    Z = 2
    
    def __init__(self, centre, radius, layer="0"):

        self.centre = tuple(centre)
        self.radius = float(radius)
        self.layer = layer
        self.type = Constants.ENTITY_CIRCLE

    def setCentre(self, centre):
        self.centre = centre

    def setRadius(self, radius):
        self.radius = radius

    def setLayer(self, layer):
        self.layer = layer

