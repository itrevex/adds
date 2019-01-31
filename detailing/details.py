from common.messages import Messages
from .beams.beams import Beams
from .coordinates.span_coord import SpanCoordinates

class AllBeamsDetails:

    def __init__(self, app_data):
        
        beams_data = Beams(app_data.getInputData())
        self.beams = beams_data.getBeams()
        self.sections = beams_data.getSections()
        self.support_types = beams_data.getSupportTypes()
        entry_point = (0,0,0)
        self.starting_point = list(entry_point)
        self.all_beams = {}
        self.getBeamDetails()
    
    def getBeamDetails(self):
        beam_start_point = list(self.starting_point)
        for beam_name, beam_data in self.beams.items():
            beam = self.BeamDetails(self, beam_name, beam_data, beam_start_point)
            self.all_beams[beam_name] = beam
            #draw next beam below current beam, change the y value 
            beam_start_point[1] -= 3500

    def getAllBeamsEntities(self):
        all_beams_entities = []
        for beam in self.all_beams.values():
            all_beams_entities.extend(beam.getBeamEntities())

        return all_beams_entities

    class BeamDetails:
        def __init__(self, all_beams_data, beam_name, beam_data, start_point):
            self.all_beams_data = all_beams_data
            self.data = beam_data
            self.name = beam_name
            self.beam_supports = list(beam_data.supports.values()) #
            self.total_spans = len(beam_data.spans) #
            self.total_span_length = 0.
            self.starting_point = tuple(start_point)
            self.columns_widths = []
            self.beam_entities = []
            self.lines = []
            self.all_spans = {}
            self.getSpanDetails()
            

        def getSpanDetails(self):
            span_starting_point = self.starting_point
            for span_name, span_data in self.data.spans.items():
                span = self.all_beams_data.SpanDetails(self, span_name, span_data, span_starting_point)
                self.all_spans[span_name] = span
                #End of current span is start point of next span
                span_starting_point = list(span.span_coords.end_point)

        def getBeamEntities(self):
            '''
            add each spans entities and the beam lines
            '''
            beam_entities = []
            beam_entities.extend(self.lines)
            for span in self.all_spans.values():
                beam_entities.extend(span.getSpanEntities())

            return beam_entities

    class SpanDetails:
        '''
        Class for calculating column lines, section_lines and beam_lines
        beam lines are stored on the beam object
        '''
        def __init__(self, beam, span_name, span_data, start_point):
            self.span_lines = []
            self.beam = beam
            self.data = span_data
            self.name = span_name
            self.starting_point = tuple(start_point)
            self.beam.total_span_length += span_data.span_length
            self.span_coords = self.getSpanCoords()
            self.addColumnWidths()
            self.column_lines = self.getColumnLines()
            self.section_lines = self.getSectionLines()
            self.beam.lines = self.getBeamLines()
        
        def getSpanEntities(self):
            span_entities = []
            span_entities.extend(self.column_lines)
            span_entities.extend(self.section_lines)
            return span_entities

        def getSectionLines(self):
            sections = self.beam.all_beams_data.sections

            left_section = sections[self.data.section_left]
            right_section = sections[self.data.section_right]

            column_widths = self.spanColumnWidths()

            return self.span_coords.getSectionLines(column_widths, 
                left_section, right_section)

        def spanColumnWidths(self):
            columns_widths = []
            start_column_widths = self.getColumnWidth(self.data.index)
            columns_widths.extend(start_column_widths)
                
            end_column_widths = self.getColumnWidth(self.data.index + 1)
            columns_widths.extend(end_column_widths)

            return columns_widths

        def getBeamLines(self):
            '''
            Only get beam lines when at the last support when all 
            column widths have been added to the column widths list

            Could be transfered to beam but uses span cordinates object 
            and therefore will be got inside beam
            '''

            if self.data.index == self.beam.total_spans - 1:
                return self.span_coords.getBeamLines(self.beam.starting_point,
                    self.beam.total_span_length, self.beam.columns_widths)

            return []

        def getColumnLines(self):
            '''
            self is the span object
            self.data gives the span input data
            '''

            support_lines = []
            left_support = self.beam.beam_supports[self.data.index]
            column_lines = self.getSupportLines(left_support)

            support_lines.extend(column_lines)
            # do I need the right support, yes; if it is the last span
            
            if (self.data.index == self.beam.total_spans - 1):
                right_support = self.beam.beam_supports[self.data.index + 1]
                column_lines = self.getSupportLines(right_support, False)

                support_lines.extend(column_lines)

            return support_lines

        def getSpanCoords(self):
            return SpanCoordinates(self.starting_point,
                self.data.span_length, self.beam.data.beam_depth)

        def addColumnWidths(self):
            '''
            Adds column widths to the beam column widths pool.
            These are used in getting beam and section lines coordinates
            '''
    
            if (self.data.index == 0):
                start_column_widths = self.getColumnWidth(self.data.index)
                self.beam.columns_widths.extend(start_column_widths)

            if self.data.index == self.beam.total_spans - 1:
                end_column_widths = self.getColumnWidth(self.beam.total_spans)
                self.beam.columns_widths.extend(end_column_widths)

        def getColumnWidth(self, index):
            '''
            Gets column width at the end of specified in span
            The end could be the left or right of the span
            '''
            try:
                support_types = self.beam.all_beams_data.support_types
                support = self.beam.beam_supports[index] #could be left or right support

                column_top_width = support_types[support].getColumnTopWidth()
                column_bottom_width = support_types[support].getColumnBottomWidth()

                if column_top_width == 0.:
                    column_top_width = column_bottom_width
                
                if column_bottom_width == 0.:
                    column_bottom_width = column_top_width

                return [column_top_width, column_bottom_width]

            except IndexError:
                message = "Please check number of supports provided for %s %s" %(self.name, self.beam.name)
                message += "\n\nThe number of supports should = spans + 1. Make sure the "
                message += "\nnumber of supports are 1 greater than the number of spans"

                Messages.showError(message)

        def getSupportLines(self, support, left_column = True):
            '''
            support could be support left or support right

            layer = supports
            '''
            support_type = self.beam.all_beams_data.support_types[support]
            column_top_width = support_type.getColumnTopWidth()
            column_bottom_width = support_type.getColumnBottomWidth()

            
            return self.span_coords.getColumnLines(column_top_width, 
                column_bottom_width, left_column)

    def drawSectionEntities(self, starting_point, beam, section):
        sec_coords = section.getCoordinates(starting_point,beam.beam_depth)
        entities = sec_coords.getEntities()
        self.drawEntities(entities)
            




