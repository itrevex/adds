class Span:
    '''
    defines span with the span centre to centre length as span_length
    in m
    The section on the left of the span and the section on the right of the span
    '''

        #SPANS
    SPAN_LENGTH = "length_m"
    SPAN_SECTION_LEFT = "section_left"
    SPAN_SECTION_RIGHT = "section_right"

    def __init__(self, name, props):
        self.name = name
        self.span_length = props[Span.SPAN_LENGTH]
        self.section_left = props[Span.SPAN_SECTION_LEFT]
        self.section_right = props[Span.SPAN_SECTION_RIGHT]

    def setSpanLength(self, span_length):
        self.span_length = span_length

    def setSectionLeft(self, section_left):
        self.section_left = section_left

    def setSectionRight(self, section_right):
        self.section_right = section_right

    def setName(self, name):
        self.name = name