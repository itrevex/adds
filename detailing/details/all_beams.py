from detailing.beams_input.beams import Beams
from .beam_details import BeamDetails
from common.constants import Constants
from common.messages import Messages

class AllBeamsDetails:

    def __init__(self, app_data):
        
        beams_data = Beams(app_data.getInputData())
        self.beams = beams_data.getBeams()
        self.sections = beams_data.getSections()
        self.support_types = beams_data.getSupportTypes()
        self.shear_links = beams_data.getLinks()
        self.starting_point = list(beams_data.starting_point)
        self.build = beams_data.build
        self.checkBuild()
        self.all_beams = {}
        self.getBeamDetails()

    def checkBuild(self):
        if self.build > Constants.CURRENT_BUILD:
            message = "File you are trying to run is from a later version of Trevexs Adds "
            message += "\nPlease install the latest version to be able to run this file"
            Messages.showError(message)
        elif self.build < Constants.CURRENT_BUILD:
            message = "File you are trying to run is not updated work fully with the current version"
            message += "\nApplication is running in compatible mode"
            message += "\n\nPlease consider updating your file to the latest version"
            
            Messages.showWarning(message)
        else:
            #build number and file being run are compatible
            pass
    
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
            




