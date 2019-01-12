import ezdxf
import sys

sys.path.append("./common/")
from utils import Utils
from constants import Constants
from center_line import CenterLine

class Detailing:
    
    def __init__(self):
        self.dwg = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'
        self.msp = self.dwg.modelspace()  # add new entities to the model space

        self.drawSupport()
        pass
    
    def makeDxf(self):
        self.dwg.saveas('output\%s'%self.getFileName())

    def getFileName(self):
        return Utils.dateTimeString() +"-detail.dxf"

    def drawSupport(self):
        '''
        **Routine for sorting the beam supports before plotting**
	
        pt1 = line beginning point                                                 
        pt = Initial point                                                         
        sw = column section width													
        nos =  Number of column sections 											       
        i = nos counter
        '''	
        
        centreline = CenterLine(Constants.START_POINT, 400, 300)
        self.drawLine(centreline.pt1, centreline.pt2)
        												
    def drawLine(self, pt1, pt2):
        self.msp.add_line(pt1, pt2)  # add a LINE entity