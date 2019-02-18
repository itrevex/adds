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
    TOP = "top"
    BOTTOM = "bottom"

    def __init__(self, type, props):
        self.type = type
        self.column_b = float(props[Column.COLUMN_B])
        self.column_d = float(props[Column.COLUMN_D])
        self.column_h_m = float(props[Column.COLUMN_H_M])

    def setB(self, column_b):
        self.column_b = float(column_b)

    def setD(self, column_d):
        self.column_d = float(column_d)

    def setHm(self, column_h_m):
        self.column_h_m = float(column_h_m)

    def setType(self, type):
        self.type = type