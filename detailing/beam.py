class Beam:
    STARTING_POINT = "starting_point"
    BEAM_DEPTH = "beam_depth"
    COLUMN_SECTION_WIDTH = "column_section_width"
    SUPPORT_LOCATION = "support_location"

    def __init__(self, beam_parameters):
        self.support_location = beam_parameters[SUPPORT_LOCATION]
        self.starting_point = beam_parameters[STARTING_POINT]
        self.beam_depth = beam_parameters[BEAM_DEPTH]
        self.column_section_width = beam_parameters[COLUMN_SECTION_WIDTH]

    def setStartingPoint(self, starting_point):
        self.starting_point = starting_point

    def setBeamDepth(self, beam_depth):
        self.beam_depth = beam_depth

    def setColumnSectionWidth(self, column_section_width):
        self.column_section_width = column_section_width

    def setSupportLocation(self, support_location):
        self.support_location = support_location