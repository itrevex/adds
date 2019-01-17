class Beam:
    '''
    Beam has a beam depth, it has spans dictionary
    and a supports dictionary
    '''
    def __init__(self, beam_depth, spans, supports):
        self.beam_depth = beam_depth
        self.spans = spans
        self.supports = supports

    def setBeamDepth(self, beam_depth):
        self.beam_depth = beam_depth

    def setSpans(self, beam_depth):
        self.spans = spans

    def setSupports(self, supports):
        self.supports = supports