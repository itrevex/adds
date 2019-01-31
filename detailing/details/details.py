from detailing.beams.beams import Beams
from .beam_details import BeamDetails

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
            




