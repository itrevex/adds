import ezdxf

from common.constants import Constants

from common.utils import Utils
from common.messages import Messages


class DxfDraw:
    _beam_name = ""
    def __init__(self, app_data):
        self.dwg = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'
        self.msp = self.dwg.modelspace()  # add new entities to the model space
        self.app_data = app_data
        self.addLayersToModelSpace()
        self.setHeaderAttribs()

        pass
    
    def makeDxf(self):
        output_path = self.app_data.getOutPutFile()
        self.dwg.saveas(output_path)
        print ("Generated \"%s\" file"%output_path)
        print()
        input("Press any key to continue . . .")

    def getFileName(self):
        return Utils.dateTimeString() +"-detail.dxf"

    def addDxfLine(self, pt1, pt2, layer_name = '0'):
        # add a LINE entity
        layer = self.getLayer(layer_name)
        self.msp.add_line(pt1, pt2, dxfattribs={'layer': layer})  

    def addDxfCircle(self, center, radius, layer_name = '0'):
        # add a LINE entity
        layer = self.getLayer(layer_name)
        self.msp.add_circle(center, radius,  dxfattribs={'layer': layer})  

    def drawLine(self, line):
        pt1 = line.pt1
        pt2 = line.pt2
        layer = self.getLayer(line.layer)
        self.addDxfLine(pt1, pt2, layer)

    def getLayer(self, layer_name):
        try:
            return self.layers[layer_name][Constants.LAYER_NAME]
        except KeyError:
            return '0'

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
        self.layers = self.app_data.getLayers()
        for layer in self.layers.values():
            name, attribs = self.getLayerAttributes(layer)
            try:
                self.dwg.layers.new(name=name, dxfattribs=attribs)
            except ezdxf.lldxf.const.DXFTableEntryError:
                #log error already exists
                pass

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
            #check to see if entity is line
            if entity.type == Constants.ENTITY_LINE:
                self.addDxfLine(entity.pt1, entity.pt2, entity.layer)
            elif entity.type == Constants.ENTITY_CIRCLE:
                #draw circle
                self.addDxfCircle(entity.centre, entity.radius, entity.layer)