class Beam:
    '''
    Beam has a beam depth, it has spans dictionary
    and a supports dictionary
    '''
    def __init__(self, beam_depth, spans, supports, name = ""):
        self.beam_depth = float(beam_depth)
        self.spans = spans
        self.supports = supports
        self.name = name
    

    def getSections(self):
        sections = set()
        for name, span in self.spans.items():
            sections.add(span.section_left)
            sections.add(span.section_right)
        
        print()
        print(self.name)
        print(sections)
        return sections

    def setBeamDepth(self, beam_depth):
        self.beam_depth = beam_depth

    def setSpans(self, beam_depth):
        self.spans = spans

    def setSupports(self, supports):
        self.supports = supports

    def setName(self, name):
        self.name =  name