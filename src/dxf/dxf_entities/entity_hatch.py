from common.constants import Constants

class EntityHatch:
    '''
    Hatch Entity
    has type, poly_line_point and layer
    '''
    
    def __init__(self, path = [], layer=Constants.LAYER_BEAM_HATCHES):

        self.path = path
        self.layer = layer
        self.type = Constants.ENTITY_HATCH

    def addPoint(self, pt):
        self.path.append = tuple(pt)

    def setPath(self, path):
        self.path = path

    def setLayer(self, layer):
        self.layer = layer

