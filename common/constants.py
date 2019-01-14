class Constants:

    def __init__(self):
        pass
    # coordinate identifiers inside list for a single point in drawing space
    X = 0
    Y = 1
    Z = 2

    # scaling factors
    COLUMN_LINE_FACTOR = 1.2
    CENTER_LINE_FACTOR = 1.75 
    SCALE_FACTOR_COLUMNS = 1.

    #starting point
    START_POINT = (0.,0.,0.) #tupple becomes by list(START_POINT)

    #Layers
    LAYER_CENTER_LINES = "CenterLines"
    LAYER_BEAM_LINES = "BeamLines"
    LAYER_SUPPORT_LINES = "SupportLines"
    LAYER_ZIGZAG_LINES = "Zigzag"

    #Layer keys
    LAYER_NAME = "layername"
    LAYER_COLOR = "color"
    LAYER_LINE_TYPE = "linetype"

    #Header Attributes
    HEADER_ATTRIB_NAME = "attrib_name"
    HEADER_ATTRIB_VALUE = "attrib_value"

    #Support constants
    CENTRE_LINE = "centre_line"
    SUPPORT_START = "start"
    SUPPORT_MID = "mid"
    SUPPORT_END = "end"

    #Input Data
    SUPPORTS = "supports" 
    COLUMN_SECION_WIDTH = "column_section_widths"
    COLUMN_CENTRE_CENTRE_LENGTHS = "column_centre_to_centre_lengths"
    BEAM_DEPTH = "beam_depth"
    STARTING_POINT = "starting_point"