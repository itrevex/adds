import sys
sys.path.append("../common/")

from constants import Constants

class Column:
    '''
    Column has the column section properties
    and the column height
    column_b - column section width
    column_d - column section height
    column_h_m - column height in m

    '''

    def __init__(self, type, props):
        self.type = type
        self.column_b = props[Constants.COLUMN_B]
        self.column_d = props[Constants.COLUMN_D]
        self.column_h_m = props[Constants.COLUMN_H_M]

    def setB(self, column_b):
        self.column_b = column_b

    def setD(self, d):
        self.column_d = column_d

    def setHm(self, column_h_m):
        self.column_h_m = column_h_m

    def setType(self, type):
        self.type = type