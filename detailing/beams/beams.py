from .beam import Beam
from .span import Span
from .column import Column
from .support_type import SupportType
from .section import Section

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

    def __init__(self, app_data):
        self.app_data = app_data

    def getBeams(self):
        beams = {}
        beams_raw_data = self.app_data[Beams.BEAMS]
        for beam_name, beam_raw_data in beams_raw_data.items():
            beam_depth = beam_raw_data[Beams.BEAM_DEPTH]
            spans = self.getBeamSpans(beam_raw_data[Beams.SPANS])
            supports = self.getBeamSupports(beam_raw_data[Beams.SUPPORTS])

            beams[beam_name] = Beam(beam_depth, spans, supports, beam_name)

        return beams

    def getBeamSpans(self, spans_raw_data):
        spans = {}
        for span_name, span_raw_data in spans_raw_data.items():
            spans[span_name] = Span(span_name, span_raw_data)

        return spans

    def getBeamSupports(self, supports_raw_data):
        supports = {}
        for support_name, support_type in supports_raw_data.items():
            supports[support_name] = support_type

        return supports

    def getSections(self):
        sections = {}
        for name, props in self.app_data[Beams.SECTIONS].items():
            sections[name] = Section(name, props)

        return sections

    def getSupportTypes(self):
        support_types = {}
        for name, props in self.app_data[Beams.SUPPORT_TYPES].items():
            column_top = self.getColumn(props, Beams.COLUMN_TOP)
            column_bottom = self.getColumn(props, Beams.COLUMN_BOTTOM)
            self.support_types[name] = SupportType(column_top, column_bottom)

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

    