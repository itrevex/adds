from .span_details import SpanDetails

class BeamDetails:
        def __init__(self, all_beams_data, beam_name, beam_data, start_point):
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
            self.getSpanDetails()
            

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
            beam_entities.extend(self.lines)
            for span in self.all_spans.values():
                beam_entities.extend(span.getSpanEntities())

            return beam_entities

    