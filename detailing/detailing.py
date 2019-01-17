import ezdxf
import sys
sys.path.append("./common/")

from constants import Constants

from utils import Utils
from supports import Supports
from beams.beams import Beams

class Detailing:
    
    def __init__(self, app_data):
        self.dwg = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'
        self.msp = self.dwg.modelspace()  # add new entities to the model space
        self.app_data = app_data
        self.addLayersToModelSpace()
        self.setHeaderAttribs()
        self.drawSupports()
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

    def trials(self):
        Beams(self.app_data.getInputData()).getStartingPoint()
        




