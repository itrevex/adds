from common.messages import Messages

class Column:
    '''
    Column has the column section properties
    and the column height
    b - column section width, represents length along beam
    d - column section height
    h - column height in m

    '''

    COLUMN_B = 0
    COLUMN_D = 1
    COLUMN_H_M = 2
    COLUMN_OFFSET = 3
    TOP = "top"
    BOTTOM = "bottom"

    def __init__(self, type, props):
        self.type = type
        self.props = props
        self.b = self.getValue(Column.COLUMN_B)
        self.d = self.getValue(Column.COLUMN_D)
        self.h = self.getValue(Column.COLUMN_H_M)
        self.offset = self.getValue(Column.COLUMN_OFFSET) 
        
    def getValue(self, index):
        try:
            if self.props[index].lower() == 'x':
                return 0.
            return float(self.props[index])
        except (IndexError):
            return 0.

    def setB(self, b):
        self.b = float(b)

    def setD(self, d):
        self.d = float(d)

    def setHm(self, h):
        self.h = float(h)

    def setType(self, type):
        self.type = type

    def toString(self):
        string = "\ntype = "+ str(self.type)
        string += "\nb = " + str(self.b)
        string += "\nd = " + str(self.d)
        string += "\nh = " + str(self.h)
        string += "\noffset = " + str(self.offset)

        return string