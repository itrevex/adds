from .beam import Beam
from .span import Span
from .column import Column
from .support_type import SupportType
from .section import Section
from .link_type import LinkType
from common.messages import Messages

class Beams:
    '''
    Used to generate the beams,
    see beam for properties of each beam
    '''

    SUPPORT_TYPES = "supports_types"
    COLUMN_TOP = "column_top"
    COLUMN_BOTTOM = "column_bottom"

    BEAMS = "beams"
    BEAM_DEPTH = "beam_depth"
    SUPPORTS = "supports" 
    SPANS = "spans"
    SECTIONS = "sections"
    LINK_TYPES = "link_types"
    STARTING_POINT = "starting_point"
    BUILD = "build"

    def __init__(self, app_data):
        self.app_data = app_data
        self.starting_point = tuple(app_data[Beams.STARTING_POINT])
        self.getBuildNumber()

    def getBuildNumber(self):
        try:
            self.build = self.app_data[Beams.BUILD]
        except KeyError:
            self.build = 1000
        

    def getBeams(self):
        beams = {}
        beams_raw_data = self.app_data[Beams.BEAMS]
        for beam_name, beam_raw_data in beams_raw_data.items():
            beam_depth = beam_raw_data[Beams.BEAM_DEPTH]
            supports, grid_labels = self.getBeamSupports(beam_raw_data[Beams.SUPPORTS])
            spans = self.getBeamSpans(beam_raw_data[Beams.SPANS])

            beams[beam_name] = Beam(beam_depth, spans, supports, grid_labels, beam_name)

        return beams

    def getBeamSpans(self, spans_raw_data):
        spans = {}
        counter = 0
        for span_name, span_raw_data in spans_raw_data.items():
            spans[span_name] = Span(span_name, span_raw_data, counter)
            counter += 1

        return spans

    def getBeamSupports(self, supports_raw_data):
        supports = {}
        grids = {}
        for support_name, support_type in supports_raw_data.items():
            if self.build == 1000:
                supports[support_name] = support_type
            else:
                supports[support_name] = list(support_type)[0]
                grids[support_name] = list(support_type)[1]

        return supports, grids

    def getSections(self):
        sections = {}
        for name, props in self.app_data[Beams.SECTIONS].items():
            sections[name] = Section(name, props)

        return sections

    def getLinks(self):
        link_types = {}
        for name, props in self.app_data[Beams.LINK_TYPES].items():
            link_types[name] = LinkType(name, props)

        return link_types

    def getSupportTypes(self):
        support_types = {}
        for name, props in self.app_data[Beams.SUPPORT_TYPES].items():
            column_top = self.getColumn(props, Beams.COLUMN_TOP)
            column_bottom = self.getColumn(props, Beams.COLUMN_BOTTOM)
            support_types[name] = SupportType(column_top, column_bottom)

        return support_types

    def getColumn(self, props, key):
        try:
            return Column(key, props[key])
        except KeyError:
            return None

    def getStartingPoint(self):
        return tuple(self.app_data[Beams.STARTING_POINT])
    

    def getBeamsPlotObjects(self, starting_point):
        #go individual beams and get their plot objects
        # each beam has supports and spans
        # each support has centre_lines and column_lines
        # each span has span(beam) lines

        pass

    