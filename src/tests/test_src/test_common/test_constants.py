from common.constants import Constants

class TestConstants():
    def test_constants(self):
        constants = Constants()

        # coordinate identifiers inside list for a single point in drawing space
        assert constants.X == 0
        assert constants.Y == 1
        assert constants.Z == 2

        #Build and app version
        assert constants.CURRENT_BUILD == 1002
        assert constants.APP_VERSION == "1.0.1"

        #Text factors
        # GRID_LABEL_STYLE == "GridLabels"
        assert constants.GRID_LABEL_STYLE == "GridLabels"
        assert constants.GRID_TEXT_HEIGHT == 111.25
        assert constants.LINK_LABEL_TEXT_HEIGHT == 50.75
        assert constants.CHARACTER_LENGTH_FACTOR == 0.9659 #calculated for romans.ttf


        # scaling factors
        assert constants.COLUMN_LINE_FACTOR == 1.2
        assert constants.CENTER_LINE_FACTOR == 1.75 
        assert constants.CENTER_LINE_FACTOR_TOP == 2.5
        assert constants.SCALE_FACTOR_COLUMNS == 1.
        assert constants.CIRCLE_TEXT_OFFSET_FACTOR == 0.3333

        #ZIGZAG AS FACTORS OF THE COLUMN WIDTH
        assert constants.Z_OUTER_SEGMENT == 0.15
        assert constants.Z_INNER_SEGMENT == 0.3125
        assert constants.Z_TIP_DEPTH == 0.2576
        assert constants.Z_TIP_LENGTH == 0.40625

        #GRID CIRCLE FACTORS
        assert constants.GRID_CIRCLE_RADIUS == 150.0
        assert constants.GRID_CIRCLE_FACTOR == 1.0

        #starting point
        assert constants.STARTING_POINT == "starting_point"
        assert constants.START_POINT == (0.,0.,0.) #tupple becomes by list(START_POINT)

        #Layers
        assert constants.LAYER_CENTER_LINES == "CenterLines"
        assert constants.LAYER_BEAM_LINES == "BeamLines"
        assert constants.LAYER_SUPPORT_LINES == "SupportLines"
        assert constants.LAYER_ZIGZAG_LINES == "Zigzag"
        assert constants.LAYER_GRID_LINES == "GridLines"
        assert constants.LAYER_GRID_LABELS == "GridLabels"
        assert constants.LAYER_BEAM_HATCHES == "BeamHatches"
        assert constants.LAYER_SECTION_LINES == "SectionLines"
        assert constants.LAYER_DIMENSIONS == "Dimensions"
        assert constants.LAYER_SHEAR_LINKS == "ShearLinks"

        #Layer keys
        assert constants.LAYER_NAME == "layername"
        assert constants.LAYER_COLOR == "color"
        assert constants.LAYER_LINE_TYPE == "linetype"

        #Header Attributes
        assert constants.HEADER_ATTRIB_NAME == "attrib_name"
        assert constants.HEADER_ATTRIB_VALUE == "attrib_value"

        #Support constants
        assert constants.CENTRE_LINE == "centre_line"
        assert constants.SUPPORT_START == "start"
        assert constants.SUPPORT_MID == "mid"
        assert constants.SUPPORT_END == "end"

        #Input Data
        assert constants.COLUMN_SECION_WIDTH == "column_section_widths"
        assert constants.COLUMN_CENTRE_CENTRE_LENGTHS == "column_centre_to_centre_lengths"

        #BEAMS
        assert constants.SUPPORTS == "supports" 
        assert constants.BEAM_DEPTH == "beam_depth"

        #Entities
        assert constants.ENTITY_CIRCLE == "entity_circle"
        assert constants.ENTITY_LINE == "entity_line"
        assert constants.ENTITY_TEXT == "entity_text"
        assert constants.ENTITY_HATCH == "entity_hatch"
        assert constants.ENTITY_DIMENSION == "entity_dimension"

        #LINKS DATA
        assert constants.LINKS_DEFAULT_OFFSET == 0.05 #default offset is in m
        assert constants.LINKS_CUT_OFF_FROM_EDGE_OF_BEAM_LINE == 20 # links offset from edge of beam in mm
        assert constants.LINK_TEXT == "LINKS"

        #DIMENSIONING CONSTANTS
        assert constants.SHEAR_DIM_BOTTOM_OFFSET == 120