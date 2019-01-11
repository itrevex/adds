import ezdxf
import sys

sys.path.append("./common/")
from utils import Utils

class Detailing:
    def __init__(self):
        pass
    
    def start(self):
        dwg = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'

        msp = dwg.modelspace()  # add new entities to the model space
        msp.add_line((0, 0), (10, 0))  # add a LINE entity
        dwg.saveas('output\%s'%self.getFileName())

    def getFileName(self):
        return Utils.dateTimeString() +"-detail.dxf"
