from support import Support
from constants import Constants

class Supports:
    def __init__(self, app_data):
        self.app_data = app_data
        self.loadSupportsData()
        self.number_of_supports = len(self.column_section_widths)
        self.generateSupports()
        pass
    
    def generateSupports(self):
        column_starting_point = list(self.starting_point)
        self.supports = []
        for support_index in range(self.number_of_supports):
            column_starting_point = self.getColumnStartingPoint(support_index, 
                column_starting_point)
            # print(column_starting_point)
            attribs ={
                Support.STARTING_POINT: column_starting_point,
                Support.BEAM_DEPTH:self.beam_depth,
                Support.COLUMN_SECTION_WIDTH: self.column_section_widths[support_index],
                Support.SUPPORT_LOCATION: self.getSupportLocation(support_index)
            }
            self.supports.append(Support(attribs))
        pass

    def getColumnStartingPoint(self, support_index,column_starting_point):
        
        if(support_index != 0):
            column_starting_point[Constants.X] += \
                (self.column_centre_centre_lengths[support_index - 1] \
                + 0.5 * self.column_section_widths[support_index - 1] \
                - 0.5 * self.column_section_widths[support_index])\
                * Constants.SCALE_FACTOR_COLUMNS

        return column_starting_point
    
    def getSupportLocation(self,support_index):
        if(support_index == 0):
            #starting support
            return Constants.SUPPORT_START
        if(support_index == self.number_of_supports -1):
            #last support
            return Constants.SUPPORT_END
        return Constants.SUPPORT_MID

    def loadSupportsData(self):
        self.input_data = self.app_data.getInputData()
        self.starting_point = tuple(map(float, self.input_data[Constants.STARTING_POINT]))
        self.supports_attribs = self.input_data[Constants.SUPPORTS]
        self.beam_depth = float(self.supports_attribs[Constants.BEAM_DEPTH])
        self.column_section_widths = list(map(float, self.supports_attribs[Constants.COLUMN_SECION_WIDTH]))
        self.column_centre_centre_lengths \
            = list(map(float, self.supports_attribs[Constants.COLUMN_CENTRE_CENTRE_LENGTHS]))


    def getSupportEntites(self):
        '''
        create list support drawable entities
        each entity must have point 1 (x, y, z ), point 2 (x,y,z)
        and a layer
        '''
        entities = []
        for support in self.supports:
            print(support.starting_point)
            entities.extend(support.getSupportObjects())
        return entities



    
