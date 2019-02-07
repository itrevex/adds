from common.constants import Constants

class LinkType:
    '''
    Defines A link
    This class will be used to calculate the links labels and return
    offset on the end depending on whether the links span length is 
    provided or not

    diameter: Strength and diameter of link
    bar_mark: Bar mark for link
    shape_code: Shape code for link BS 8666: 2005
    spacing: Link spacing
    offset: Offset from edge of support, default is 50
    length: 2.3 
    '''
    DIAMETER = "diameter"
    BAR_MARK = "bar_mark"
    SHAPE_CODE = "shape_code"
    SPACING = "spacing" 
    OFFSET = "offset" 
    LENGTH = "length"  

    def __init__(self, name, links):
        self.links_input = links
        self.name = name
        self.diameter = self.getValue(LinkType.DIAMETER)
        self.bar_mark = self.getValue(LinkType.BAR_MARK)
        self.shape_code = self.getValue(LinkType.SHAPE_CODE)
        self.spacing = self.getValue(LinkType.SPACING)
        self.offset = self.getOffset()
        self.length = self.getLength() 

    
    def getValue(self, key):
        return self.links_input[key]
    
    def getLength(self):
        try:
            return self.links_input(LinkType.LENGTH)
        except KeyError:
            return None
        

    def getOffset(self):
        try:
            return self.links_input(LinkType.OFFSET)
        except KeyError:
            return Constants.LINKS_DEFAULT_OFFSET 


        