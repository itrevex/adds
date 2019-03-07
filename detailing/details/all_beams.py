from detailing.beams_input.beams import Beams
from .beam_details import BeamDetails
from common.constants import Constants
from common.messages import Messages
from common.message_codes import MessageCodes

class AllBeamsDetails:
    def __init__(self, app_data):
        beams_data = Beams(app_data.readTradFile())
        self.beams = beams_data.getBeams()
        self.sections = beams_data.getSections()
        self.support_types = beams_data.getSupportTypes()
        self.shear_links = beams_data.getLinks()
        self.starting_point = list(beams_data.starting_point)
        self.build = beams_data.build
        self.all_beams = {}
        self.checkMissingBeamParameter()
        self.getBeamDetails()
        self.number_of_beams = len(self.beams)

    def checkMissingBeamParameter(self):
        # Messages.d(self.support_types.keys())
        for name, beam_data in self.beams.items():
            self.checkBeamSections(beam_data.spans, name)
            self.checkBeamLinks(beam_data.spans, name)
            self.checkBeamSupports(beam_data.supports, name)
            # Messages.d("spans", beam_data.spans.keys())
            # Messages.d("supports", beam_data.supports)
            # Messages.d("sections", beam_data.sections)
        pass

    def checkBeamSections(self, spans, beam_name):
        for name, span in spans.items():
            section = span.section_left
            if section not in self.sections.keys():
                #show error message
                error_msg = MessageCodes.ERROR_SPAN_SECTION_NOT_SPECIFIED
                error_msg.setMsg(error_msg.msg%(section,name, beam_name, section))
                Messages.showError(error_msg)

        return True

    def checkBeamLinks(self, spans, beam_name):
        for name, span in spans.items():
            for link in span.links:
                if link not in self.shear_links.keys():
                    #show error message
                    error_msg = MessageCodes.ERROR_SPAN_LINKS_NOT_SPECIFIED
                    error_msg.setMsg(error_msg.msg%(link,name, beam_name, link))
                    Messages.showError(error_msg)

        return True

    def checkBeamSupports(self, supports, beam_name):
        for name, support in supports.items():
            if support not in self.support_types.keys():
                #show error message
                error_msg = MessageCodes.ERROR_SUPPORT_NOT_SPECIFIED
                error_msg.setMsg(error_msg.msg%(support, name, beam_name, support))
                Messages.showError(error_msg)

        return True

    def getBeamDetails(self):
        beam_start_point = list(self.starting_point)
        for beam_name, beam_data in self.beams.items():
            beam = BeamDetails(self, beam_name, beam_data, beam_start_point)
            self.all_beams[beam_name] = beam
            #draw next beam below current beam, change the y value 
            beam_start_point[1] -= 3500

    def getAllBeamsEntities(self):
        all_beams_entities = []
        for beam in self.all_beams.values():
            all_beams_entities.extend(beam.getBeamEntities())

        return all_beams_entities

    def drawSectionEntities(self, starting_point, beam, section):
        sec_coords = section.getCoordinates(starting_point,beam.beam_depth)
        entities = sec_coords.getEntities()
        return entities
            




