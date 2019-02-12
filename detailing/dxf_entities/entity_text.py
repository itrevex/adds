from common.constants import Constants
from common.messages import Messages
class EntityText:
    '''
    Text entity base class
    
    '''

    def __init__(self, text, pos=(0,0,0), layer="0", 
            style=Constants.GRID_LABEL_STYLE, 
            height=Constants.GRID_TEXT_HEIGHT, align="LEFT"):  
        self.text = text
        self.style = style
        self.height = height
        self.pos = pos
        self.align = align
        self.type = Constants.ENTITY_TEXT
        self.layer = layer

        pass

    def setText(self, text):
        self.text = text

    def setStyle(self, style):
        self.style = style

    def setHeight(self, height):
        self.height = height

    def setPos(self, pos):
        self.pos = pos

    def setAlign(self, align):
        self.align = align

    def getTextLenth(self):
        return len(self.text) * self.height * Constants.CHARACTER_LENGTH_FACTOR
