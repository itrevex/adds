class SupportProps:
    '''
    for on condition check the support line class
    '''
    def __init__(self, beam_depth, layer, mulltiplication_factor, 
        starting_point = None, condition = "", column_section_width = "0"):
        self.starting_point = starting_point
        self.beam_depth = beam_depth
        self.layer = layer 
        self.column_section_width = column_section_width
        self.mulltiplication_factor = mulltiplication_factor
        self.condition = condition

    def setStartingPoint(self, starting_point):
        self.starting_point = starting_point

    def setBeamDepth(self, beam_depth):
        self.beam_depth = beam_depth

    def setLayer(self, layer):
        self.layer = layer

    def setMultiplicaionFactor(self, mulltiplication_factor):
        self.mulltiplication_factor = mulltiplication_factor

    def setCondition(self, condition):
        self.condition = condition

    def setColumnSectionWidth(self, column_section_width):
        self.column_section_width = column_section_width