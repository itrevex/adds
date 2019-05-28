import ezdxf
from ezdxf.addons import dimstyles, LinearDimension
from src.common.constants import Constants

from src.common.utils import Utils
from src.common.messages import Messages
from src.common.message_codes import MessageCodes
from .vport import VPort

SHOW_DIMENSIONS = False

class DxfDraw:

    def __init__(self, app_data):
        self.dwg = ezdxf.new('R2010')  # create a new DXF R2010 drawing, official DXF version name: 'AC1024'
        self.msp = self.dwg.modelspace()  # add new entities to the model space
        self.app_data = app_data
        self.addLayersToModelSpace()
        self.addStylesToModelSpace()
        self.setHeaderAttribs()

        #setup dimstyles
        # dimstyles.setup(self.dwg)
        pass
    
    def makeDxf(self, entities, number_of_beams):
        self.drawEntities(entities)
        #setup viewports
        VPort(self.dwg, number_of_beams)

        output_path = self.app_data.getOutPutFile()
        try:
            self.dwg.saveas(output_path)
            Messages.i("")
            Messages.i(MessageCodes.INFO_DXF_GENERATED%output_path)
        except PermissionError:
            Messages.showError(MessageCodes.ERROR_OPEN_DXF)
        
        Messages.continuePrompt(MessageCodes.INFO_CONTINUE_PROMPT)

    def getFileName(self):
        return Utils.dateTimeString() +"-detail.dxf"

    def addDxfLine(self, line):
        # add a LINE entity
        layer = self.getLayer(line.layer)
        self.msp.add_line(line.pt1, line.pt2, 
            dxfattribs={'layer': layer})  

    def addDxfCircle(self, circle):
        # add a Circle entity
        layer = self.getLayer(circle.layer)
        self.msp.add_circle(circle.centre, circle.radius,  
            dxfattribs={'layer': layer})  

    def addDxfTexT(self, text):
        # add a Text entity

        # self.msp .add_circle(center, radius,  dxfattribs={'layer': layer}) 
        layer = self.getLayer(text.layer)
        self.msp.add_text(text.text, dxfattribs={'style': text.style, 
            'height': text.height, 'layer': layer }).set_pos(text.pos, align=text.align)

    def addDxfHatch(self, hatch):
        '''
        hatch has a list of the polyline path.
        Path should be closed
        '''
        layer = self.getLayer(hatch.layer)
        color = self.getLayerColor(hatch.layer)
        dxf_hatch = self.msp.add_hatch(color=color, dxfattribs={'layer': layer})
        with dxf_hatch.edit_boundary() as boundary:
            boundary.add_polyline_path(hatch.path, is_closed=1)

    def addDimEntity(self, dim):
        '''
        add dimesion
        '''
        if SHOW_DIMENSIONS:
            layer = self.getLayer(dim.layer)
            Messages.d("dxf.py", dim.points, dim.starting_point, dim.angle)
            dimline = LinearDimension(dim.starting_point, 
                dim.points, dim.angle, layer=layer)
            dimline.render(self.msp)

    def getLayer(self, layer_name):
        try:
            return self.layers[layer_name][Constants.LAYER_NAME]
        except KeyError:
            return '0'
        
    def getLayerColor(self, layer_name):
        try:
            return self.layers[layer_name][Constants.LAYER_COLOR]
        except KeyError:
            return '7'

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

    def addStylesToModelSpace(self):
        self.styles = self.app_data.getTextStyles()
        for name, attribs in self.styles.items():
            try:
                self.dwg.styles.new(name=name, dxfattribs=attribs)
            except ezdxf.lldxf.const.DXFTableEntryError:
                #log error already exists
                pass

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
                self.addDxfLine(entity)
                pass
            elif entity.type == Constants.ENTITY_CIRCLE:
                #draw circle
                self.addDxfCircle(entity)
                pass
            elif entity.type == Constants.ENTITY_TEXT: 
                #draw text
                self.addDxfTexT(entity)
                pass
            elif entity.type == Constants.ENTITY_HATCH: 
                #draw hatch
                self.addDxfHatch(entity)
                pass
            elif entity.type == Constants.ENTITY_DIMENSION: 
                #draw dimension
                self.addDimEntity(entity)
                pass