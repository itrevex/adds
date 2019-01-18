class Column:
    '''
    Column has the column section properties
    and the column height
    column_b - column section width
    column_d - column section height
    column_h_m - column height in m

    '''

    COLUMN_B = "section_b"
    COLUMN_D = "section_d"
    COLUMN_H_M = "column_h_m"

    def __init__(self, type, props):
        self.type = type
        self.column_b = props[Column.COLUMN_B]
        self.column_d = props[Column.COLUMN_D]
        self.column_h_m = props[Column.COLUMN_H_M]

    def setB(self, column_b):
        self.column_b = column_b

    def setD(self, d):
        self.column_d = column_d

    def setHm(self, column_h_m):
        self.column_h_m = column_h_m

    def setType(self, type):
        self.type = type