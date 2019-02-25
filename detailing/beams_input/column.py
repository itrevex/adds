from common.messages import Messages
class Column:
    '''
    Column has the column section properties
    and the column height
    column_b - column section width, represents length along beam
    column_d - column section height
    column_h_m - column height in m

    '''

    COLUMN_B = 0
    COLUMN_D = 1
    COLUMN_H_M = 2
    COLUMN_OFFSET = 3
    TOP = "top"
    BOTTOM = "bottom"

    def __init__(self, type, props):
        self.type = type
        Messages.d(props)
        self.props = props
        self.column_b = float(props[Column.COLUMN_B])
        self.column_d = float(props[Column.COLUMN_D])
        self.column_h_m = self.getValue(Column.COLUMN_H_M)
        self.offset = self.getValue(Column.COLUMN_OFFSET) 
    
    def getValue(self, index):
        try:
            return float(self.props[index])
        except (IndexError):
            return 0.

    def setB(self, column_b):
        self.column_b = float(column_b)

    def setD(self, column_d):
        self.column_d = float(column_d)

    def setHm(self, column_h_m):
        self.column_h_m = float(column_h_m)

    def setType(self, type):
        self.type = type