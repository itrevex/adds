import ezdxf
import sys
sys.path.append("./common/")

from constants import Constants

from utils import Utils
from supports import Supports
from beams.beams import Beams
from coordinates.span_coord import SpanCoordinates

class Detailing:
    
    def __init__(self, app_data):
        self.dwg = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'
        self.msp = self.dwg.modelspace()  # add new entities to the model space
        self.app_data = app_data
        self.addLayersToModelSpace()
        self.setHeaderAttribs()
        # self.drawSupports()
        pass
    
    def makeDxf(self):
        name = self.getFileName()
        self.dwg.saveas('output\%s'%name)
        print (name + " generated ...")

    def getFileName(self):
        return Utils.dateTimeString() +"-detail.dxf"

    def drawLine(self, pt1, pt2, layer = '0'):
        # add a LINE entity
        self.msp.add_line(pt1, pt2, dxfattribs={'layer': layer})  

    def drawLineObject(self, lineObject):
        pt1 = lineObject.pt1
        pt2 = lineObject.pt2
        layer = lineObject.layer
        self.drawLine(pt1, pt2, layer)

    def drawSupports(self):
        support_entities = Supports(self.app_data).getSupportEntites()
        for entity in support_entities:
           self.drawLineObject(entity)
            

        												
    def availableLineTypes(self):
        # iteration
        print('available line types:')
        for linetype in self.dwg.linetypes:
            print('{}: {}'.format(linetype.dxf.name, linetype.dxf.description))

    def printLayers(self):
        print(self.app_data.getLayers())


    def getLayerAttributes(self, layer):
        
        name = layer[Constants.LAYER_NAME]
        lineType = layer[Constants.LAYER_LINE_TYPE]
        color = layer[Constants.LAYER_COLOR]

        layerAttributes = { Constants.LAYER_LINE_TYPE: lineType,
            Constants.LAYER_COLOR: color}

        return name, layerAttributes

    def addLayersToModelSpace(self):
        layers = self.app_data.getLayers()
        for layer in layers.values():
            name, attribs = self.getLayerAttributes(layer)
            self.dwg.layers.new(name=name, dxfattribs=attribs)

    def setHeaderAttribs(self):
        headerAttribs = self.app_data.getHeaderAttribs()
        for attrib in headerAttribs.values():
            attribName = attrib[Constants.HEADER_ATTRIB_NAME]
            attribValue = attrib[Constants.HEADER_ATTRIB_VALUE]
            self.dwg.header.__setitem__(attribName, attribValue)

    def drawEntities(self, entities):
        if (entities == None):
            return

        for entity in entities:
            self.drawLineObject(entity)

    def trials(self):
        beams_data = Beams(self.app_data.getInputData())
        beams = beams_data.getBeams()
        sections = beams_data.getSections()
        support_types = beams_data.getSupportTypes()

        entry_point = (0,0,0)
        starting_point = list(entry_point)
        for beam_name, beam in beams.items():
            beam_supports = list(beam.supports.values())
            total_spans = len(beam.spans)
            total_span_length = 0.
            beam_start_point = tuple(starting_point)
            columns_widths = []
            print("")
            print(beam_name)
            
            for span in beam.spans.values():
                
                span_lines = []
                total_span_length += span.span_length
                span_coords = SpanCoordinates(starting_point,span.span_length, 
                    beam.beam_depth)

                Detailing.loadEndColumnWidth(span, support_types, beam_supports, 
                    total_spans, columns_widths)

                column_lines = Detailing.getColumnLines(support_types, beam_supports, 
                    span, span_coords, total_spans)

                span_lines.extend(column_lines)

                if span.index == total_spans - 1:
                    beam_lines = span_coords.getBeamLines(beam_start_point,
                        total_span_length, columns_widths)

                    span_lines.extend(beam_lines)

                section_lines = Detailing.getSectionLines(sections, span,support_types, 
                    beam_supports, span_coords)

                span_lines.extend(section_lines)  
                # span_lines.append(span_coords.getSpanLine())

                #draw left section
                

                

                #can draw out section but this will be for later when showing
                #section details
                #section = sections[span.section_left]
                # self.drawSectionEntities(span_coords.end_point, beam, section)

                self.drawEntities(span_lines)
                starting_point = list(span_coords.end_point)

            starting_point[1] -= 3500
            starting_point[0] = entry_point[0]

        self.makeDxf()

    @staticmethod
    def getSectionLines(sections, span,support_types, beam_supports, span_coords):
        left_section = sections[span.section_left]
        right_section = sections[span.section_right]

        column_widths = Detailing.spanColumnWidths(span, 
            support_types, beam_supports)

        return span_coords.getSectionLines(column_widths, 
            left_section, right_section)

    @staticmethod
    def loadEndColumnWidth(span, support_types, beam_supports, 
        total_spans, columns_widths):
        if (span.index == 0):
            start_column_widths = Detailing.getEndColumnWidth(support_types, 
                beam_supports, span.index)
            columns_widths.extend(start_column_widths)

        if span.index == total_spans - 1:
            end_column_widths = Detailing.getEndColumnWidth(support_types, 
                beam_supports, total_spans)
            columns_widths.extend(end_column_widths)
    @staticmethod
    def spanColumnWidths(span, support_types, beam_supports):
        columns_widths = []
        start_column_widths = Detailing.getEndColumnWidth(support_types, 
                beam_supports, span.index)
        columns_widths.extend(start_column_widths)
            
        end_column_widths = Detailing.getEndColumnWidth(support_types, 
                beam_supports, span.index + 1)
        columns_widths.extend(end_column_widths)

        return columns_widths
            
    
    @staticmethod
    def getSupportLines(support_types, support, span_coords, left_column = True):
        '''
        support could be support left or support right

        layer = supports
        '''

        column_top_width = support_types[support].getColumnTopWidth()
        column_bottom_width = support_types[support].getColumnBottomWidth()

        
        return span_coords.getColumnLines(column_top_width, 
            column_bottom_width, left_column)

    @staticmethod
    def getEndColumnWidth(support_types, beam_supports, index):
        left_support = beam_supports[index]
        column_top_width = support_types[left_support].getColumnTopWidth()
        column_bottom_width = support_types[left_support].getColumnBottomWidth()

        if column_top_width == 0.:
                column_top_width = column_bottom_width
        
        if column_bottom_width == 0.:
            column_bottom_width = column_top_width

        return [column_top_width, column_bottom_width]

    @staticmethod
    def getColumnLines(support_types, beam_supports, span, 
        span_coords, total_spans):
        support_lines = []
        left_support = beam_supports[span.index]
        column_lines = Detailing.getSupportLines(support_types,
            left_support, span_coords)

        support_lines.extend(column_lines)
        # do I need the right support, yes; if it is the last span
        
        if (span.index == total_spans - 1):
            right_support = beam_supports[span.index + 1]
            column_lines = Detailing.getSupportLines(support_types,
            right_support, span_coords, False)

            support_lines.extend(column_lines)

        return support_lines

    def drawSectionEntities(self, starting_point, beam, section):
        sec_coords = section.getCoordinates(starting_point,beam.beam_depth)
        entities = sec_coords.getEntities()
        self.drawEntities(entities)
            




