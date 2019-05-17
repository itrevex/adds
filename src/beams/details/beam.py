from .span import SpanDetails
from dxf.dxf_entities.entity_hatch import EntityHatch
from dxf.dxf_entities.entity_line import EntityLine
from common.messages import Messages
from common.message_codes import MessageCodes

class BeamDetails:
        def __init__(self, all_beams_data, beam_name, beam_data, start_point):
            Messages.i("") #add space at start of each beam info output
            self.all_beams_data = all_beams_data
            self.data = beam_data
            self.name = beam_name
            self.beam_supports = list(beam_data.supports.values()) #
            self.beam_grid_labels = list(beam_data.grid_labels.values())
            self.total_spans = len(beam_data.spans) #
            self.total_span_length = 0.
            self.starting_point = tuple(start_point)
            self.columns_widths = []
            self.beam_entities = []
            self.lines = []
            self.all_spans = {}
            # check deepest section against beam depth before getting span details
            self.checkBeamDepth()
            self.getSpanDetails()

        def checkBeamDepth(self):
            deepest_section_depth = 0
            for section in self.data.sections:
                deepest_section_depth = self.getDeepestSection(section, deepest_section_depth)

            if self.data.beam_depth < deepest_section_depth:
                self.data.beam_depth = deepest_section_depth
                Messages.w(MessageCodes.WARNING_BEAM_DEPTH_ALTERED)
            

        def getDeepestSection(self, section, deepest_section_depth):
            '''
            Method to get deepest section. If the deepest section is less
            than the beam depth the the beam depth has to be adjusted to the deepest 
            section
            '''
            new_section_depth  = self.all_beams_data.sections[section].d

            if new_section_depth > deepest_section_depth:
                deepest_section_depth = new_section_depth

            return deepest_section_depth
            
        def getSpanDetails(self):
            span_starting_point = self.starting_point
            for span_name, span_data in self.data.spans.items():
                span = SpanDetails(self, span_name, span_data, span_starting_point)
                self.all_spans[span_name] = span
                #End of current span is start point of next span
                span_starting_point = list(span.span_coords.end_point)

        def getBeamEntities(self):
            '''
            add each spans entities and the beam lines
            '''
            beam_entities = []
            span_entities = []
            bottom_pts_2 = []
            top_pts_5 = []
            for span in self.all_spans.values():
                span_entities.extend(span.getSpanEntities())
                coords = span.hatch_coords
                bottom_pts_2.extend(coords.getBottomList())
                top_pts_5.extend(coords.getTopList())
                
            hatch_path = self.getHatchPath(bottom_pts_2, top_pts_5)
            
            beam_entities.append(EntityHatch(hatch_path))
            beam_entities.extend(span_entities)
            beam_entities.extend(self.lines)
            return beam_entities
            
        def getHatchPath(self, bottom_pts_2, top_pts_5):
            '''
            1. add left beam line bottom point: pt_1
            2. add bottom span lines: bottom_pts_2
            3. add right beam line bottom point: pt_3
            4. add right beam line bottom point: pt_4
            5. add top span lines: top_pts_5
            6. add left beam line top point: pt_6
            '''
            hatch_path = []
            pt_1 = self.lines[2].pt2
            pt_3 = self.lines[3].pt2
            pt_4 = self.lines[3].pt1
            pt_6 = self.lines[2].pt1

            hatch_path.append(pt_1)
            hatch_path.extend(bottom_pts_2)
            hatch_path.append(pt_3)
            hatch_path.append(pt_4)
            hatch_path.extend(top_pts_5)
            hatch_path.append(pt_6)

            return hatch_path
            
        def sortPoints(self, pts):
            '''
            Sorting points from left bottom corner
            Meaning left most -x comes before bottom most point
            But points sharing a similar x will be sorted according to y 
            '''

            x_sorted = self.insertionSort(list(pts), EntityLine.X)
            return self.levelTwoSort(x_sorted, EntityLine.X, EntityLine.Y)

        def insertionSort(self, pts, pt_index, simulation=False):
            for i, pt in enumerate(pts):
                cursor = pt[pt_index]
                pos = i
                
                while pos > 0 and pts[pos - 1][pt_index] > cursor:
                    # Swap the number down the list
                    pts[pos] = pts[pos - 1]
                    pos = pos - 1
                # Break and do the final swap
                pts[pos] = pt

            return pts

        def levelTwoSort(self, pts, sorted_index, to_sort_index):
            '''
            Sorts Y values where x values are similar
            '''
            last_pos = -1 #there is no last position at the start
            for i, pt in enumerate(pts):
                cursor = pt[sorted_index]
                pos = i
                if (pos < last_pos):
                    pos = last_pos

                pts_similar_x = [pt]
                while pos < len(pts) - 1 and pts[pos+1][sorted_index] == cursor:
                    pts_similar_x.append(pts[pos+1])
                    pos += 1
                    last_pos = pos + 1
                    pass

                if len(pts_similar_x) > 1:
                    #sort this sub list
                    pts[i:last_pos] = self.insertionSort(pts_similar_x, to_sort_index)
            
            return pts