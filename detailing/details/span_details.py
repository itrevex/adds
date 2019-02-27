import copy

from common.messages import Messages
from common.message_codes import MessageCodes
from detailing.coordinates.span_coord import SpanCoordinates
from detailing.coordinates.shear_coords import ShearCoords
from detailing.dxf_entities.entity_dimension import EntityDimension
from detailing.coordinates.span_points import SpanPoints

class SpanDetails: 
        '''
        Class for calculating column lines, section_lines and beam_lines
        beam lines are stored on the beam object
        '''
        def __init__(self, beam, span_name, span_data, start_point):

            Messages.i(MessageCodes.INFO_CREATING_ENTITY%(beam.name, span_name))
            self.span_lines = []
            self.beam = beam
            self.data = span_data #Span input data object
            self.name = span_name
            self.starting_point = tuple(start_point)
            self.beam.total_span_length += span_data.span_length
            self.span_coords = self.getSpanCoords()
            self.addColumnWidths()
            self.shear_links = copy.deepcopy(self.beam.all_beams_data.shear_links)
            self.column_lines = self.getColumnLines()
            self.section_lines, self.hatch_coords = self.getSectionLines()
            self.beam.lines = self.getBeamLines()
  
        def getSpanEntities(self):
            span_entities = []
            span_entities.extend(self.column_lines)
            span_entities.extend(self.section_lines)
            span_entities.extend(self.getShearData().getEntitiesList())     
            
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

            Column lines include the the lines to indicate the columns,
            the centre lines and other properties that may be on those items

            '''

            support_lines = []
            #dimension points pool for each section
            dim_points = []
            #support at index as indicated in the input data. This on gives
            #the support name, the support data will got from support_types
            #present on all beams data pool
            left_support = self.beam.beam_supports[self.data.index]
            grid_label = ""
            if len(self.beam.beam_grid_labels) != 0:     
                grid_label = self.beam.beam_grid_labels[self.data.index]

            column_lines, dim_point = self.getSupportLines(left_support, grid_label)
            
            dim_points.append(dim_point)
            support_lines.extend(column_lines)
            # do I need the right support, yes; if it is the last span
            
            if (self.data.index == self.beam.total_spans - 1):
                #the very last support is got with last span index + 1
                right_support = self.beam.beam_supports[self.data.index + 1]

                # if self.beam.beam_grid_labels != []:
                grid_label = ""
                if len(self.beam.beam_grid_labels) != 0:     
                    grid_label = self.beam.beam_grid_labels[self.data.index + 1]

                column_lines, dim_point = self.getSupportLines(right_support, grid_label, False)
                dim_points.append(dim_point)
                dim = EntityDimension(dim_points)
                #create dim entity and add it to column_lines

                support_lines.extend(column_lines)
                support_lines.append(dim)

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
                support_index = self.beam.beam_supports[index] #could be left or right support
                support = support_types[support_index]
                
                column_top_width = support.column_top.b
                column_bottom_width = support.column_bottom.b

                if column_top_width == 0.:
                    column_top_width = column_bottom_width
                
                if column_bottom_width == 0.:
                    column_bottom_width = column_top_width

                return [column_top_width, column_bottom_width]

            except IndexError:
                message = MessageCodes.ERROR_WRONG_NO_SUPPORTS
                message.setMsg(message.msg%(self.name, self.beam.name))         
                Messages.showError(message)

        def getShearData(self):
             #column left bigger width, data==span
            left_column_width = max(self.getColumnWidth(self.data.index))

             #column right bigger width,
            right_column_width = max(self.getColumnWidth(self.data.index + 1))

            #check multiple links for lengths
            self.setLinkLengths(left_column_width, right_column_width)

            shear_coord = ShearCoords(self, left_column_width, right_column_width) 

            return shear_coord

        def setLinkLengths(self, left_column_width, right_column_width):
            '''
            Checks multiple links, incase there are multiple links and no lengths
            provided for some of these, this routine is responsible for assigning
            lengths to links without lengths
            '''

            calculate_lengths, total_offset, total_none_length_links = self.calculateLengths()
            total_offset += (left_column_width/2 + right_column_width/2) / SpanPoints.ONE_M_IN_MM

            if calculate_lengths:
                shear_length = (self.data.span_length - total_offset) /total_none_length_links
                for link in self.data.links:
                    link_type = self.shear_links[link]
                    if link_type.length == None:
                        link_type.setLength(shear_length)
                
        def calculateLengths(self):
            calculate_lengths = False
            total_offset = 0.
            total_none_length_links = 0
            for i, link in enumerate(self.data.links):
                link_type = self.shear_links[link]
                total_offset += link_type.offset
                if link_type.length == None:
                    total_none_length_links += 1
                    calculate_lengths = True
                else:
                    total_offset += link_type.length

                #final link
                if i == len(self.data.links) - 1:
                    total_offset += link_type.offset 

            return calculate_lengths, total_offset, total_none_length_links

        def getSupportLines(self, support, grid_label, left_column = True):
            '''
            support could be support left or support right
            support is the support name and it is stored in the beams data

            layer = supports
            '''
            support_type = self.beam.all_beams_data.support_types[support]

            return self.span_coords.getColumnLines(support_type, grid_label, left_column)
 