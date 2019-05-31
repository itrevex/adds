from src.common.constants import Constants

class EntityDimension:
    def __init__(self, dim_points):
        pass
        self.points = dim_points
        self.dim_style =""
        self.angle = 0.
        self.text = ""
        self.starting_point = self.points[0]
        self.type = Constants.ENTITY_DIMENSION 
        self.layer = Constants.LAYER_DIMENSIONS 