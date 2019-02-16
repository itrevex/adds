import re
from .beam import Beam
from .span import Span
from .column import Column
from .support_type import SupportType
from .section import Section
from .link_type import LinkType
from common.messages import Messages
from common.constants import Constants
from common.message_codes import MessageCodes

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
        self.build = self.getBuildNumber()
        self.starting_point = self.getStartingPoint()

        self.checkBuild()

    def getStartingPoint(self):
        i = 0
        start_point = (0.,0.,0.)
        while i < len(self.app_data[i]):
            if re.search("^(?=^START)(?=.*\\bPOINT\\b).*$", self.app_data[i]):
                line = list(filter(None, self.app_data[i].split(" ")))
                start_point = tuple([float(x) for x in line[-3:]])
                self.app_data.pop(i)
                return start_point
            i += 1
        

    def checkBuild(self):
        if self.build > Constants.CURRENT_BUILD:
            Messages.showError(MessageCodes.ERROR_LATER_VERSION)
        elif self.build < Constants.CURRENT_BUILD:            
            Messages.showWarning(MessageCodes.WARNING_EARLIER_VERSION)
        else:
            #build number and file being run are compatible
            pass

    def getBuildNumber(self):
        i = 0
        while i < len(self.app_data[i]):
            if re.search("^\\bBUILD\\b", self.app_data[i]):
                line = list(filter(None, self.app_data[i].split(" ")))
                build_number = int(line[1])
                self.app_data.pop(i)
                break
            i += 1
        return build_number

    def getBeams(self):
        beams = {}
        beams_raw_data = self.app_data[Beams.BEAMS]
        
        for beam_name, beam_raw_data in beams_raw_data.items():
            Messages.i(MessageCodes.INFO_DATA_READ%beam_name)
            beam_depth = beam_raw_data[Beams.BEAM_DEPTH]
            supports, grid_labels = self.getBeamSupports(beam_raw_data[Beams.SUPPORTS])
            spans = self.getBeamSpans(beam_raw_data[Beams.SPANS], beam_name)

            beams[beam_name] = Beam(beam_depth, spans, supports, grid_labels, beam_name)

        return beams

    def getBeamSpans(self, spans_raw_data, beam_name):
        spans = {}
        counter = 0
        for span_name, span_raw_data in spans_raw_data.items():
            spans[span_name] = Span(span_name, span_raw_data, beam_name, self.build, counter)
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
        i = 0
        while i < len(self.app_data):
            store = False
            if re.search("^SECTIONS", self.app_data[i]):
                i+=1
                store = True
            while store:
                if re.search("^END SECTION", self.app_data[i]):
                    self.app_data.pop(i)
                    store = False #break out of inner loop
                elif re.search("^\\bSECTION\\b", self.app_data[i]):
                    section = list(filter(None, self.app_data[i].split(" ")))
                    sections[section[Section.SECTION_NAME]] = Section(section)
                    self.app_data.pop(i)
                i += 1
            i += 1

        
        # for name, props in self.app_data[Beams.SECTIONS].items():
        #     Messages.i(MessageCodes.INFO_DATA_READ%name)
        #     sections[name] = Section(name, props)

        return sections

    def getLinks(self):
        link_types = {}
        if self.build > 1000:
            for name, props in self.app_data[Beams.LINK_TYPES].items():
                Messages.i(MessageCodes.INFO_DATA_READ%name)
                link_types[name] = LinkType(name, props)

        return link_types

    def getSupportTypes(self):
        support_types = {}
        for name, props in self.app_data[Beams.SUPPORT_TYPES].items():
            Messages.i(MessageCodes.INFO_DATA_READ%name)
            column_top = self.getColumn(props, Beams.COLUMN_TOP)
            column_bottom = self.getColumn(props, Beams.COLUMN_BOTTOM)
            support_types[name] = SupportType(column_top, column_bottom)

        return support_types

    def getColumn(self, props, key):
        try:
            return Column(key, props[key])
        except KeyError:
            return None


    