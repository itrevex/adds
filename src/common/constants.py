class Constants:

    # coordinate identifiers inside list for a single point in drawing space
    X = 0
    Y = 1
    Z = 2

    #Build and app version
    CURRENT_BUILD = 1002
    APP_VERSION = "1.0.1"

    #Text factors
    # GRID_LABEL_STYLE = "GridLabels"
    GRID_LABEL_STYLE = "GridLabels"
    GRID_TEXT_HEIGHT = 111.25
    LINK_LABEL_TEXT_HEIGHT = 50.75
    CHARACTER_LENGTH_FACTOR = 0.9659 #calculated for romans.ttf


    # scaling factors
    COLUMN_LINE_FACTOR = 1.2
    CENTER_LINE_FACTOR = 1.75 
    CENTER_LINE_FACTOR_TOP = 2.5
    SCALE_FACTOR_COLUMNS = 1.
    CIRCLE_TEXT_OFFSET_FACTOR = 0.3333

    #ZIGZAG AS FACTORS OF THE COLUMN WIDTH
    Z_OUTER_SEGMENT = 0.15
    Z_INNER_SEGMENT = 0.3125
    Z_TIP_DEPTH = 0.2576
    Z_TIP_LENGTH = 0.40625

    #GRID CIRCLE FACTORS
    GRID_CIRCLE_RADIUS = 150.0
    GRID_CIRCLE_FACTOR = 1.0

    #starting point
    STARTING_POINT = "starting_point"
    START_POINT = (0.,0.,0.) #tupple becomes by list(START_POINT)

    #Layers
    LAYER_CENTER_LINES = "CenterLines"
    LAYER_BEAM_LINES = "BeamLines"
    LAYER_SUPPORT_LINES = "SupportLines"
    LAYER_ZIGZAG_LINES = "Zigzag"
    LAYER_GRID_LINES = "GridLines"
    LAYER_GRID_LABELS = "GridLabels"
    LAYER_BEAM_HATCHES = "BeamHatches"
    LAYER_SECTION_LINES = "SectionLines"
    LAYER_DIMENSIONS = "Dimensions"
    LAYER_SHEAR_LINKS = "ShearLinks"

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
    COLUMN_SECION_WIDTH = "column_section_widths"
    COLUMN_CENTRE_CENTRE_LENGTHS = "column_centre_to_centre_lengths"

    #BEAMS
    SUPPORTS = "supports" 
    BEAM_DEPTH = "beam_depth"

    #Entities
    ENTITY_CIRCLE = "entity_circle"
    ENTITY_LINE = "entity_line"
    ENTITY_TEXT = "entity_text"
    ENTITY_HATCH = "entity_hatch"
    ENTITY_DIMENSION = "entity_dimension"

    #LINKS DATA
    LINKS_DEFAULT_OFFSET = 0.05 #default offset is in m
    LINKS_CUT_OFF_FROM_EDGE_OF_BEAM_LINE = 20 # links offset from edge of beam in mm
    LINK_TEXT = "LINKS"

    #DIMENSIONING CONSTANTS
    SHEAR_DIM_BOTTOM_OFFSET = 120